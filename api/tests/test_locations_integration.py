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

