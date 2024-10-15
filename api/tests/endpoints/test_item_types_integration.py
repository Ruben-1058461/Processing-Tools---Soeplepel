import pytest
import requests
from test_setup import api_setup

api_setup()

def test_get_item_types_by_id(self):
    base_url, headers = api_setup

    # Define the item types ID to retrieve
    item_type_id = 100  # input("Choose an ID ")

    # Send the GET request to retrieve the item Type by ID
    response = requests.get(
        f'{base_url}/{item_type_id}', headers=headers)

    # Assert the response status code (200 for successful retrieval)
    assert response.status_code == 200
    if response.status_code == 200:
        print(
            "The requested ID has been successfully retrieved.")
    else:
        print("The requested ID has not been retrieved.")

def test_compare_item_types_with_data(api_setup):
    base_url, headers = api_setup
        
    # Define the item types ID to retrieve
    item_type_id = 1 

    data = {
        "id": 1,
        "name": "Desktop",
        "description": "",
        "created_at": "1993-07-28 13:43:32",
        "updated_at": "2022-05-12 08:54:35"
        }

        # Send the GET request to retrieve the item Type by ID
    response = requests.get(
        f'{base_url}/{item_type_id}', headers=headers)
    response_data = response.json

    # Assert the response status code (200 for successful retrieval)
    assert response.status_code == 200
    # Compare response with data
    assert response_data == data
    if response.status_code == 200:
        print(
                "The requested ID has been successfully retrieved.")
    else:
        print("The requested ID has not been retrieved.")

def test_put_item_types(api_setup):
    base_url, headers = api_setup
    # Define the POST request data
    data = {
            "id": 100,
            "name": "Testing item_types",
            "description": "integration test",
            "created_at": "2007-12-31 10:48:06",
            "updated_at": "2023-08-22 06:43:47"
        }

    # Define the item type ID to update
    item_type_id = 100  # input("Choose an ID ")

    # Send the PUT request to retrieve the item type by ID
    response = requests.put(
            f'{base_url}/{item_type_id}', headers=headers, json=data)

        # Assert the response status code
    assert response.status_code == 200
    if response.status_code == 200:
        print("The requested ID has been successfully updated.")
    else:
        print("The requested ID has not been updated.")

def test_delete_item_types(api_setup):
    base_url, headers = api_setup

    # Define the item type ID to update
    item_type_id = 100  # input("Choose an ID ")

    # Send the PUT request to retrieve the item type by ID
    response = requests.delete(
            f'{base_url}/{item_type_id}', headers=headers)

    # Assert the response status code
    assert response.status_code == 200
    if response.status_code == 200:
        print("The requested ID has been successfully deleted.")
    else:
        print("The requested ID has not been deleted.")
