import networkx as nx
import matplotlib.pyplot as plt
from bipartite import BipartiteGraph

def visualize_bipartite_graph(graph):
    G = nx.Graph()

    # adding nodes with the "bipartite" attribute set to 0 or 1
    G.add_nodes_from(range(graph.num_vertices), bipartite=0)
    G.add_nodes_from(range(graph.num_vertices, 2 * graph.num_vertices), bipartite=1)

    for u in range(graph.num_vertices):
        for v in graph.adj_list[u]:
            G.add_edge(u, v + graph.num_vertices)

    # assigning respective positions to nodes
    pos = {}
    pos.update((node, (1, index)) for index, node in enumerate(range(graph.num_vertices)))
    pos.update((node, (2, index)) for index, node in enumerate(range(graph.num_vertices, 2 * graph.num_vertices)))

    nx.draw(G, pos, with_labels=True, node_color=["lightblue" if node < graph.num_vertices else "lightgreen" for node in G.nodes], node_size=500, font_size=12)
    plt.title("Bipartite Graph")
    plt.show()


# testing
if __name__ == "__main__":
    graph = BipartiteGraph(6)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)

    visualize_bipartite_graph(graph)
