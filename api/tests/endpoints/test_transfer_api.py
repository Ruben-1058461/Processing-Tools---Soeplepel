import pytest 
import requests 


@pytest.fixture 
def setup():
    url = 'http://localhost:3000/api/v1/'

    headers = {
        'api_key': 'a1b2c3d4e5',
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    return url, headers 



def test_post_transfer(setup):
    url, headers = setup 
    transfer_id = 123456789
    testurl = url + f'transfers/{transfer_id}'



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



    status_code = post_response.status_code
    assert status_code == 201






def test_get_transfer(setup):
    url, headers = setup  
    transfer_id = 123456789
    testurl = url + f'transfers/{transfer_id}'



    get_response = requests.get(testurl, headers=headers)


    status_code = get_response.status_code

    assert status_code == 200



def test_update_transfer(setup):
    url, headers = setup 
    transfer_id = 123456789
    testurl = url + f'transfers/{transfer_id}'


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

    
    assert up_response.status_code == 200


def test_delete_transfer(setup):
    url, headers = setup 
    transfer_id = 123456789
    testurl = url + f'transfers/{transfer_id}'


    del_response = requests.delete(testurl, headers=headers)


    assert del_response.status_code == 200


    
def test_postnoitems(setup): 
    url, headers = setup
    transfer_id =  12999999   	
    testurl = url + f'transfers/{transfer_id}'


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

    
    status_code = post_response.status_code
    assert status_code == 201

def test_delete_transferbyid(setup):
    url, headers = setup 
    transfer_id = 12999999
    testurl = url + f'transfers/{transfer_id}'


    del_response = requests.delete(testurl, headers=headers)

    
    assert del_response.status_code == 200





