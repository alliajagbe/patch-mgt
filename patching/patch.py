import networkx as nx
import pyomo.core as pyo
import classiq
from classiq import construct_combinatorial_optimization_model, set_execution_preferences, write_qmod, show, synthesize, execute
from classiq.applications.combinatorial_optimization import OptimizerConfig, QAOAConfig, get_optimization_solution_from_pyo
from classiq.execution import ClassiqBackendPreferences, ExecutionPreferences, VQESolverResult
import matplotlib.pyplot as plt
import pandas as pd

def mvc(graph: nx.Graph) -> pyo.ConcreteModel:
    model = pyo.ConcreteModel()
    model.x = pyo.Var(graph.nodes, domain=pyo.Binary)
    nodes = list(graph.nodes())

    @model.Constraint(graph.edges)
    def full_cover(model, i, j):
        # all sets are covered
        return ((1 - model.x[i]) * (1 - model.x[j])) == 0

    def obj_expression(model):
        # number of nodes selected
        return sum(model.x.values())

    model.cost = pyo.Objective(rule=obj_expression, sense=pyo.minimize)

    return model

edge_dict = {
    1: ["A", "B", "D", "F"],
    2: ["A", "B"],
    3: ["A", "D", "E"],
    4: ["B", "C", "F"],
    5: ["G"],
    6: ["F", "G"],
    7: ["B", "C", "F"],
    8: ["C", "D", "G"],
}
#-------------------------------------------------------
B = nx.Graph()
B.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8], bipartite=0)
B.add_nodes_from(["A", "B", "C", "D", "E", "F", "G"], bipartite=1)
for u in range(1, 9):
    for v in edge_dict[u]:
        B.add_edge(u, v)
X, Y = nx.bipartite.sets(B)
#------------------------------------------------------
B_dual = nx.Graph()

B_2 = B.copy()

S, T = nx.bipartite.sets(B_2)

def gen_dual(B_2, S=None):
    B_2c = B_2.copy()
    DualG = nx.Graph()
    if not S:
        S, _ = nx.bipartite.sets(B_2c)
    for s in S:
        DualG.add_node(s)
        # iter over all nodes s talks to
        for t1 in B_2c.neighbors(s):
            for t2 in B_2c.neighbors(t1):
                if t2 != s:
                    DualG.add_edge(s, t2)
        B_2c.remove_node(s)
    return DualG

DG = gen_dual(B_2, S)
#------------------------------------------------------
mvc_model = mvc(DG)
print(mvc_model.pprint())
#------------------------------------------------------
qaoa_config = QAOAConfig(num_layers=1)
def prepare_classiq(should_write):
    optimizer_config = OptimizerConfig(max_iteration=60, alpha_cvar=0.9)
    qmod = construct_combinatorial_optimization_model(
        pyo_model=mvc_model,
        qaoa_config=qaoa_config,
        optimizer_config=optimizer_config,
    )
    backend_preferences = ExecutionPreferences(
        backend_preferences=ClassiqBackendPreferences(backend_name="aer_simulator")
    )
    qmod = set_execution_preferences(qmod, backend_preferences)
    if should_write:
        write_qmod(qmod, "patching_mvc")
    return qmod

qmod = prepare_classiq(should_write=True)

classiq.authenticate()
#------------------------------------------------------
qprog = synthesize(qmod)
show(qprog)
#------------------------------------------------------
res = execute(qprog).result()
print(res)
#------------------------------------------------------
vqe_result = VQESolverResult.parse_obj(res[0].value)
plt.figure(figsize=(20, 10))
vqe_result.convergence_graph
plt.show()
#------------------------------------------------------
solution = get_optimization_solution_from_pyo(
    mvc_model, vqe_result=vqe_result, penalty_energy=qaoa_config.penalty_energy
)
optimization_result = pd.DataFrame.from_records(solution)
optimization_result = optimization_result.sort_values(by="cost", ascending=True)
optimization_result.to_csv("patching_mvc_result.csv")
#------------------------------------------------------
plt.figure(figsize=(20, 10))
optimization_result.hist("cost", weights=optimization_result["probability"])
plt.show()
#------------------------------------------------------
best_solution = optimization_result.solution[optimization_result.cost.idxmin()]
print("Best Solution found:",best_solution)
#------------------------------------------------------
def draw_solution(graph: nx.Graph, solution: list):
    solution_nodes = [v for v in graph.nodes if solution[v - 1]]
    solution_edges = [
        (u, v) for u, v in graph.edges if u in solution_nodes or v in solution_nodes
    ]
    nx.draw_kamada_kawai(graph, with_labels=True)
    nx.draw_kamada_kawai(
        graph,
        nodelist=solution_nodes,
        edgelist=solution_edges,
        node_color="r",
        edge_color="y",
    )
plt.figure(figsize=(20, 10))
draw_solution(DG, best_solution)
plt.show()
#------------------------------------------------------
check_B = B.copy()
vc2 = [v for v in DG.nodes if best_solution[v - 1]]
for v in vc2:
    check_B.remove_node(v)

plt.figure(figsize=(20, 10))
nx.draw(
    check_B,
    pos=nx.bipartite_layout(check_B, S),
    with_labels=True,
    font_color="whitesmoke",
)
plt.show()