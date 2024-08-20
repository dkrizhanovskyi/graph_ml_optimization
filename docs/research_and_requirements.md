# Research and Requirements for Graph ML Optimization Project

This document outlines the research and requirements for the development of machine learning algorithms to solve graph optimization problems.

## 1. Research Overview

### Classical Graph Optimization Algorithms
- **Dijkstra's Algorithm**: A well-known algorithm for finding the shortest path between nodes in a graph, which works on graphs with non-negative weights.
- **Bellman-Ford Algorithm**: Computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph, capable of handling negative weights.
- **Floyd-Warshall Algorithm**: Finds shortest paths in a weighted graph with positive or negative edge weights, but without negative cycles.

### Machine Learning Techniques
- **Supervised Learning**: Using labeled graph data to train models that can predict certain graph properties or optimization results.
- **Reinforcement Learning**: Exploring how reinforcement learning can be applied to solve graph optimization problems by learning policies that improve graph traversal efficiency.
- **Graph Neural Networks (GNNs)**: Investigating GNNs to leverage the structural properties of graphs for better model performance in optimization tasks.

## 2. Requirements

### Functional Requirements
- **Graph Representation**: The system should support various graph representations, including edge lists and adjacency matrices.
- **Algorithm Implementation**: Implement classical graph algorithms as a baseline for comparison with ML models.
- **Model Training**: Train machine learning models on generated and real-world graph datasets.
- **Model Adaptation**: Adapt trained models to work with new, unseen graphs.
- **API Development**: Provide a RESTful API to expose the functionality of the graph optimization models and algorithms.

### Non-Functional Requirements
- **Performance**: The system should be optimized to handle large graphs efficiently.
- **Scalability**: The solution should be scalable to accommodate increasing graph sizes and complexity.
- **Extensibility**: The system should be designed with extensibility in mind, allowing for easy integration of new algorithms and models.

## 3. Datasets

### Generated Datasets
- Random graphs with varying node and edge counts to simulate different levels of complexity.

### Real-World Datasets
- **Biological Networks**: Protein-protein interaction networks.
- **Social Networks**: Graphs representing social connections between individuals.
- **Transportation Networks**: Urban road networks for navigation and routing tasks.

## 4. Performance Metrics

- **Accuracy**: Measure the accuracy of ML models in predicting the shortest path length compared to classical algorithms.
- **Execution Time**: Evaluate the time taken by each algorithm and model to complete optimization tasks.
- **Memory Usage**: Assess the memory footprint of different models and algorithms, especially when dealing with large graphs.

## 5. Future Research Directions
- **Exploration of GNNs**: Further research into using GNNs for more complex graph-related tasks.
- **Hybrid Models**: Combining classical algorithms with machine learning approaches to create hybrid models that leverage the strengths of both.
- **Optimization on Dynamic Graphs**: Investigate techniques for optimizing graphs that change over time, such as in real-time traffic networks.

This document will be updated as the project progresses and as new research findings emerge.
