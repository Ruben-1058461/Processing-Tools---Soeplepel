import pytest

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
