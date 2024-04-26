import networkx as nx
from collections import defaultdict

def construct_dual_graph(G):
    """
    Construct the dual graph D(G) based on the provided instructions.

    Parameters:
        G (networkx.Graph): Input graph.

    Returns:
        networkx.Graph: Dual graph D(G).
    """
    dual_graph = nx.Graph()
    edge_weights = defaultdict(int)

    for vi in G.nodes():
        if vi in dual_graph.nodes():
            continue
        
        dual_graph.add_node(vi)

        # Enumerate the list of assets connected to vi
        assets_connected_to_vi = [neighbor for neighbor in G.neighbors(vi)]

        for vj in assets_connected_to_vi:
            if vj not in dual_graph.nodes():
                dual_graph.add_node(vj)
            
            # Add edge (vi, vj) to the dual graph
            if dual_graph.has_edge(vi, vj):
                edge_weights[(vi, vj)] += 1
            else:
                dual_graph.add_edge(vi, vj)
                edge_weights[(vi, vj)] = 1
    
    # Add weights to edges
    for edge, weight in edge_weights.items():
        dual_graph[edge[0]][edge[1]]['weight'] = weight

    return dual_graph

# Example usage
G = nx.Graph()
# Add vulnerability vertices
G.add_nodes_from(['v1', 'v2', 'v3'])
# Add edges between vulnerability and asset vertices
G.add_edges_from([('v1', 'a1'), ('v1', 'a2'), ('v2', 'a1'), ('v2', 'a3'), ('v3', 'a2'), ('v3', 'a3')])
dual_graph = construct_dual_graph(G)
print("Dual Graph Nodes:", dual_graph.nodes())
print("Dual Graph Edges:", dual_graph.edges(data=True))
