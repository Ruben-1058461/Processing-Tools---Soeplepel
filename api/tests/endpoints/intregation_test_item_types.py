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

    def test_put_item_types(self):
        # Define the POST request data
        data = {
            "id": 100,
            "name": "Testing item_types",
            "description": "intregation test",
            "created_at": "2007-12-31 10:48:06",
            "updated_at": "2023-08-22 06:43:47"
        }

        # Define the item type ID to update
        item_type_id = 100  # input("Choose an ID ")

        # Send the PUT request to retrieve the item type by ID
        response = requests.put(f'{self.base_url}/{item_type_id}', headers=self.headers, json=data)

        # Assert the response status code (200 or 201 depending on your API)
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print(f"The requested ID has been succesfully updated. {data}")
        
    def test_delete_item_types(self):

        # Define the item type ID to update
        item_type_id = 100  # input("Choose an ID ")

        # Send the PUT request to retrieve the item type by ID
        response = requests.delete(f'{self.base_url}/{item_type_id}', headers=self.headers)

        # Assert the response status code (200 or 201 depending on your API)
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print("The requested ID has been succesfully deleted.")

if __name__ == '__main__':
    unittest.main()
