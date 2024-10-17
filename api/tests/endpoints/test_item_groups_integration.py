import pytest
import requests


@pytest.fixture
def api_setup():
    base_url = 'http://localhost:3000/api/v1/item_lines'
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
        'API_KEY': 'a1b2c3d4e5',
        'Content-Type': 'application/json'
    }
    return base_url, headers


def test_get_item_group_by_id(api_setup):
    base_url, headers = api_setup

    # Define the item group ID to retrieve
    item_group_id = 1

    # Send the GET request to retrieve the item group by ID
    response = requests.get(
        f'{base_url}/{item_group_id}', headers=headers)

    # Assert the response status code (200 for successful retrieval)
    assert response.status_code == 200
    if response.status_code == 200:
        print(
            "The requested ID has been successfully retrieved.")
    else:
        print("The requested ID has not been retrieved.")


def test_compare_item_group_with_data(api_setup):
    base_url, headers = api_setup
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
        f'{base_url}/{item_group_id}', headers=headers)

    response_data = response.json

    # Assert the response status code (200 for successful retrieval)
    assert response.status_code == 200
    # Compare response with existing data
    assert response_data == data

    if response.status_code == 200:
        print(
            "The requested ID has been successfully retrieved.")
    else:
        print("The requested ID has not been retrieved.")


def test_put_item_group(api_setup):
    base_url, headers = api_setup

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
        f'{base_url}/{item_group_id}', headers=headers, json=data)

    # Assert the response status code
    assert response.status_code == 200
    if response.status_code == 200:
        print("The requested ID has been successfully updated.")
    else:
        print("The requested ID has not been updated.")


def test_delete_item_group(api_setup):
    base_url, headers = api_setup

    # Define the item group ID to delete
    item_group_id = 100

    # Send the DELETE request to delete the item group by ID
    response = requests.delete(
        f'{base_url}/{item_group_id}', headers=headers)

    # Assert the response status code
    assert response.status_code == 200
    if response.status_code == 200:
        print("The requested ID has been successfully deleted.")
    else:
        print("The requested ID has not been deleted.")
