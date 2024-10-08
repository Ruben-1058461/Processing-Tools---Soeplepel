import pytest
from providers.auth_provider import init, get_user, has_access

# Door fixture is auth provider altijd geinitialiseerd
@pytest.fixture(autouse=True)
def setup_auth_provider():
    """Initialiseer authprovider met gebruikergegevens."""
    init()