import networkx as nx

def dijkstra_shortest_path(G, source, target):
    """
    Calculate the shortest path between source and target nodes using Dijkstra's algorithm.
    """
    try:
        path = nx.dijkstra_path(G, source=source, target=target)
        length = nx.dijkstra_path_length(G, source=source, target=target)
        return path, length
    except nx.NetworkXNoPath:
        return [], float('inf')

def bellman_ford_shortest_path(G, source, target):
    """
    Calculate the shortest path between source and target nodes using the Bellman-Ford algorithm.
    """
    try:
        path = nx.bellman_ford_path(G, source=source, target=target)
        length = nx.bellman_ford_path_length(G, source=source, target=target)
        return path, length
    except nx.NetworkXNoPath:
        return [], float('inf')

def floyd_warshall_shortest_paths(G):
    """
    Compute the shortest paths between all pairs of nodes using the Floyd-Warshall algorithm.
    Returns a dictionary of dictionaries keyed by source and target nodes.
    """
    try:
        paths = dict(nx.floyd_warshall(G))
        return paths
    except Exception as e:
        return {}

if __name__ == "__main__":
    # Example usage with a generated graph
    G = nx.gnm_random_graph(100, 200)
    
    source, target = list(G.nodes())[0], list(G.nodes())[-1]
    
    path, length = dijkstra_shortest_path(G, source, target)
    print(f"Dijkstra path from {source} to {target}: {path}, length: {length}")
    
    path, length = bellman_ford_shortest_path(G, source, target)
    print(f"Bellman-Ford path from {source} to {target}: {path}, length: {length}")
    
    all_pairs_paths = floyd_warshall_shortest_paths(G)
    print(f"Floyd-Warshall shortest paths: {all_pairs_paths}")
