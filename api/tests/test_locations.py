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

def test_get_location(locations):
    """Test voor het ophalen van locatie op ID"""
    location = {
        "id": 1, # ID voor testlocatie
        "warehouse_id": 102, # Warehouse id 
        "name": "Location 1" # Naam locatie 
    }
    locations.add_location(location)  # Testlocatie

    # Ophalen van de locatie met ID
    result = locations.get_location(1)

    # Check of er een resultaat is
    assert result is not None

    # Check of naam overeenkomt met die toegevoegd is
    assert result["name"] == "Location 1"

def test_delete_location(locations):
    """Test het verwijderen van een locatie"""
    location = {
        "id": 1,
        "warehouse_id": 101,
        "name": "Location 1"
    }
    # Voeg locatie toe aan de locations
    locations.add_location(location)

    # Verwijder op basis van id (1)
    locations.remove_location(1)

    # Probeer opnieuw op te halen om checken of verwijdert
    result = locations.get_location(1) # We verwachten none want hij is verwijdert

    # Controleer of die verwijderd is
    assert result is None