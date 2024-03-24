class BipartiteGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
        self.color = [-1] * num_vertices  # Color of each vertex, initialized to -1

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def is_bipartite(self, src=0):
        queue = [src]
        self.color[src] = 0  # Color the source vertex with 0

        while queue:
            u = queue.pop(0)

            for v in self.adj_list[u]:
                if self.color[v] == -1:
                    self.color[v] = 1 - self.color[u]  # Assign opposite color to adjacent vertices
                    queue.append(v)
                elif self.color[v] == self.color[u]:
                    return False  # If adjacent vertices have same color, not bipartite

        return True