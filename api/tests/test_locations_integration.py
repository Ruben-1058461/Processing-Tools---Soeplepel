import pytest
from models.locations import Locations

@pytest.fixture
def locations(tmp_path):
    """init locations"""
    # Tijdelijk path
    data_path = tmp_path / "locations.json"

    locations_instance = Locations(root_path=str(tmp_path) + "/", is_debug=True)

    return locations_instance



def test_add_and_get_location_integration(locations):
    """Integratietest voor add en get locatie"""
    location = {
        "id": 1,
        "warehouse_id": 101,
        "name": "Location 1"
    }

    # Voeg locatie toe
    locations.add_location(location)

    # Haal locatie op
    result = locations.get_location(1)

    assert result is not None # Locatie moet bestaan
    assert result["name"] == "Location 1"


def test_not_existing_location_integration(locations):
    """Integratietest voor het ophalen van niet bestaande locatie."""
    # Haal locatie op die niet bestaat
    result = locations.get_location(123456) # Fake id

    assert result is None # Dit moet uitkomen op None

def test_updating_location_integration(locations):
    """Integratietest voor het bijwerken van location"""
    location = {
        "id": 1,
        "warehouse_id": 101,
        "name": "Location 1"
    }

    # Voeg locatie toe
    locations.add_location(location)

    updated_location = {
        "id": 1,
        "warehouse_id": 102,
        "name": "Updated location 1"
    }

    
    locations.update_location(1, updated_location)

    # Haal de locatie opnieuw op
    result = locations.get_location(1)

    
    assert result is not None  # De locatie moet bestaan
    assert result["warehouse_id"] == 102  # De naam moet zijn bijgewerkt
    assert result["name"] == "Updated location 1"  # De naam moet zijn bijgewerkt

def test_remove_location_integration(locations):
    """Integratietest voor verwijderen locatie"""
    location = {
        "id": 1,
        "warehouse_id": 101,
        "name": "Location 1"
    }

    # Voeg locatie toe
    locations.add_location(location)

    # Verwijder locatie
    locations.remove_location(1)

    # Check of die verwijdert is
    result = locations.get_location(1)

    assert result is None # Check of het gelukt is


def test_get_locations_in_warehouse(locations):
    """Integratietest voor het ophalen van locaties in een magazijn"""
    # Voeg meerdere locaties toe aan hetzelfde magazijn
    location1 = {"id": 1, "warehouse_id": 101, "name": "Location 1"}
    location2 = {"id": 2, "warehouse_id": 101, "name": "Location 2"}
    location3 = {"id": 3, "warehouse_id": 102, "name": "Location 3"}
    
    locations.add_location(location1)
    locations.add_location(location2)
    locations.add_location(location3)

    # Haal locaties op voor warehouse_id 101
    results = locations.get_locations_in_warehouse(101)


    assert len(results) == 2  # Er moeten 2 locaties zijn in warehouse_id 101
    assert results[0]["name"] in ["Location 1", "Location 2"]  # Controleer namen
    assert results[1]["name"] in ["Location 1", "Location 2"]  # Controleer namen
