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

def test_get_item_lines_by_id(api_setup):
    base_url, headers = api_setup
    item_line_id = 1
    response = requests.get(f'{base_url}/{item_line_id}', headers=headers)

    assert response.status_code == 200

# Test: Compare item lines with data
def test_compare_item_lines_with_data(api_setup):
    base_url, headers = api_setup
    item_line_id = 1
    data = {
        "id": 1,
        "name": "Home Appliances",
        "description": "",
        "created_at": "1979-01-16 07:07:50",
        "updated_at": "2024-01-05 23:53:25"
    }

    response = requests.get(f'{base_url}/{item_line_id}', headers=headers)

    assert response.status_code == 200
    assert response.json() == data


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

# Test: Delete item line
def test_delete_item_line(api_setup):
    base_url, headers = api_setup
    item_line_id = 97

    response = requests.delete(f'{base_url}/{item_line_id}', headers=headers)

    assert response.status_code == 200
