import networkx as nx
import matplotlib.pyplot as plt

kill_chain_example_edge_dict = {1: ["B", "F"], 4: ["F", "C"], 8: ["C"]}

B_example = nx.Graph()
B_example.add_nodes_from([1, 4, 8], bipartite=0)
B_example.add_nodes_from(["B", "C", "F"], bipartite=1)
for u in [1, 4, 8]:
    for v in kill_chain_example_edge_dict[u]:
        B_example.add_edge(u, v)
nx.draw(B_example, with_labels=True, font_color="whitesmoke")
plt.show()

X, Y = nx.bipartite.sets(B_example)
nx.draw(
    B_example,
    pos=nx.bipartite_layout(B_example, X),
    with_labels=True,
    font_color="whitesmoke",
)
plt.show()