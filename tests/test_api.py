import unittest
import json
from src.api import app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Flask test client for use in test cases
        self.app = app.test_client()
        self.app.testing = True

    def test_predict(self):
        # Test the /predict endpoint for a valid case
        response = self.app.post('/predict', 
                                 data=json.dumps({
                                     'source': '1',
                                     'target': '10',
                                     'graph_file': 'data/processed/social_networks/facebook_graph.edgelist'
                                 }),
                                 content_type='application/json')
        
        # Parse the response data and assert that the prediction is present and is an integer
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('predicted_length', data)
        self.assertIsInstance(data['predicted_length'], int)

    def test_dijkstra(self):
        # Test the /dijkstra endpoint for a valid case
        response = self.app.post('/dijkstra', 
                                 data=json.dumps({
                                     'source': '1',
                                     'target': '10',
                                     'graph_file': 'data/processed/social_networks/facebook_graph.edgelist'
                                 }),
                                 content_type='application/json')
        
        # Parse the response data and assert that the path and length are present and correctly typed
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('length', data)
        self.assertIsInstance(data['length'], int)
        self.assertIn('path', data)
        self.assertIsInstance(data['path'], list)

    def test_adapt(self):
        # Test the /adapt endpoint for a case where the graph adaptation is attempted
        response = self.app.post('/adapt', 
                                 data=json.dumps({
                                     'graph_file': 'data/processed/transportation_networks/manhattan_graph.graphml'
                                 }),
                                 content_type='application/json')
        
        # Parse the response data and check for successful adaptation or a failure due to no valid path
        data = json.loads(response.get_data(as_text=True))
        
        if 'Adaptation failed' in data['status']:
            self.assertEqual(data['status'], 'Adaptation failed due to no valid path in the graph.')
        else:
            self.assertEqual(data['status'], 'Model adapted and saved.')

    def test_evaluate(self):
        # Test the /evaluate endpoint for evaluating the adapted model on a new task
        response = self.app.post('/evaluate', 
                                 data=json.dumps({
                                     'source': '42421728',
                                     'target': '42421775',
                                     'graph_file': 'data/processed/transportation_networks/manhattan_graph.graphml'
                                 }),
                                 content_type='application/json')
        
        # Parse the response data and handle both the presence and absence of the adapted model
        data = json.loads(response.get_data(as_text=True))
        
        if 'error' in data:
            self.assertEqual(data['error'], 'Adapted model not found. Please adapt the model first.')
        else:
            self.assertIn('accuracy', data)
            self.assertIsInstance(data['accuracy'], float)

    # Additional Test: Handling invalid data
    def test_invalid_data(self):
        # Test the /predict endpoint with invalid input data (wrong data types)
        response = self.app.post('/predict',
                                 data=json.dumps({
                                     'source': 1,  # Should be a string
                                     'target': '10',
                                     'graph_file': 'data/processed/social_networks/facebook_graph.edgelist'
                                 }),
                                 content_type='application/json')
        
        # Assert that the response status code is 400 indicating a bad request
        self.assertEqual(response.status_code, 400)
    
    # Additional Test: Handling an empty graph
    def test_empty_graph(self):
        # Test the /predict endpoint with an empty graph
        response = self.app.post('/predict',
                                 data=json.dumps({
                                     'source': '1',
                                     'target': '10',
                                     'graph_file': 'data/processed/social_networks/empty_graph.edgelist'
                                 }),
                                 content_type='application/json')
        
        # Assert that the response status code is 400 indicating a bad request
        self.assertEqual(response.status_code, 400)
    
    # Additional Test: Handling a sparse graph
    def test_sparse_graph(self):
        # Test the /predict endpoint with a sparse graph
        response = self.app.post('/predict',
                                 data=json.dumps({
                                     'source': '1',
                                     'target': '10',
                                     'graph_file': 'data/processed/social_networks/sparse_graph.edgelist'
                                 }),
                                 content_type='application/json')
        
        # Parse the response data and assert that the prediction is present and is an integer
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('predicted_length', data)
        self.assertIsInstance(data['predicted_length'], int)

    # Additional Test: Handling a graph with self-loops
    def test_graph_with_self_loops(self):
        # Test the /predict endpoint with a graph containing self-loops
        response = self.app.post('/predict',
                                 data=json.dumps({
                                     'source': '1',
                                     'target': '1',  # Self-loop case
                                     'graph_file': 'data/processed/social_networks/self_loop_graph.edgelist'
                                 }),
                                 content_type='application/json')
        
        # Parse the response data and assert that the prediction correctly handles self-loops (should be 0)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('predicted_length', data)
        self.assertEqual(data['predicted_length'], 0)  # Path length should be 0 due to self-loop

    # Additional Test: Handling a large graph
    def test_large_graph(self):
        # Test the /predict endpoint with a large graph
        response = self.app.post('/predict',
                                 data=json.dumps({
                                     'source': '1',
                                     'target': '10000',  # Assuming the graph is large
                                     'graph_file': 'data/processed/social_networks/large_graph.edgelist'
                                 }),
                                 content_type='application/json')
        
        # Parse the response data and assert that the prediction is present and is an integer
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('predicted_length', data)
        self.assertIsInstance(data['predicted_length'], int)

if __name__ == '__main__':
    unittest.main()
