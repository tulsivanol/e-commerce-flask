import unittest
from app import app, product_col, client
from pymongo import MongoClient
from pymongo.server_api import ServerApi

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # Set up the test client for Flask
        self.app = app.test_client()
        self.app.testing = True

    # Test 1: Route Test
    def test_home_route_invalid_method(self):
        """
        Test the / route with an invalid HTTP method (POST instead of GET).
        Ensures the route returns a 405 Method Not Allowed status code.
        """
        response = self.app.post('/')  # Sending POST request to a GET-only route
        self.assertEqual(response.status_code, 405)  # Assert 405 status code

    # Test 2: Database Read Operation
    def test_mongodb_connection(self):
        """
        Test the MongoDB connection by executing a ping command.
        Ensures the database connection is successful.
        """
        response =  client.shop_db.command('ping')  # MongoDB ping operation
        self.assertEqual(response['ok'], 1)  # Assert the connection was successful

    # Test 3: Database Write Operation
    def test_mongodb_write_operation(self):
        """
        Test a MongoDB write operation by inserting a document into the 'products' collection
        and checking if it exists in the database.
        """
        test_product = {'name': 'Test Product', 'price': 19.99, 'quantity': 10}
        # Insert the document
        result = product_col.insert_one(test_product)
        self.assertIsNotNone(result.inserted_id)  # Ensure a document ID was generated

        # Verify the document exists in the collection
        inserted_product = product_col.find_one({'_id': result.inserted_id})
        self.assertIsNotNone(inserted_product)  # Ensure the document is found
        self.assertEqual(inserted_product['name'], 'Test Product')  # Validate the document data

        # Clean up: Delete the inserted test product
        product_col.delete_one({'_id': result.inserted_id})

if __name__ == '__main__':
    unittest.main()