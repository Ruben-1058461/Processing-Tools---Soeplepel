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




def test_post_shipment(setup):
    url ,headers = setup 
    shipment_id = 123456789
    testurl = url + f'shipments/{shipment_id}'


    data = {
        "id": shipment_id,
        "order_id": 3,
        "source_id": 52,
        "order_date": "1973-01-28",
        "request_date": "1973-01-30",
        "shipment_date": "1973-02-01",
        "shipment_type": "I",
        "shipment_status": "testing",
        "notes": "testing",
        "carrier_code": "testing",
        "carrier_description": "testing",
        "service_code": "testing",
        "payment_type": "testing",
        "transfer_mode": "testing",
        "total_package_count": 29,
        "total_package_weight": 463.0,
        "created_at": "1973-01-28T20:09:11Z",
        "updated_at": "1973-01-29T22:09:11Z",
        "items": [
            {
                "item_id": "P010669",
                "amount": 16
            }
        ]
    } 

    post_response = requests.post(testurl, headers=headers, json=data)

    status_code = post_response.status_code
    assert status_code == 201



def test_get_shipment(setup):     
    url, headers = setup 
    shipment_id = 123456789
    testurl = url + f'shipments/{shipment_id}'

    get_response = requests.get(testurl, headers=headers)

    status_code = get_response.status_code

    assert status_code == 200



def test_update_shipment(setup):
    url, headers = setup
    shipment_id = 123456789
    testurl = url + f'shipments/{shipment_id}'


    data = {
        "id": 3,
        "order_id": 3,
        "source_id": 52,
        "order_date": "1973-01-28",
        "request_date": "1973-01-30",
        "shipment_date": "1973-02-01",
        "shipment_type": "Update",
        "shipment_status": "Update",
        "notes": "Update",
        "carrier_code": "Update",
        "carrier_description": "Update",
        "service_code": "NextDay",
        "payment_type": "Automatic",
        "transfer_mode": "Ground",
        "total_package_count": 29,
        "total_package_weight": 463.0,
        "created_at": "1973-01-28T20:09:11Z",
        "updated_at": "1973-01-29T22:09:11Z",
        "items": [
            {
                "item_id": "P010669",
                "amount": 16
            }
        ]
    }
        

   
    up_response = requests.put(testurl, headers=headers, json=data)

    assert up_response.status_code == 200

 
def test_delete_shipment(setup):
    url, headers = setup
    shipment_id = 123456789
    testurl = url + f'shipments/{shipment_id}'



    del_response = requests.delete(testurl, headers=headers)

    assert del_response.status_code == 200
 

    
def test_postnoitems(setup): 
    url, headers = setup
    shipments_id =  12999999   	
    testurl = url + f'shipments/{shipments_id}'


    data = {

        "id": shipments_id,
        "order_id": 3,
        "source_id": 52,
        "order_date": "1973-01-28",
        "request_date": "1973-01-30",
        "shipment_date": "1973-02-01",
        "shipment_type": "I",
        "shipment_status": "Pending",
        "notes": "Hoog genot springen afspraak mond bus.",
        "carrier_code": "DHL",
        "carrier_description": "DHL Express",
        "service_code": "NextDay",
        "payment_type": "Automatic",
        "transfer_mode": "Ground",
        "total_package_count": 29,
        "total_package_weight": 463.0,
        "created_at": "1973-01-28T20:09:11Z",
        "updated_at": "1973-01-29T22:09:11Z"

    }
    

    post_response = requests.post(testurl,headers=headers, json=data)

    
    status_code = post_response.status_code
    assert status_code == 201


def test_delete_shipmentbyid(setup):
    url, headers = setup
    shipment_id = 12999999
    testurl = url + f'shipments/{shipment_id}'



    del_response = requests.delete(testurl, headers=headers)

    assert del_response.status_code == 200




