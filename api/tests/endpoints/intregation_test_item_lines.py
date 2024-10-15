import unittest
import requests


class TestItemLineAPI(unittest.TestCase):
    def setUp(self):
        # Base URL for your backend API
        self.base_url = f'http://localhost:3000/api/v1/item_lines'
        # Headers for the url to accept
        self.headers = {
            'Accept': '*/*',
            'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
            'API_KEY': 'a1b2c3d4e5',
            'Content-Type': 'application/json'
        }

    def test_get_item_lines_by_id(self):
        # Define the item line ID to retrieve
        item_line_id = 1

        # Send the GET request to retrieve the item line by ID
        response = requests.get(
            f'{self.base_url}/{item_line_id}', headers=self.headers)

        # Assert the response status code (200 for successful retrieval)
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print(
                "The requested ID has been successfully retrieved.")
        else:
            print("The requested ID has not been retrieved.")

    def test_compare_item_lines_with_data(self):
        # Define the item line ID to retrieve
        item_line_id = 1  # input("Choose an ID ")

        data = {
        "id": 1,
        "name": "Home Appliances",
        "description": "",
        "created_at": "1979-01-16 07:07:50",
        "updated_at": "2024-01-05 23:53:25"
        }

        # Send the GET request to retrieve the item line by ID
        response = requests.get(
            f'{self.base_url}/{item_line_id}', headers=self.headers)
        
        response_data = response.json

        # Assert the response status code (200 for successful retrieval)
        self.assertEqual(response.status_code, 200)
        # compare response with existing data
        self.assertEqual(response_data, data)
        if response.status_code == 200:
            print(
                "The requested ID has been successfully retrieved.")
        else:
            print("The requested ID has not been retrieved.")

    def test_put_item_line(self):
        # Define the POST request data
        data = {
            "id": 97,
            "name": "Testing item_lines",
            "description": "integration test",
            "created_at": "2007-12-31 10:48:06",
            "updated_at": "2023-08-22 06:43:47"
        }

        # Define the item line ID to update
        item_line_id = 97  # input("Choose an ID ")

        # Send the PUT request to retrieve the item line by ID
        response = requests.put(
            f'{self.base_url}/{item_line_id}', headers=self.headers, json=data)

        # Assert the response status code (200 or 201 depending on your API)
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print("The requested ID has been successfully updated.")
        else:
            print("The requested ID has not been updated.")

    def test_delete_item_line(self):

        # Define the item line ID to update
        item_line_id = 97  # input("Choose an ID ")

        # Send the PUT request to retrieve the item line by ID
        response = requests.delete(
            f'{self.base_url}/{item_line_id}', headers=self.headers)

        # Assert the response status code (200 or 201 depending on your API)
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print("The requested ID has been successfully deleted.")
        else:
            print("The requested ID has not been deleted.")


# Create a test suite to control the order of test execution
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestItemLineAPI('test_get_item_lines_by_id'))
    suite.addTest(TestItemLineAPI('test_put_item_lines'))
    suite.addTest(TestItemLineAPI('test_delete_item_lines'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
