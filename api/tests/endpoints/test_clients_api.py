import requests 
import pytest 


@pytest.fixture 
def setup():
    url = 'http://localhost:3000/api/v1/'
    headers = {
        'api_key': 'a1b2c3d4e5', 
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }
    return url, headers



def test_post_client(setup):
    url, headers = setup
    client_id = 123456789
    testurl = url + f'clients/{client_id}'
     

    data = {
        "id": client_id,
        "name": "testing",
        "address": "tetsing",
        "city": "testing",
        "zip_code": "testing",
        "province": "testing",
        "country": "testing",
        "contact_name": "Jose Vargas",
        "contact_phone": "(641)877-1451x37769",
        "contact_email": "parkersnow@example.org",
        "created_at": "2003-12-15 21:25:02",
        "updated_at": "2008-07-18 23:05:39"
    }
 


    post_response = requests.post(testurl, headers=headers, json=data)

    print(f"Status Code: {post_response.status_code}")
    print(f"Response Content: {post_response.content}")
    print(f"Request URL: {post_response.url}")

    status_code = post_response.status_code
    assert status_code == 201


def test_get_client(setup): 
    url, headers = setup 
    client_id = 15
    testurl = url + f'clients/{client_id}'

    headers = {
        'api_key': 'a1b2c3d4e5', 
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    get_response = requests.get(testurl, headers=headers)

    
    print(f"Status Code: {get_response.status_code}")
    print(f"Response Content: {get_response.content}")
    print(f"Request URL: {get_response.url}")

    status_code = get_response.status_code

    assert status_code == 200



def test_update_client(setup):
    url, headers = setup 
    client_id = 123456789
    testurl = url + f'clients/{client_id}'

    headers = {
        'api_key': 'a1b2c3d4e5', 
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    data = {
        "id": client_id,
        "name": "update",
        "address": "update",
        "city": "update",
        "zip_code": "76117",
        "province": "Alabama",
        "country": "update",
        "contact_name": "update",
        "contact_phone": "(641)877-1451x37769",
        "contact_email": "parkersnow@example.org",
        "created_at": "2003-12-15 21:25:02",
        "updated_at": "2008-07-18 23:05:39"
    }

   
    up_response = requests.put(testurl, headers=headers, json=data)

    print(f"Status Code: {up_response.status_code}")
    assert up_response.status_code == 200

 
def test_delete_client(setup):
    url, headers = setup
    client_id = 123456789
    testurl = url + f'clients/{client_id}'


    del_response = requests.delete(testurl, headers=headers)

    print(f"Status Code: {del_response.status_code}")
    assert del_response.status_code == 200
 

 







