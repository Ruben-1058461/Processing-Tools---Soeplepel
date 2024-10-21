import pytest 
import requests 


@pytest.fixture 
def url():
    return 'http://localhost:3000/api/v1/'



def test_post_transfer(url):
    transfer_id = 123456789
    testurl = url + f'transfers/{transfer_id}'

    headers = {
        'api_key': 'a1b2c3d4e5',
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    data = {
        "id": transfer_id,  # Fix here, removed curly braces
        "reference": "testing",
        "transfer_from": 6220,
        "transfer_to": 9199,
        "transfer_status": "testing",
        "created_at": "2000-03-11T13:11:14Z",
        "updated_at": "2000-03-12T14:11:14Z",
        "items": [
            {
                "item_id": "testing",
                "amount": 1
            }
        ]
    }

    post_response = requests.post(testurl, headers=headers, json=data)

    print(f"Status Code: {post_response.status_code}")
    print(f"Response Content: {post_response.content}")
    print(f"Request URL: {post_response.url}")

    status_code = post_response.status_code
    assert status_code == 201






def test_get_transfer(url): 
    transfer_id = 123456789
    testurl = url + f'transfers/{transfer_id}'

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



def test_update_transfer(url):
    transfer_id = 123456789
    testurl = url + f'transfers/{transfer_id}'

    headers = {
        'api_key': 'a1b2c3d4e5', 
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    data = {
        "id": transfer_id,
        "reference": "update",
        "transfer_from": 28430,
        "transfer_to": 28454,
        "transfer_status": "update",
        "created_at": "1995-11-24T09:18:11Z",
        "updated_at": "1995-11-25T10:18:11Z",
        "items": [
            {
                "item_id": "update",
                "amount": 0
            }
        ]
    }


    up_response = requests.put(testurl, headers=headers, json=data)

    print(f"Status Code: {up_response.status_code}")
    assert up_response.status_code == 200


def test_delete_transfer(url):
    transfer_id = 123456789
    testurl = url + f'transfers/{transfer_id}'

    headers = {
        'api_key': 'a1b2c3d4e5', 
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    del_response = requests.delete(testurl, headers=headers)

    print(f"Status Code: {del_response.status_code}")
    assert del_response.status_code == 200


    
def test_postnoitems(url): 
    transfer_id =  12999999   	
    testurl = url + f'transfers/{transfer_id}'

    headers = {
        'api_key': 'a1b2c3d4e5', 
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    data = {
        "id": transfer_id,
        "reference": "TR00037",
        "transfer_from": 28430,
        "transfer_to": 28454,
        "transfer_status": "Completed",
        "created_at": "1995-11-24T09:18:11Z",
        "updated_at": "1995-11-25T10:18:11Z",
    
    } 

    post_response = requests.post(testurl,headers=headers, json=data)

    print(f"Status Code: {post_response.status_code}")
    print(f"Response Content: {post_response.content}")
    print(f"Request URL: {post_response.url}")
    
    status_code = post_response.status_code
    assert status_code == 201







