import pytest
import requests


@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/'


def test_create_order(_url):
    order_id = 123456789123456789  # ID
    url = _url + f'orders/{order_id}'

    headers = {
        'API_KEY': 'a1b2c3d4e5',  
        'Content-Type': 'application/json'
    }

    data = {
    "id": 123456789123456789,
    "source_id": "testing",
    "order_date": "testing",
    "request_date": "testing",
    "reference": "testing",
    "reference_extra": "testing",
    "order_status": "testing",
    "notes": "testing",
    "shipping_notes": "testing",
    "picking_notes": "testing",
    "warehouse_id": "testing",
    "ship_to": "testing",
    "bill_to": "testing",
    "shipment_id": "testing",
    "total_amount": "testing",
    "total_discount": "testing",
    "total_tax": "testing",
    "total_surcharge": "testing",
    "created_at": "testing",
    "updated_at": "testing",
    "items": [
        {"item_id": "P007435", "amount": 23},
        {"item_id": "P009557", "amount": 1},
        {"item_id": "P009553", "amount": 50},
        {"item_id": "P010015", "amount": 16},
        {"item_id": "P002084", "amount": 33},
        {"item_id": "P009663", "amount": 18},
        {"item_id": "P010125", "amount": 18},
        {"item_id": "P005768", "amount": 26},
        {"item_id": "P004051", "amount": 1},
        {"item_id": "P005026", "amount": 29},
        {"item_id": "P000726", "amount": 22},
        {"item_id": "P008107", "amount": 47},
        {"item_id": "P001598", "amount": 32},
        {"item_id": "P002855", "amount": 20},
        {"item_id": "P010404", "amount": 30},
        {"item_id": "P010446", "amount": 6},
        {"item_id": "P001517", "amount": 9},
        {"item_id": "P009265", "amount": 2},
        {"item_id": "P001108", "amount": 20},
        {"item_id": "P009110", "amount": 18},
        {"item_id": "P009686", "amount": 13}
    ]
}

    # Send a POST request to the API
    response = requests.post(url, headers=headers, json=data)

    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")
    print(f"Request URL: {response.url}")

    status_code = response.status_code
    assert status_code == 201


def test_get_order(_url):
    order_id = 123456789123456789  # ID
    url = _url + f'orders/{order_id}'  # Orders endpoint

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


def test_update_order(_url):
    order_id = 123456789123456789  # ID
    url = _url + f'orders/{order_id}'  # Orders endpoint

    headers = {
        'API_KEY': 'a1b2c3d4e5',  
        'Content-Type': 'application/json'
    }

    data = {
    "id": 123456789123456789,
    "source_id": "testing updated",
    "order_date": "testing updated",
    "request_date": "testing updated",
    "reference": "testing updated",
    "reference_extra": "testing updated",
    "order_status": "testing updated",
    "notes": "testing updated",
    "shipping_notes": "testing updated",
    "picking_notes": "testing updated",
    "warehouse_id": "testing updated",
    "ship_to": "testing updated",
    "bill_to": "testing updated",
    "shipment_id": "testing updated",
    "total_amount": "testing updated",
    "total_discount": "testing updated",
    "total_tax": "testing updated",
    "total_surcharge": "testing updated",
    "created_at": "testing updated",
    "updated_at": "testing updated",
    "items": [
        {"item_id": "P007435", "amount": 23},
        {"item_id": "P009557", "amount": 1},
        {"item_id": "P009553", "amount": 50},
        {"item_id": "P010015", "amount": 16},
        {"item_id": "P002084", "amount": 33},
        {"item_id": "P009663", "amount": 18},
        {"item_id": "P010125", "amount": 18},
        {"item_id": "P005768", "amount": 26},
        {"item_id": "P004051", "amount": 1},
        {"item_id": "P005026", "amount": 29},
        {"item_id": "P000726", "amount": 22},
        {"item_id": "P008107", "amount": 47},
        {"item_id": "P001598", "amount": 32},
        {"item_id": "P002855", "amount": 20},
        {"item_id": "P010404", "amount": 30},
        {"item_id": "P010446", "amount": 6},
        {"item_id": "P001517", "amount": 9},
        {"item_id": "P009265", "amount": 2},
        {"item_id": "P001108", "amount": 20},
        {"item_id": "P009110", "amount": 18},
        {"item_id": "P009686", "amount": 13}
    ]
}


    response = requests.put(url, json=data, headers=headers)
    # Check the response
    if response.status_code == 200:
        print("PUT request successful")
    else:
        print(f"Failed to update order. Status code: {response.status_code}")


def test_delete_order(_url):
    order_id = 123456789123456789  # ID
    url = _url + f'orders/{order_id}'  # Orders endpoint

    headers = {
        'API_KEY': 'a1b2c3d4e5',  
        'Content-Type': 'application/json'
    }

    response = requests.delete(url, headers=headers)

    # Check the response
    if response.status_code == 204:
        print("DELETE request successful")
    else:
        print(f"Failed to delete order. Status code: {response.status_code}")


def test_View_item_order(_url):
    order_id = 123456789123456789  # ID
    url = _url + f'orders/{order_id}'  # Orders endpoint

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