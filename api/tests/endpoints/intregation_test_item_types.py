import unittest
import requests

class TestItemTypesAPI(unittest.TestCase):
    def setUp(self):
        # Base URL for your backend API
        self.base_url = f'http://localhost:3000/api/v1/item_types'
        # Headers for the url to accept
        self.headers = {
            'Accept':'*/*',
            'User-Agent':'Thunder Client (https://www.thunderclient.com)',
            'API_KEY': 'a1b2c3d4e5',
            'Content-Type': 'application/json'
        }
    
    def test_get_item_types_by_id(self):
        # Define the item types ID to retrieve
        item_type_id = 100 # input("Choose an ID ")
        
        # Send the GET request to retrieve the item Type by ID
        response = requests.get(f'{self.base_url}/{item_type_id}', headers=self.headers)

        # Assert the response status code (200 for successful retrieval)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        if response.status_code == 200:
            print(f"The requested ID has been succesfully retrieved. {response_data}")

    
if __name__ == '__main__':
    unittest.main()
