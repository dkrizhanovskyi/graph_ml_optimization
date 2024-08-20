from skopt import BayesSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import networkx as nx
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

def optimize_hyperparameters(G):
    """
    Optimize hyperparameters for the Random Forest Regressor using Bayesian optimization.
    """
    data, labels = generate_training_data(G)
    
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(random_state=42)
    
    # Define the hyperparameter search space
    param_space = {
        'n_estimators': (50, 500),
        'max_depth': (5, 50),
        'min_samples_split': (2, 10),
        'min_samples_leaf': (1, 4),
    }
    
    # Set up Bayesian search
    bayes_cv = BayesSearchCV(
        estimator=model,
        search_spaces=param_space,
        n_iter=32,
        cv=3,
        n_jobs=-1,
        random_state=42
    )
    
    # Perform hyperparameter optimization
    bayes_cv.fit(X_train, y_train)
    
    # Evaluate the optimized model
    best_model = bayes_cv.best_estimator_
    predictions = best_model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    logging.info(f"Best parameters found: {bayes_cv.best_params_}")
    logging.info(f"Best cross-validation score: {bayes_cv.best_score_}")
    logging.info(f"Test MSE with optimized model: {mse}")
    
    # Save the optimized model
    joblib.dump(best_model, "src/models/compressed_shortest_path_model.pkl")
    logging.info("Optimized model saved to src/models/compressed_shortest_path_model.pkl")

if __name__ == "__main__":
    G = nx.gnm_random_graph(100, 200)
    optimize_hyperparameters(G)
