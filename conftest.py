import pytest
from src.api.pet_api import PetApi
from src.api.store_api import StoreApi

@pytest.fixture(scope="session")
def base_url():
    return "https://petstore.swagger.io/v2"

@pytest.fixture
def pet_api(base_url):
    return PetApi(base_url)

@pytest.fixture
def store_api(base_url):
    return StoreApi(base_url)

@pytest.fixture
def pet_data():
    return {
        "category": {"id": 1, "name": "dogs"},
        "name": "doggie",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available"
    }

@pytest.fixture
def order_data():
    return {
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2025-01-11T10:00:00.000Z",
        "status": "placed",
        "complete": True
    }
