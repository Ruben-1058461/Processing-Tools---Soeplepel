import pytest
from providers.data_provider import init, fetch_warehouse_pool, fetch_location_pool, fetch_item_pool
from models.warehouses import Warehouses
from models.locations import Locations
from models.items import Items

@pytest.fixture(scope="module")
def setup_data():
    """Fixture voor het initialiseren van de DataProvider."""
    init()  # Initialiseer de dataprovider hier
    yield  # Hier kan je eventueel meer data instellen als dat nodig is

def test_init(setup_data):
    """Test dat de DataProvider succesvol is geïnitialiseerd."""
    assert fetch_warehouse_pool() is not None
    assert fetch_location_pool() is not None
    assert fetch_item_pool() is not None


def test_fetch_warehouse_pool(setup_data):
    """Test dat we een Warehouse object kunnen ophalen."""
    warehouses = fetch_warehouse_pool()
    assert warehouses is not None  # Controleer dat we gegevens hebben
    assert isinstance(warehouses, Warehouses)  # Controleer dat het een warehouses object is
    

def test_fetch_location_pool(setup_data):
    """Test dat we een Locations object kunnen ophalen."""
    locations = fetch_location_pool()
    assert locations is not None  # Controleer dat we gegevens hebben
    assert isinstance(locations, Locations)  # Controleer dat het een Locations object is

def test_fetch_item_pool(setup_data):
    """Test dat we een Items object kunnen ophalen."""
    items = fetch_item_pool()
    assert items is not None  # Controleer dat we gegevens hebben
    assert isinstance(items, Items)  # Controleer dat het een Items object is
