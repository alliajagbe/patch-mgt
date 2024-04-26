import networkx as nx
import matplotlib.pyplot as plt

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

B = nx.Graph()
B.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8], bipartite=0) # these are the vulnerability nodes
B.add_nodes_from(["A", "B", "C", "D", "E", "F", "G"], bipartite=1) # these are the asset nodes
for u in range(1, 9):
    for v in edge_dict[u]:
        B.add_edge(u, v)
X, Y = nx.bipartite.sets(B)
nx.draw(B, pos=nx.bipartite_layout(B, X), with_labels=True, font_color="whitesmoke")
plt.show()


B_dual = nx.Graph()

B_2 = B.copy()

S, T = nx.bipartite.sets(B_2)
# nx.draw(B_2, pos=nx.bipartite_layout(B_2,S), with_labels=True)


# iterate over one side of the bipartite graph
# and construct the dual from the paper.
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
nx.draw(DG, pos=nx.circular_layout(DG), with_labels=True, font_color="whitesmoke")
plt.show()