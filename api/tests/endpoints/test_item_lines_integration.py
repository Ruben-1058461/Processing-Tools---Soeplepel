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

# Test: Get item lines by ID


def test_get_item_lines_by_id(api_setup):
    base_url, headers = api_setup
    item_line_id = 1
    response = requests.get(f'{base_url}/{item_line_id}', headers=headers)

    assert response.status_code == 200
    if response.status_code == 200:
        print("The requested ID has been successfully retrieved.")
    else:
        print("The requested ID has not been retrieved.")

# Test: Compare item lines with data


def test_compare_item_lines_with_data(api_setup):
    base_url, headers = api_setup
    item_line_id = 1
    expected_data = {
        "id": 1,
        "name": "Home Appliances",
        "description": "",
        "created_at": "1979-01-16 07:07:50",
        "updated_at": "2024-01-05 23:53:25"
    }

    response = requests.get(f'{base_url}/{item_line_id}', headers=headers)

    assert response.status_code == 200
    assert response.json() == expected_data  # Fixed response.json call

    if response.status_code == 200:
        print("The requested ID has been successfully retrieved.")
    else:
        print("The requested ID has not been retrieved.")


# Test: Update (PUT) item line
def test_put_item_line(api_setup):
    base_url, headers = api_setup
    data = {
        "id": 97,
        "name": "Testing item_lines",
        "description": "integration test",
        "created_at": "2007-12-31 10:48:06",
        "updated_at": "2023-08-22 06:43:47"
    }
    item_line_id = 97

    response = requests.put(
        f'{base_url}/{item_line_id}', headers=headers, json=data)

    assert response.status_code == 200
    if response.status_code == 200:
        print("The requested ID has been successfully updated.")
    else:
        print("The requested ID has not been updated.")


# Test: Delete item line
def test_delete_item_line(api_setup):
    base_url, headers = api_setup
    item_line_id = 97

    response = requests.delete(f'{base_url}/{item_line_id}', headers=headers)

    assert response.status_code == 200
    if response.status_code == 200:
        print("The requested ID has been successfully deleted.")
    else:
        print("The requested ID has not been deleted.")
