import pytest
from models.locations import Locations

@pytest.fixture
def locations():
    """Init locations met debug on"""
    return Locations(root_path='', is_debug=True)

def test_add_location(locations):
    """Test toevoegen locatie"""
    location = {
        "id": 1, # Unieke id
        "warehouse_id": 102, # ID van magazijn
        "name": "Location 1" # Naam locatie
    }
    locations.add_location(location) # Voeg locatie toe aan in memory

    # 1 Controlleer of eht aantal locaties in data nu 1 is
    assert len(locations.data) == 1
    # 2 Controlleer of de toegevoegde locatie de juiste naam heeft
    assert locations.data[0]["name"] == "Location 1"