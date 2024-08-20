import networkx as nx
import random
import logging

logging.basicConfig(level=logging.INFO)

def add_random_edges(G, num_edges):
    """
    Add a specified number of random edges to the graph G.
    """
    possible_edges = list(nx.non_edges(G))
    random.shuffle(possible_edges)
    
    edges_to_add = possible_edges[:num_edges]
    G.add_edges_from(edges_to_add)
    
    logging.info(f"Added {num_edges} random edges to the graph.")
    return G

def add_noise_to_edges(G, noise_level=0.1):
    """
    Add noise to the weights of the edges in the graph.
    The noise level determines the fraction of the original weight added as noise.
    """
    for u, v, d in G.edges(data=True):
        if 'weight' in d:
            noise = random.uniform(-1, 1) * noise_level * d['weight']
            d['weight'] += noise
    
    logging.info(f"Added noise to the edges with a noise level of {noise_level}.")
    return G

def augment_graph(G, num_edges=10, noise_level=0.1):
    """
    Augment the graph by adding random edges and noise to edge weights.
    """
    G_augmented = add_random_edges(G, num_edges)
    G_augmented = add_noise_to_edges(G_augmented, noise_level)
    
    logging.info("Graph augmentation complete.")
    return G_augmented

if __name__ == "__main__":
    # Example usage with a generated graph
    G = nx.gnm_random_graph(100, 200)
    G_augmented = augment_graph(G, num_edges=15, noise_level=0.05)
    nx.write_edgelist(G_augmented, "data/processed/augmented_graph.edgelist")
    logging.info("Augmented graph saved to data/processed/augmented_graph.edgelist")
