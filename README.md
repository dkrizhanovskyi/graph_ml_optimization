# Graph ML Optimization Project

This project focuses on the research and development of machine learning algorithms to solve optimization problems in graph theory. The main goal is to create a set of ML models capable of solving complex graph optimization tasks with high accuracy and efficiency.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Training a Model](#training-a-model)
  - [Optimizing Hyperparameters](#optimizing-hyperparameters)
  - [Adapting a Model](#adapting-a-model)
  - [Comparing Algorithms](#comparing-algorithms)
  - [Running the API](#running-the-api)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview
The project is designed to:
- Implement classical graph optimization algorithms.
- Explore and develop machine learning models to solve graph optimization problems.
- Compare traditional algorithms with ML-based solutions.
- Provide an API to interact with the models and algorithms.

## Installation
To get started with this project, clone the repository and install the required dependencies.

```bash
git clone https://github.com/dkrizhanovskyi/graph_ml_optimization.git
cd graph_ml_optimization
pip install -r requirements.txt
```

## Usage

### Training a Model
To train a machine learning model on a generated graph:

```bash
python src/models/train_shortest_path_model.py
```

### Optimizing Hyperparameters
To optimize hyperparameters using Bayesian optimization:

```bash
python src/models/optimize_hyperparameters.py
```

### Adapting a Model
To adapt a pre-trained model to a new graph:

```bash
python src/models/adapt_models_for_new_graphs.py
```

### Comparing Algorithms
To compare different shortest path algorithms:

```bash
python src/comparison/compare_algorithms.py
```

### Running the API
To run the Flask API for model predictions and comparisons:

```bash
python src/api.py
```

The API will be available at `http://127.0.0.1:5000/`.

## Project Structure

```
graph_ml_optimization/
│
├── data/                    # Raw and processed data
├── docs/                    # Documentation
├── src/                     # Source code for the project
│   ├── algorithms/          # Classical graph algorithms
│   ├── comparison/          # Scripts for comparing algorithms
│   ├── data_preprocessing/  # Data preprocessing scripts
│   ├── models/              # Machine learning models and related scripts
│   └── api.py               # Flask API implementation
├── tests/                   # Unit and integration tests
├── requirements.txt         # Python dependencies
└── README.md                # Project overview
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
