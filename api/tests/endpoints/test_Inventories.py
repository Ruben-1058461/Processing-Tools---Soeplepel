import pytest
import requests


@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/'


def test_create_inventory(_url):
    
    inventory_id = 123456789123456789  # ID
    url = _url + f'inventories/{inventory_id}'

    headers = {
        'API_KEY': 'a1b2c3d4e5',
        'Content-Type': 'application/json'
    }

    data = {
    "id": 123456789123456789,
    "item_id": "P000001",
    "description": "testing",
    "item_reference": "testing",
    "locations": [
        3211,
        24700,
        14123,
        19538,
        31071,
        24701,
        11606,
        11817
    ],
    "total_on_hand": "testing",
    "total_expected": "testing",
    "total_ordered": "testing",
    "total_allocated": "testing",
    "total_available": "testing",
    "created_at": "testing",
    "updated_at": "testing"
}


    # Send a POST request to the API
    response = requests.post(url, headers=headers, json=data)

    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")
    print(f"Request URL: {response.url}")

    status_code = response.status_code
    assert status_code == 201


def test_get_inventory(_url):
    inventory_id = 123456789123456789  # ID
    url = _url + f'inventories/{inventory_id}'  # Inventories endpoint

    headers = {
        'API_KEY': 'a1b2c3d4e5',
        'Content-Type': 'application/json'
    }

    # Send a GET request to the API
    response = requests.get(url, headers=headers)

    # Get the status code and response data
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")
    print(f"Request URL: {response.url}")
    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_update_inventory(_url):
    inventory_id = 123456789123456789  # ID
    url = _url + f'inventories/{inventory_id}'  # Inventories endpoint

    headers = {
        'API_KEY': 'a1b2c3d4e5',
        'Content-Type': 'application/json'
    }

    data = {
    "id": 123456789123456789,
    "item_id": "P000001",
    "description": "testing updated",
    "item_reference": "testing updated",
    "locations": [
        3211,
        24700,
        14123,
        19538,
        31071,
        24701,
        11606,
        11817
    ],
    "total_on_hand": "testing updated",
    "total_expected": "testing updated",
    "total_ordered": "testing updated",
    "total_allocated": "testing updated",
    "total_available": "testing updated",
    "created_at": "testing updated",
    "updated_at": "testing updated"
}

    response = requests.put(url, json=data, headers=headers)
    # Check the response
    if response.status_code == 200:
        print("PUT request successful")
    else:
        print(f"Failed to update inventory. Status code: {response.status_code}")


def test_delete_inventory(_url):
    inventory_id = 123456789123456789  # ID
    url = _url + f'inventories/{inventory_id}'  # Inventories endpoint

    headers = {
        'API_KEY': 'a1b2c3d4e5',
        'Content-Type': 'application/json'
    }

    response = requests.delete(url, headers=headers)

    # Check the response
    if response.status_code == 204:
        print("DELETE request successful")
    else:
        print(f"Failed to delete inventory. Status code: {response.status_code}")


def test_Check_item_inventory(_url):
    inventory_id = 123456789123456789  # ID
    url = _url + f'inventories/{inventory_id}'  # Inventories endpoint

    headers = {
        'API_KEY': 'a1b2c3d4e5',
        'Content-Type': 'application/json'
    }

    # Send a GET request to the API
    response = requests.get(url, headers=headers)

    # Get the status code and response data
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")
    print(f"Request URL: {response.url}")
    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200