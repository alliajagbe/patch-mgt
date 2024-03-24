import unittest

from vertexCover import Graph

class TestVertexCover(unittest.TestCase):
    def test_vertex_cover(self):
        g1 = Graph(7)
        g1.add_edge(0, 1)
        g1.add_edge(0, 2)
        g1.add_edge(1, 3)
        g1.add_edge(4, 1)
        g1.add_edge(2, 4)
        g1.add_edge(5, 4)
        g1.add_edge(6, 4)
        cover1 = g1.vertex_cover()
        self.assertTrue(all(any(u in edge or v in edge for edge in g1.graph.items()) for u, v in zip(cover1[::2], cover1[1::2])))
        print("Test Passed!")

        g2 = Graph(4)
        g2.add_edge(0, 1)
        g2.add_edge(1, 2)
        g2.add_edge(2, 3)
        cover2 = g2.vertex_cover()
        self.assertTrue(all(any(u in edge or v in edge for edge in g2.graph.items()) for u, v in zip(cover2[::2], cover2[1::2])))
        print("Test Passed!")

        g3 = Graph(7)
        g3.add_edge(0, 1)
        g3.add_edge(0, 2)
        g3.add_edge(1, 3)
        g3.add_edge(3, 4)
        g3.add_edge(4, 5)
        g3.add_edge(5, 6)
        cover3 = g3.vertex_cover()
        self.assertTrue(all(any(u in edge or v in edge for edge in g3.graph.items()) for u, v in zip(cover3[::2], cover3[1::2])))
        print("Test Passed!")

if __name__ == "__main__":
    unittest.main()