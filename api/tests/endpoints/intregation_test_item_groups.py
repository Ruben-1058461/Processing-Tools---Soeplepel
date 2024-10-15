import unittest
import requests


class TestItemGroupAPI(unittest.TestCase):
    def setUp(self):
        # Base URL for your backend API
        self.base_url = f'http://localhost:3000/api/v1/item_groups'
        # Headers for the url to accept
        self.headers = {
            'Accept': '*/*',
            'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
            'API_KEY': 'a1b2c3d4e5',
            'Content-Type': 'application/json'
        }

    def test_get_item_group_by_id(self):
        # Define the item group ID to retrieve
        item_group_id = 1

        # Send the GET request to retrieve the item group by ID
        response = requests.get(
            f'{self.base_url}/{item_group_id}', headers=self.headers)

        # Assert the response status code (200 for successful retrieval)
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print(
                "The requested ID has been successfully retrieved.")
        else:
            print("The requested ID has not been retrieved.")

    def test_compare_item_group_with_data(self):
        # Define the item group ID to retrieve
        item_group_id = 1

        data = {
        "id": 1,
        "name": "Furniture",
        "description": "",
        "created_at": "2019-09-22 15:51:07",
        "updated_at": "2022-05-18 13:49:28"
        }

        # Send the GET request to retrieve the item group by ID
        response = requests.get(
            f'{self.base_url}/{item_group_id}', headers=self.headers)

        response_data = response.json

        # Assert the response status code (200 for successful retrieval)
        self.assertEqual(response.status_code, 200)
        # Compare response with existing data
        self.assertEqual(response_data, data)

        if response.status_code == 200:
            print(
                "The requested ID has been successfully retrieved.")
        else:
            print("The requested ID has not been retrieved.")

    def test_put_item_group(self):
        # Define the PUT request data
        data = {
            "id": 100,
            "name": "Testing",
            "description": "Testing unittest",
            "created_at": "2016-05-25 10:50:09",
            "updated_at": "2024-08-06 06:39:30"
        }

        # Define the item group ID to update
        item_group_id = 100

        # Send the PUT request to update the item group by ID
        response = requests.put(
            f'{self.base_url}/{item_group_id}', headers=self.headers, json=data)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print("The requested ID has been successfully updated.")
        else:
            print("The requested ID has not been updated.")

    def test_delete_item_group(self):
        # Define the item group ID to delete
        item_group_id = 100

        # Send the DELETE request to delete the item group by ID
        response = requests.delete(
            f'{self.base_url}/{item_group_id}', headers=self.headers)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print("The requested ID has been successfully deleted.")
        else:
            print("The requested ID has not been deleted.")


# Create a test suite to control the order of test execution
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestItemGroupAPI('test_get_item_group_by_id'))
    suite.addTest(TestItemGroupAPI('test_compare_item_group_with_data'))
    suite.addTest(TestItemGroupAPI('test_put_item_group'))
    suite.addTest(TestItemGroupAPI('test_delete_item_group'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
