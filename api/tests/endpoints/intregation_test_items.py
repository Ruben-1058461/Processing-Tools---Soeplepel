import unittest
import requests

class TestItemsAPI(unittest.TestCase):
    def setUp(self):
        # Base URL for your backend API
        self.base_url = f'http://localhost:3000/api/v1/items'
        # Headers for the url to accept
        self.headers = {
            'Accept':'*/*',
            'User-Agent':'Thunder Client (https://www.thunderclient.com)',
            'API_KEY': 'a1b2c3d4e5',
            'Content-Type': 'application/json'
        }
    
    def test_get_item_item_by_id(self):
        # Define the item item ID to retrieve
        item_id = 'P000001' # input("Choose an ID ")
        
        # Send the GET request to retrieve the item item by ID
        response = requests.get(f'{self.base_url}/{item_id}', headers=self.headers)

        # Assert the response status code (200 for successful retrieval)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        if response.status_code == 200:
            print(f"The requested ID has been succesfully retrieved. {response_data}")

    def test_post_item_item(self):
        # Define the POST request data
        data =     {
        "uid": "P011721",
        "code": "Testing123",
        "description": "Testing items",
        "short_description": "pass",
        "upc_code": "2541112620796",
        "model_number": "ZK-417773-PXy",
        "commodity_code": "z-761-L5A",
        "item_line": 100,
        "item_group": 100,
        "item_type": 100,
        "unit_purchase_quantity": 100,
        "unit_order_quantity": 100,
        "pack_order_quantity": 100,
        "supplier_id": 100,
        "supplier_code": "TEST468",
        "supplier_part_number": "TESTING-ZH-103509-MLv",
        "created_at": "1997-05-13 02:30:31",
        "updated_at": "2003-10-18 00:21:57"
    }

        # Define the item item ID to update
        item_id = 'P011721'  # input("Choose an ID ")

        # Send the PUT request to retrieve the item item by ID
        response = requests.post(f'{self.base_url}/{item_id}', headers=self.headers, json=data)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print(f"The requested ID has been succesfully posted.")

    def test_put_item_item(self):
        # Define the PUT request data
        data =     {
        "uid": "P011721",
        "code": "Testing",
        "description": "Testing",
        "short_description": "pass",
        "upc_code": "2541112620796",
        "model_number": "ZK-417773-PXy",
        "commodity_code": "z-761-L5A",
        "item_line": 100,
        "item_group": 100,
        "item_type": 100,
        "unit_purchase_quantity": 100,
        "unit_order_quantity": 100,
        "pack_order_quantity": 100,
        "supplier_id": 100,
        "supplier_code": "TEST468",
        "supplier_part_number": "TESTING-ZH-103509-MLv",
        "created_at": "1997-05-13 02:30:31",
        "updated_at": "2003-10-18 00:21:57"
    }

        # Define the item item ID to update
        item_id = 'P011721'  # input("Choose an ID ")

        # Send the PUT request to retrieve the item item by ID
        response = requests.put(f'{self.base_url}/{item_id}', headers=self.headers, json=data)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        if response.status_code == 201:
            print(f"The requested ID has been succesfully updated. {data}")

    def test_delete_items(self):

        # Define the item ID to update
        item_id = 'P011721'  # input("Choose an ID ")

        # Send the PUT request to retrieve the item item by ID
        response = requests.delete(f'{self.base_url}/{item_id}', headers=self.headers)

        # Assert the response status code (200 or 201 depending on your API)
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print("The requested ID has been succesfully deleted.")


        
if __name__ == '__main__':
    unittest.main()
