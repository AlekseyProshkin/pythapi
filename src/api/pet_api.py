import requests
import allure
from typing import Dict, Any
from src.utils.logger import logger, log_request_response


class PetApi:
    """Class for handling Pet API endpoints"""

    def __init__(self, base_url: str):
        """Initialize PetApi with base URL

        Args:
            base_url (str): Base URL of the Pet Store API
        """
        self.base_url = base_url
        self.pet_endpoint = f"{base_url}/pet"

    @allure.step("Create new pet")
    def create_pet(self, pet_data: Dict[str, Any]) -> requests.Response:
        """Create a new pet

        Args:
            pet_data (Dict[str, Any]): Pet data to create

        Returns:
            requests.Response: Response from the API
        """
        logger.info(f"Creating new pet with data: {pet_data}")
        response = requests.post(self.pet_endpoint, json=pet_data)
        log_request_response(pet_data, response)
        return response

    @allure.step("Get pet by ID")
    def get_pet(self, pet_id: int) -> requests.Response:
        """Get pet by ID

        Args:
            pet_id (int): ID of the pet to retrieve

        Returns:
            requests.Response: Response from the API
        """
        logger.info(f"Getting pet with ID: {pet_id}")
        response = requests.get(f"{self.pet_endpoint}/{pet_id}")
        log_request_response({"pet_id": pet_id}, response)
        return response

    @allure.step("Update existing pet")
    def update_pet(self, pet_data: Dict[str, Any]) -> requests.Response:
        """Update an existing pet

        Args:
            pet_data (Dict[str, Any]): Updated pet data

        Returns:
            requests.Response: Response from the API
        """
        logger.info(f"Updating pet with data: {pet_data}")
        response = requests.put(self.pet_endpoint, json=pet_data)
        log_request_response(pet_data, response)
        return response

    @allure.step("Delete pet")
    def delete_pet(self, pet_id: int) -> requests.Response:
        """Delete a pet

        Args:
            pet_id (int): ID of the pet to delete

        Returns:
            requests.Response: Response from the API
        """
        logger.info(f"Deleting pet with ID: {pet_id}")
        response = requests.delete(f"{self.pet_endpoint}/{pet_id}")
        log_request_response({"pet_id": pet_id}, response)
        return response

    @allure.step("Find pets by status")
    def find_pets_by_status(self, status: str) -> requests.Response:
        """Find pets by status

        Args:
            status (str): Status value to filter pets

        Returns:
            requests.Response: Response from the API
        """
        logger.info(f"Finding pets by status: {status}")
        params = {"status": status}
        response = requests.get(f"{self.pet_endpoint}/findByStatus", params=params)
        log_request_response({"status": status}, response)
        return response

    @allure.step("Update pet with form data")
    def update_pet_with_form(self, pet_id: int, name: str = None, status: str = None) -> requests.Response:
        """Update a pet in the store with form data

        Args:
            pet_id (int): ID of pet to update
            name (str, optional): Updated name of the pet
            status (str, optional): Updated status of the pet

        Returns:
            requests.Response: Response from the API
        """
        logger.info(f"Updating pet {pet_id} with form data: name={name}, status={status}")
        data = {}
        if name:
            data["name"] = name
        if status:
            data["status"] = status

        response = requests.post(f"{self.pet_endpoint}/{pet_id}", data=data)
        log_request_response(data, response)
        return response
