import networkx as nx
from sklearn.ensemble import RandomForestRegressor
from src.models.train_shortest_path_model import generate_training_data
import joblib
import logging

logging.basicConfig(level=logging.INFO)

def adapt_model_to_new_graph(model, G):
    """
    Adapt the given model to a new graph by retraining it on the new graph's data.
    """
    try:
        data, labels = generate_training_data(G)
        
        if not data or not labels:
            logging.error("No valid training data generated from the graph.")
            return None
        
        model.fit(data, labels)
        logging.info("Model successfully adapted to the new graph.")
        return model
    except Exception as e:
        logging.error(f"Failed to adapt model: {e}")
        return None

def evaluate_model_on_new_task(model, G, source, target):
    """
    Evaluate the adapted model's accuracy on predicting the shortest path between the source and target in the new graph.
    """
    try:
        actual_length = nx.shortest_path_length(G, source=source, target=target)
        predicted_length = model.predict([[source, target]])[0]
        
        # Accuracy can be defined as how close the predicted length is to the actual length
        accuracy = 1 - abs(predicted_length - actual_length) / actual_length
        
        logging.info(f"Evaluating model: Actual length = {actual_length}, Predicted length = {predicted_length}, Accuracy = {accuracy}")
        return accuracy
    except nx.NetworkXNoPath:
        logging.warning(f"No path between {source} and {target} in the graph.")
        return 0
    except Exception as e:
        logging.error(f"Error during model evaluation: {e}")
        return 0

if __name__ == "__main__":
    # Example usage
    model = joblib.load("src/models/compressed_shortest_path_model.pkl")
    G = nx.gnm_random_graph(100, 200)
    adapted_model = adapt_model_to_new_graph(model, G)
    if adapted_model:
        joblib.dump(adapted_model, "src/models/adapted_shortest_path_model.pkl")
