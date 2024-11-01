import pytest 
import requests 


@pytest.fixture 
def url():
    return 'http://localhost:3000/api/v1/'



def test_post_warehouse(url):
    warehouse_id = 123456789
    testurl = url + f'warehouses/{warehouse_id}'

    headers = {
        'api_key': 'a1b2c3d4e5',
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    data =     {
        "id": warehouse_id,
        "code": "testing",
        "name": "testingname",
        "address": "testing",
        "zip": "testing",
        "city": "testing",
        "province": "testing",
        "country": "NL",
        "contact": {
            "name": "Sjoerd Sterkman",
            "phone": "0943-736616",
            "email": "imkehermans@example.org"
        },
        "created_at": "2017-11-03 19:21:26",
        "updated_at": "2023-05-30 16:45:10"
    } 

    post_response = requests.post(testurl, headers=headers, json=data)

    status_code = post_response.status_code
    assert status_code == 201



def test_get_warehouse(url): 
    warehouse_id = 123456789
    testurl = url + f'warehouses/{warehouse_id}'

    headers = {
        'api_key': 'a1b2c3d4e5', 
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    get_response = requests.get(testurl, headers=headers)



    status_code = get_response.status_code

    assert status_code == 200



def test_update_locations(url):
    warehouse_id = 123456789
    testurl = url + f'warehouses/{warehouse_id}'

    headers = {
        'api_key': 'a1b2c3d4e5', 
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    data =  {
        "id": warehouse_id,
        "code": "update",
        "name": "update",
        "address": "being updated",
        "zip": "updated",
        "city": "updated",
        "province": "Flevoland",
        "country": "NL",
        "contact": {
            "name": "Jamie van Bruchem",
            "phone": "+31(0)563-472814",
            "email": "lizzvan-duvenvoirde@example.org"
        },
        "created_at": "2001-01-26 13:25:16",
        "updated_at": "2012-10-14 14:49:08"
    }


    up_response = requests.put(testurl, headers=headers, json=data)

    assert up_response.status_code == 200


def test_delete_warehouse(url):
    warehouse_id = 123456789
    testurl = url + f'warehouses/{warehouse_id}'

    headers = {
        'api_key': 'a1b2c3d4e5', 
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    del_response = requests.delete(testurl, headers=headers)

    assert del_response.status_code == 200



def test_post_with_no_warehousecontact(url): 
    warehouse_id =  12999999   	
    testurl = url + f'warehouses/{warehouse_id}'

    headers = {
        'api_key': 'a1b2c3d4e5', 
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    data = {
        "id": warehouse_id,
        "code": "BWRXNLH6",
        "name": "Standdaarbuiten longterm facility",
        "address": "Louisedreef 0",
        "zip": "5149 RW",
        "city": "Standdaarbuiten",
        "province": "Flevoland",
        "country": "NL",
        "created_at": "1983-07-10 13:29:30",
        "updated_at": "2020-05-17 04:19:20"
    }


    post_response = requests.post(testurl,headers=headers, json=data)


    status_code = post_response.status_code
    assert status_code == 201

def test_delete_warehouse_by_id(url):
    warehouse_id = 12999999
    testurl = url + f'warehouses/{warehouse_id}'

    headers = {
        'api_key': 'a1b2c3d4e5', 
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    del_response = requests.delete(testurl, headers=headers)

    assert del_response.status_code == 200





