from flask import Flask, request, jsonify
import joblib
import networkx as nx
import os
import logging
from src.algorithms.classical_algorithms import dijkstra_shortest_path
from src.models.train_shortest_path_model import generate_training_data, train_model
from src.models.graph_reduction_and_model_compression import compress_model, reduce_graph_size
from src.models.adapt_models_for_new_graphs import adapt_model_to_new_graph, evaluate_model_on_new_task

# Set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict the shortest path length using the machine learning model.
    This endpoint expects JSON input with source and target nodes, and an optional graph file path.
    """
    data = request.get_json()
    
    source = data['source']
    target = data['target']
    
    # Validate input types
    if not isinstance(source, str) or not isinstance(target, str):
        return jsonify({'error': 'Invalid input data types.'}), 400
    
    # Load the graph from the provided file or use the default path
    graph_file = data.get('graph_file', "data/processed/social_networks/facebook_graph.edgelist")
    
    # Check if the file exists before loading
    if not os.path.exists(graph_file):
        logging.error(f"Graph file {graph_file} not found.")
        return jsonify({'error': f"Graph file {graph_file} not found."}), 400
    
    G = nx.read_edgelist(graph_file)
    
    # Check if the graph is empty
    if G.number_of_nodes() == 0:
        logging.error("Graph is empty.")
        return jsonify({'error': 'Graph is empty.'}), 400
    
    # Check for self-loop case
    if source == target and G.has_edge(source, target):
        logging.info(f"Self-loop detected for node {source}.")
        return jsonify({'predicted_length': 0})
    
    # Load the pre-trained machine learning model
    model = joblib.load("src/models/compressed_shortest_path_model.pkl")
    
    # Predict the shortest path length between the source and target nodes
    predicted_length = model.predict([[source, target]])[0]
    
    logging.info(f"Predicted length from {source} to {target} is {predicted_length}.")
    
    # Return the predicted length as a JSON response
    return jsonify({'predicted_length': int(predicted_length)})

@app.route('/dijkstra', methods=['POST'])
def dijkstra():
    """
    Calculate the shortest path length using Dijkstra's algorithm.
    This endpoint expects JSON input with source and target nodes, and an optional graph file path.
    """
    data = request.get_json()
    source = data['source']
    target = data['target']
    
    # Load the graph from the provided file or use the default path
    graph_file = data.get('graph_file', "data/processed/social_networks/facebook_graph.edgelist")
    G = nx.read_edgelist(graph_file)
    
    # Compute the shortest path and its length using Dijkstra's algorithm
    path, length = dijkstra_shortest_path(G, source, target)
    
    logging.info(f"Dijkstra path from {source} to {target} is {path} with length {length}.")
    
    # Return the path and length as a JSON response
    return jsonify({'path': path, 'length': length})

@app.route('/adapt', methods=['POST'])
def adapt():
    """
    Adapt the machine learning model to a new graph.
    This endpoint expects JSON input with the graph file path. 
    It adapts the pre-trained model to the new graph and saves the adapted model.
    """
    data = request.get_json()
    
    # Load the new graph from the provided file path
    graph_file = data['graph_file']
    G = nx.read_graphml(graph_file)
    
    # Load the pre-trained machine learning model
    model = joblib.load("src/models/compressed_shortest_path_model.pkl")
    
    # Adapt the model to the new graph
    adapted_model = adapt_model_to_new_graph(model, G)
    
    if adapted_model:
        # Save the adapted model if adaptation was successful
        joblib.dump(adapted_model, "src/models/adapted_shortest_path_model.pkl")
        logging.info(f"Model adapted and saved for graph {graph_file}.")
        return jsonify({'status': 'Model adapted and saved.'})
    else:
        logging.error(f"Adaptation failed for graph {graph_file} due to no valid path.")
        # Return an error message if adaptation failed due to no valid path
        return jsonify({'status': 'Adaptation failed due to no valid path in the graph.'}), 400

@app.route('/evaluate', methods=['POST'])
def evaluate():
    """
    Evaluate the adapted model on a new task.
    This endpoint expects JSON input with source and target nodes, and the graph file path.
    It returns the accuracy of the adapted model on the specified task.
    """
    data = request.get_json()
    source = data['source']
    target = data['target']
    
    # Check if the adapted model exists before attempting to load it
    model_path = "src/models/adapted_shortest_path_model.pkl"
    
    if not os.path.exists(model_path):
        # Return an error if the adapted model is not found
        logging.error("Adapted model not found. Please adapt the model first.")
        return jsonify({'error': 'Adapted model not found. Please adapt the model first.'}), 400
    
    # Load the adapted machine learning model
    adapted_model = joblib.load(model_path)
    
    # Load the graph from the provided file path
    graph_file = data['graph_file']
    G = nx.read_graphml(graph_file)
    
    # Evaluate the adapted model's accuracy on the new task
    accuracy = evaluate_model_on_new_task(adapted_model, G, source, target)
    
    logging.info(f"Evaluation accuracy for adapted model on graph {graph_file}: {accuracy}.")
    
    # Return the accuracy as a JSON response
    return jsonify({'accuracy': accuracy})

if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)
