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