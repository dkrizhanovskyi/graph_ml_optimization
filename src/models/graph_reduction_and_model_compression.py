import networkx as nx
from sklearn.ensemble import RandomForestRegressor
import joblib
import logging

logging.basicConfig(level=logging.INFO)

def reduce_graph_size(G, percentage=0.5):
    """
    Reduce the size of the graph by a specified percentage.
    This can be useful for model compression or reducing computational complexity.
    """
    num_nodes_to_remove = int(len(G) * percentage)
    
    nodes_to_remove = list(G.nodes())[:num_nodes_to_remove]
    G_reduced = G.copy()
    G_reduced.remove_nodes_from(nodes_to_remove)
    
    logging.info(f"Reduced graph size by {percentage * 100}%. Number of nodes removed: {num_nodes_to_remove}")
    return G_reduced

def compress_model(model):
    """
    Apply model compression techniques to reduce the size of the trained model.
    This function currently supports reducing the number of trees in a Random Forest.
    """
    if isinstance(model, RandomForestRegressor):
        original_num_trees = len(model.estimators_)
        compressed_model = RandomForestRegressor(
            n_estimators=int(original_num_trees * 0.5),
            random_state=42
        )
        compressed_model.fit(model.estimators_[0].estimators_, model.estimators_)
        
        logging.info(f"Compressed model by reducing the number of trees from {original_num_trees} to {len(compressed_model.estimators_)}.")
        return compressed_model
    else:
        logging.warning("Model compression not supported for this type of model.")
        return model

if __name__ == "__main__":
    # Example usage with a generated graph
    G = nx.gnm_random_graph(100, 200)
    G_reduced = reduce_graph_size(G, percentage=0.5)
    
    model = joblib.load("src/models/compressed_shortest_path_model.pkl")
    compressed_model = compress_model(model)
    joblib.dump(compressed_model, "src/models/compressed_shortest_path_model.pkl")
    logging.info("Compressed model saved to src/models/compressed_shortest_path_model.pkl")
