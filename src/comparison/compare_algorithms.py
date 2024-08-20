import time
import networkx as nx
from src.algorithms.classical_algorithms import dijkstra_shortest_path, bellman_ford_shortest_path, floyd_warshall_shortest_paths
import logging

logging.basicConfig(level=logging.INFO)

def compare_algorithms(G, source, target):
    """
    Compare the performance of different shortest path algorithms on the graph G.
    Measures both execution time and accuracy.
    """
    algorithms = {
        "Dijkstra": dijkstra_shortest_path,
        "Bellman-Ford": bellman_ford_shortest_path,
        "Floyd-Warshall": floyd_warshall_shortest_paths
    }
    
    results = {}
    
    for name, algorithm in algorithms.items():
        start_time = time.time()
        
        if name == "Floyd-Warshall":
            all_pairs_paths = algorithm(G)
            path = all_pairs_paths[source][target] if target in all_pairs_paths[source] else None
            length = nx.shortest_path_length(G, source=source, target=target) if path else float('inf')
        else:
            path, length = algorithm(G, source, target)
        
        end_time = time.time()
        duration = end_time - start_time
        
        results[name] = {
            "path": path,
            "length": length,
            "time": duration
        }
        
        logging.info(f"{name} algorithm: path length = {length}, time taken = {duration} seconds")
    
    return results

if __name__ == "__main__":
    # Example usage with a generated graph
    G = nx.gnm_random_graph(100, 200)
    source, target = list(G.nodes())[0], list(G.nodes())[-1]
    
    results = compare_algorithms(G, source, target)
    for algorithm, result in results.items():
        logging.info(f"{algorithm} result: {result}")
