# Data Preparation Process

## Overview
This document describes the data preparation process for the Graph ML Optimization Project. The preparation includes generating random graphs, converting graph data into suitable formats, augmenting data to improve model generalization, and gathering real-world graph datasets.

## Steps

### 1. Generating Random Graphs
- **Script**: `generate_graphs.py`
- **Description**: This script generates random undirected and directed graphs, as well as weighted graphs with both positive and negative weights.
- **Usage**: The script generates graphs of varying complexity for training and testing machine learning models.

### 2. Converting Graph Data into Suitable Formats
- **Script**: `preprocess_social_networks.py`, `preprocess_transportation_networks.py`, `preprocess_biological_networks.py`
- **Description**: These scripts load raw graph data, preprocess it, and save it in formats suitable for machine learning (e.g., edge lists, adjacency matrices).

### 3. Data Augmentation
- **Script**: `augment_data.py`
- **Description**: The augmentation process involves adding noise to graphs by randomly modifying edges. This improves the generalization capability of machine learning models.
- **Example Augmentation**: 
  - Noise level: 2%
  - Augmentation applied to: Facebook Social Network graph
  - Output: `facebook_graph_augmented.gml`

### 4. Gathering Real-World Graph Datasets
- **Sources**: 
  - **Social Networks**: Facebook Social Circles
  - **Transportation Networks**: OpenStreetMap
  - **Biological Networks**: STRING Database
- **Scripts**: Various preprocessing scripts to clean and format the datasets.

## Tools Used
- **NetworkX**: For graph generation, manipulation, and analysis.
- **OSMnx**: For downloading and processing transportation networks from OpenStreetMap.
- **Pandas**: For handling tabular data during preprocessing.
- **Matplotlib**: For visualizing graphs.

## Notes
- All steps in the data preparation process are fully automated through the provided scripts.
- Ensure that all dependencies are installed before running the scripts.
