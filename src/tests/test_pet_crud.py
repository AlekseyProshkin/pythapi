import pytest
import allure
import uuid
import random
from datetime import datetime


@allure.epic("Pet Store API Testing")
class TestPetCrud:
    @pytest.fixture
    def pet_data(self):
        """Fixture for creating base pet data with unique ID and name"""
        unique_id = random.randint(1, 100000)
        unique_name = f"doggie_{str(uuid.uuid4())[:8]}"
        return {
            "id": unique_id,
            "category": {"id": 1, "name": "dogs"},
            "name": unique_name,
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }

    @allure.feature("Pet CRUD Operations")
    @allure.story("Create Pet")
    @allure.description("Test creating a new pet in the store")
    def test_create_pet(self, pet_api, pet_data):
        with allure.step("Create new pet"):
            response = pet_api.create_pet(pet_data)
            allure.attach(str(response.json()), 'Response', allure.attachment_type.TEXT)

        with allure.step("Verify response status code"):
            assert response.status_code == 200

        with allure.step("Verify response data"):
            response_data = response.json()
            assert response_data["name"] == pet_data["name"]
            assert response_data["status"] == pet_data["status"]

    @allure.feature("Pet CRUD Operations")
    @allure.story("Read Pet")
    @allure.description("Test retrieving pet details")
    def test_get_pet(self, pet_api, pet_data):
        with allure.step("Create pet for testing"):
            create_response = pet_api.create_pet(pet_data)
            created_pet = create_response.json()
            pet_id = created_pet["id"]
            allure.attach(str(created_pet), 'Created Pet', allure.attachment_type.TEXT)

        with allure.step(f"Get pet with id {pet_id}"):
            get_response = pet_api.get_pet(pet_id)
            retrieved_pet = get_response.json()
            allure.attach(str(retrieved_pet), 'Retrieved Pet', allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert get_response.status_code == 200
            assert retrieved_pet["id"] == created_pet["id"]
            assert retrieved_pet["name"] == created_pet["name"], \
                f"Expected name {created_pet['name']}, but got {retrieved_pet['name']}"
            assert retrieved_pet["status"] == created_pet["status"], \
                f"Expected status {created_pet['status']}, but got {retrieved_pet['status']}"

    @allure.feature("Pet CRUD Operations")
    @allure.story("Update Pet")
    @allure.description("Test updating an existing pet")
    def test_update_pet(self, pet_api, pet_data):
        with allure.step("Create pet for testing"):
            create_response = pet_api.create_pet(pet_data)
            created_pet = create_response.json()
            pet_id = created_pet["id"]
            allure.attach(str(created_pet), 'Initial Pet', allure.attachment_type.TEXT)

        updated_data = pet_data.copy()
        updated_name = f"updated_{str(uuid.uuid4())[:8]}"
        updated_data.update({
            "id": pet_id,
            "name": updated_name,
            "status": "pending"
        })

        with allure.step("Update pet"):
            response = pet_api.update_pet(updated_data)
            allure.attach(str(response.json()), 'Updated Pet', allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code == 200
            response_data = response.json()
            assert response_data["name"] == updated_data["name"], \
                f"Expected name to be {updated_data['name']}, but got {response_data['name']}"
            assert response_data["status"] == updated_data["status"], \
                f"Expected status to be {updated_data['status']}, but got {response_data['status']}"

    @allure.feature("Pet CRUD Operations")
    @allure.story("Delete Pet")
    @allure.description("Test deleting a pet from the store")
    def test_delete_pet(self, pet_api, pet_data):
        with allure.step("Create pet for testing"):
            create_response = pet_api.create_pet(pet_data)
            created_pet = create_response.json()
            pet_id = created_pet["id"]
            allure.attach(str(created_pet), 'Pet to Delete', allure.attachment_type.TEXT)

        with allure.step(f"Delete pet with id {pet_id}"):
            response = pet_api.delete_pet(pet_id)
            allure.attach(str(response.json()), 'Delete Response', allure.attachment_type.TEXT)

        with allure.step("Verify delete response"):
            assert response.status_code == 200
            delete_response_data = response.json()
            assert delete_response_data["code"] == 200
            assert str(pet_id) in delete_response_data["message"]

        with allure.step("Verify pet data after deletion"):
            get_response = pet_api.get_pet(pet_id)
            allure.attach(str(get_response.json() if get_response.status_code == 200 else get_response.text),
                          'Get After Delete Response', allure.attachment_type.TEXT)

            if get_response.status_code == 404:
                assert True, "Pet was successfully deleted"
            else:
                get_response_data = get_response.json()
                assert (get_response_data["status"] != created_pet["status"] or
                        get_response_data["name"] != created_pet["name"]), \
                    "Pet data should be different after deletion"

    @allure.feature("Pet CRUD Operations")
    @allure.story("Negative Testing")
    @allure.description("Test creating pet with invalid data")
    def test_create_pet_invalid_data(self, pet_api):
        invalid_pet_data = {
            "category": {"id": "invalid", "name": 123},
            "name": "",
            "photoUrls": None,
            "status": "invalid_status"
        }

        with allure.step("Try to create pet with invalid data"):
            response = pet_api.create_pet(invalid_pet_data)
            allure.attach(str(response.text), 'Error Response', allure.attachment_type.TEXT)

        with allure.step("Verify error response"):
            assert response.status_code in [400, 500]
