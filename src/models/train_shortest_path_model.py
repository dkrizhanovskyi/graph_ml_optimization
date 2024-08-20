import networkx as nx
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import logging

logging.basicConfig(level=logging.INFO)

def generate_training_data(G):
    """
    Generate training data for the shortest path model.
    For each pair of nodes, compute the shortest path length.
    """
    data = []
    labels = []

    for source in G.nodes():
        for target in G.nodes():
            if source != target:
                try:
                    length = nx.shortest_path_length(G, source=source, target=target)
                    data.append([source, target])
                    labels.append(length)
                except nx.NetworkXNoPath:
                    logging.warning(f"No path between {source} and {target}.")
                    continue

    return data, labels

def train_model(G):
    """
    Train a machine learning model to predict the shortest path length between nodes.
    """
    # Generate training data
    data, labels = generate_training_data(G)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    
    # Train a Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model on the test set
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    logging.info(f"Model trained with MSE: {mse}")
    
    # Save the trained model
    joblib.dump(model, "src/models/compressed_shortest_path_model.pkl")
    logging.info("Model saved to src/models/compressed_shortest_path_model.pkl")

    return model

if __name__ == "__main__":
    # Example usage with a generated graph
    G = nx.gnm_random_graph(100, 200)
    train_model(G)
