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
