import unittest
from bipartite import BipartiteGraph

class TestBipartiteGraph(unittest.TestCase):
    def test_bipartite_graph(self):
        # Test a bipartite graph
        graph = BipartiteGraph(6)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 4)
        graph.add_edge(3, 5)
        graph.add_edge(4, 5)

        self.assertTrue(graph.is_bipartite(), "Graph should be bipartite")
        print("Graph is bipartite. Test passed.")

        graph2 = BipartiteGraph(4)
        graph2.add_edge(0, 1)
        graph2.add_edge(1, 2)
        graph2.add_edge(2, 3)
        graph2.add_edge(3, 0)

        self.assertTrue(graph2.is_bipartite(), "Graph should be bipartite")
        print("Graph is bipartite. Test passed.")

    def test_non_bipartite_graph(self):
        # Test a non-bipartite graph
        graph = BipartiteGraph(5)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 4)
        graph.add_edge(3, 4)

        self.assertFalse(graph.is_bipartite(), "Graph should not be bipartite")
        print("Graph is not bipartite. Test passed.")

if __name__ == "__main__":
    unittest.main()
