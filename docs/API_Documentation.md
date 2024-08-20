# API Documentation for Graph ML Optimization Project

This document provides details on how to interact with the RESTful API developed for the Graph ML Optimization Project. The API allows users to perform various operations related to graph optimization using classical algorithms and machine learning models.

## Base URL
```
http://127.0.0.1:5000/
```

## Endpoints

### 1. `/predict` - Predict Shortest Path Length

**Description**: Predicts the shortest path length between two nodes in a graph using a pre-trained machine learning model.

- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "source": "source_node_id",
    "target": "target_node_id",
    "graph_file": "path_to_graph_file"  // Optional
  }
  ```
- **Response**:
  - `200 OK`
    ```json
    {
      "predicted_length": 42
    }
    ```
  - `400 Bad Request`: If input data types are incorrect or if the graph file is not found.
  - `500 Internal Server Error`: If an unexpected error occurs.

### 2. `/dijkstra` - Compute Shortest Path Using Dijkstra's Algorithm

**Description**: Computes the shortest path between two nodes in a graph using Dijkstra's algorithm.

- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "source": "source_node_id",
    "target": "target_node_id",
    "graph_file": "path_to_graph_file"  // Optional
  }
  ```
- **Response**:
  - `200 OK`
    ```json
    {
      "path": ["node1", "node2", "node3"],
      "length": 42
    }
    ```
  - `400 Bad Request`: If the graph file is not found.
  - `500 Internal Server Error`: If an unexpected error occurs.

### 3. `/adapt` - Adapt Model to New Graph

**Description**: Adapts a pre-trained machine learning model to a new graph.

- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "graph_file": "path_to_graph_file"
  }
  ```
- **Response**:
  - `200 OK`
    ```json
    {
      "status": "Model adapted and saved."
    }
    ```
  - `400 Bad Request`: If the graph file is not found or if adaptation fails.
  - `500 Internal Server Error`: If an unexpected error occurs.

### 4. `/evaluate` - Evaluate Adapted Model

**Description**: Evaluates the accuracy of the adapted machine learning model on a new task.

- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "source": "source_node_id",
    "target": "target_node_id",
    "graph_file": "path_to_graph_file"
  }
  ```
- **Response**:
  - `200 OK`
    ```json
    {
      "accuracy": 0.95
    }
    ```
  - `400 Bad Request`: If the graph file or adapted model is not found.
  - `500 Internal Server Error`: If an unexpected error occurs.

## Error Handling

- **400 Bad Request**: This status code is returned when there is an issue with the request, such as missing or incorrect data.
- **500 Internal Server Error**: This status code is returned when an unexpected error occurs on the server.

## Example Usage with cURL

### Predict Shortest Path Length
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"source": "1", "target": "10", "graph_file": "data/processed/social_networks/facebook_graph.edgelist"}'
```

### Compute Shortest Path Using Dijkstra's Algorithm
```bash
curl -X POST http://127.0.0.1:5000/dijkstra -H "Content-Type: application/json" -d '{"source": "1", "target": "10"}'
```

### Adapt Model to New Graph
```bash
curl -X POST http://127.0.0.1:5000/adapt -H "Content-Type: application/json" -d '{"graph_file": "data/processed/social_networks/new_graph.edgelist"}'
```

### Evaluate Adapted Model
```bash
curl -X POST http://127.0.0.1:5000/evaluate -H "Content-Type: application/json" -d '{"source": "1", "target": "10", "graph_file": "data/processed/social_networks/new_graph.edgelist"}'
```

For further questions or issues, please refer to the project documentation or open an issue in the repository.
