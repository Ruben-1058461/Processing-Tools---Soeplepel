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



def test_post_location(setup):
    url, headers = setup 
    location_id = 123456789
    testurl = url + f'locations/{location_id}'



    data = {
        "id": location_id,
        "warehouse_id": 60,
        "code": "A.2.2",
        "name": "Row: A, Rack: 2, Shelf: 2",
        "created_at": "1992-05-15 03:21:32",
        "updated_at": "1992-05-15 03:21:32"
    }

    post_response = requests.post(testurl, headers=headers, json=data)

    status_code = post_response.status_code
    assert status_code == 201



def test_get_location(setup): 
    url, headers = setup
    location_id = 123456789
    testurl = url + f'locations/{location_id}'

    

    get_response = requests.get(testurl, headers=headers)



    status_code = get_response.status_code

    assert status_code == 200



def test_update_locations(setup):
    url, headers = setup
    location_id = 123456789
    testurl = url + f'locations/{location_id}'

    

    data = {
        "id": location_id,
        "warehouse_id": 60,
        "code": "testing",
        "name": "testing",
        "created_at": "1992-05-15 03:21:32",
        "updated_at": "1992-05-15 03:21:32"
    }



    up_response = requests.put(testurl, headers=headers, json=data)

    assert up_response.status_code == 200


def test_delete_location(setup):
    url, headers = setup
    location_id = 123456789
    testurl = url + f'locations/{location_id}'

   

    del_response = requests.delete(testurl, headers=headers)

    assert del_response.status_code == 200



def test_post_with_no_warehouse_id(setup): 
    url, headers = setup
    location_id =  12999999   	
    testurl = url + f'locations/{location_id}'

   

    data =     {
        "id": location_id,
        "code": "A.5.1",
        "name": "Row: A, Rack: 5, Shelf: 1",
        "created_at": "1992-05-15 03:21:32",
        "updated_at": "1992-05-15 03:21:32"
    }


    post_response = requests.post(testurl,headers=headers, json=data)


    status_code = post_response.status_code
    assert status_code == 201

def test_delete_location_by_id(setup):
    url, headers = setup
    location_id = 12999999
    testurl = url + f'locations/{location_id}'

    headers = {
        'api_key': 'a1b2c3d4e5', 
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    del_response = requests.delete(testurl, headers=headers)

    assert del_response.status_code == 200