import pytest
from providers.auth_provider import init, get_user, has_access

# Door fixture is auth provider altijd geinitialiseerd
@pytest.fixture(autouse=True)
def setup_auth_provider():
    """Initialiseer authprovider met gebruikergegevens."""
    init()

def test_get_user_valid_api_key():
    """"Test dat een geldige api-key de juiste gebruiker terugstuurd."""
    user = get_user("a1b2c3d4e5") # Sleutel
    assert user is not None # Ik verwacht dat het een gebruiker teruggeefd  
    assert user["app"] == "Cargohub Dashboard 1" # Controleer dat het de juiste gebruiker is opgehaald

def test_get_user_invalid_api_key():
    """Test dat een ongeldige api-key geen gebruiker terugstuurd."""
    user = get_user("invalid_api_key")
    assert user is None # We verwachten dat geen gebruiker word teruggegeven
