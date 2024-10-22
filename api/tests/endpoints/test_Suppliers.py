import pytest
import requests 


@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/'



    
def test_create_supplier(_url):

    supplier_id = 123456789123456789  # ID
    url = _url + f'suppliers/{supplier_id}'


    headers = {
        'API_KEY': 'a1b2c3d4e5',  
        'Content-Type': 'application/json'
    }


    data = {
        "id": 123456789123456789,
        "code": "testing",
        "name": "testing",
        "address": "testing",
        "address_extra": "testing",
        "city": "testing",
        "zip_code": "testing",
        "province": "testing",
        "country": "testing",
        "contact_name": "testing",
        "phonenumber": "testing",
        "reference": "testing",
        "created_at": "testing",
        "updated_at": "testing"
    }

    # Send a GET request to the API
    response = requests.post(url,headers=headers, json=data)
    

    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")
    print(f"Request URL: {response.url}")
    

    status_code = response.status_code
    assert status_code == 201


def test_get_supplier(_url):
    supplier_id = 123456789123456789  # ID
    url = _url + f'suppliers/{supplier_id}'  # Suppliers endpoint
    

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


def test_update_suppliers(_url):
    supplier_id = 123456789123456789  # ID
    url = _url + f'suppliers/{supplier_id}'  # Suppliers endpoint
    

    headers = {
        'API_KEY': 'a1b2c3d4e5',  
        'Content-Type': 'application/json'
    }
    
    data = {
        "id": 123456789123456789,
        "code": "testing UPDATED",
        "name": "testing UPDATED",
        "address": "testing UPDATED",
        "address_extra": "testing UPDATED",
        "city": "testing UPDATED",
        "zip_code": "testing UPDATED",
        "province": "testing UPDATED",
        "country": "testing UPDATED",
        "contact_name": "testing UPDATED",
        "phonenumber": "testing UPDATED",
        "reference": "testing UPDATED",
        "created_at": "testing UPDATED",
        "updated_at": "testing UPDATED"
    }
    
    response = requests.put(url, json=data, headers=headers)
    # Check the response
    if response.status_code == 200:
     print("PUT request successful")
     
     

def test_delete_supplier(_url):

    supplier_id = 123456789123456789  # ID
    url = _url + f'suppliers/{supplier_id}'  # Suppliers endpoint
    

    headers = {
        'API_KEY': 'a1b2c3d4e5',  
        'Content-Type': 'application/json'
    }

    response = requests.delete(url, headers=headers)
   
    # Check the response
    if response.status_code == 200:
     print("PUT request successful")
     
     
def test_test_item_supplier(_url):
    supplier_id = 123456789123456789  # ID
    url = _url + f'suppliers/{supplier_id}'  # Suppliers endpoint
    

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
