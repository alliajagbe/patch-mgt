import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def vertex_cover(self):
        visited = [False] * self.V
        cover = []

        for u in range(self.V):
            if not visited[u]:
                for v in self.graph[u]:
                    if not visited[v]:
                        visited[u] = visited[v] = True
                        cover.append(u)
                        cover.append(v)
                        break

        return cover

    def visualize_graph(self):
        G = nx.Graph()
        for u in range(self.V):
            for v in self.graph[u]:
                G.add_edge(u, v)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', node_size=700, edge_color='gray')
        plt.title("Graph Visualization")
        plt.show()

    def visualize_vertex_cover(self):
        G = nx.Graph()
        for u in range(self.V):
            for v in self.graph[u]:
                G.add_edge(u, v)

        cover = self.vertex_cover()
        cover_nodes = set(cover)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', node_size=700, edge_color='gray')
        nx.draw_networkx_nodes(G, pos, nodelist=cover_nodes, node_color='salmon', node_size=700)
        plt.title("Vertex Cover Visualization")
        plt.show()


# testing
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

print("Graph:")
g.visualize_graph()

print("Vertex Cover:")
g.visualize_vertex_cover()
