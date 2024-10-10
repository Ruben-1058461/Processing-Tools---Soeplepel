import unittest
import requests

class TestItemGroupAPI(unittest.TestCase):
    def setUp(self):
        # Base URL for your backend API
        self.base_url = f'http://localhost:3000/api/v1/item_groups'
        # Headers for the url to accept
        self.headers = {
            'Accept':'*/*',
            'User-Agent':'Thunder Client (https://www.thunderclient.com)',
            'API_KEY': 'a1b2c3d4e5',
            'Content-Type': 'application/json'
        }
    
    def test_get_item_group_by_id(self):
        # Define the item group ID to retrieve
        item_group_id = 100 # input("Choose an ID ")
        
        # Send the GET request to retrieve the item group by ID
        response = requests.get(f'{self.base_url}/{item_group_id}', headers=self.headers)

        # Assert the response status code (200 for successful retrieval)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        if response.status_code == 200:
            print(f"The requested ID has been succesfully retrieved. {response_data}")

    def test_put_item_group(self):
        # Define the POST request data
        data = {
            "id": 100,
            "name": "Testing",
            "description": "Testing unittest",
            "created_at": "2016-05-25 10:50:09",
            "updated_at": "2024-08-06 06:39:30"
        }

        # Define the item group ID to update
        item_group_id = 100  # input("Choose an ID ")

        # Send the PUT request to retrieve the item group by ID
        response = requests.put(f'{self.base_url}/{item_group_id}', headers=self.headers, json=data)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print(f"The requested ID has been succesfully updated. {data}")

    def test_delete_item_group(self):

        # Define the item group ID to update
        item_group_id = 100  # input("Choose an ID ")

        # Send the PUT request to retrieve the item group by ID
        response = requests.delete(f'{self.base_url}/{item_group_id}', headers=self.headers)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print("The requested ID has been succesfully deleted.")

        
if __name__ == '__main__':
    unittest.main()
