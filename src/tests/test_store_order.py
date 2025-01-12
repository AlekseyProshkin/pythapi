import allure
import pytest
from datetime import datetime


@allure.epic("Pet Store API Testing")
class TestStoreOrder:
    @pytest.fixture
    def order_data(self):
        """Fixture for creating base order data"""
        return {
            "id": 1,
            "petId": 1,
            "quantity": 1,
            "shipDate": datetime.now().isoformat(),
            "status": "placed",
            "complete": True
        }

    @allure.feature("Store Operations")
    @allure.story("Create and Verify Order")
    @allure.description("Test creating a new order and verifying its details")
    def test_create_and_verify_order(self, store_api, order_data):
        """
        Test creating and verifying store order:
        1. Create new order
        2. Verify creation response
        3. Get created order
        4. Verify order details
        """
        """Create new order"""
        with allure.step("Create new order"):
            create_response = store_api.create_order(order_data)

        with allure.step("Verify create response status code"):
            assert create_response.status_code == 200, \
                f"Expected status code 200, but got {create_response.status_code}"

        with allure.step("Get order details from response"):
            created_order = create_response.json()
            order_id = created_order["id"]
            allure.attach(
                str(created_order),
                name="Created Order Response",
                attachment_type=allure.attachment_type.TEXT
            )

        """Get and verify created order """
        with allure.step(f"Get created order with id: {order_id}"):
            get_response = store_api.get_order(order_id)

        with allure.step("Verify get response status code"):
            assert get_response.status_code == 200, \
                f"Expected status code 200, but got {get_response.status_code}"

        with allure.step("Verify order details"):
            get_order_data = get_response.json()
            allure.attach(
                str(get_order_data),
                name="Retrieved Order Data",
                attachment_type=allure.attachment_type.TEXT
            )

            assert get_order_data["petId"] == order_data["petId"], \
                f"Pet ID mismatch. Expected {order_data['petId']}, got {get_order_data['petId']}"
            assert get_order_data["quantity"] == order_data["quantity"], \
                f"Quantity mismatch. Expected {order_data['quantity']}, got {get_order_data['quantity']}"
            assert get_order_data["status"] == order_data["status"], \
                f"Status mismatch. Expected {order_data['status']}, got {get_order_data['status']}"
            assert get_order_data["complete"] == order_data["complete"], \
                f"Complete flag mismatch. Expected {order_data['complete']}, got {get_order_data['complete']}"

    @allure.feature("Store Operations")
    @allure.story("Negative Testing - Invalid Order")
    def test_create_order_with_invalid_data(self, store_api):
        """Test creating order with invalid data"""
        invalid_order_data = {
            "id": "invalid_id",  """Should be integer""" 
            "petId": -1,  """Invalid pet ID"""
            "quantity": "invalid_quantity",  """Should be integer"""
            "shipDate": "invalid_date",  """Invalid date format"""
            "status": "invalid_status", """Invalid status """
            "complete": "not_boolean"  """Should be boolean """
        }

        with allure.step("Try to create order with invalid data"):
            response = store_api.create_order(invalid_order_data)

        with allure.step("Verify error response"):
            assert response.status_code in [400, 500], \
                f"Expected status code 400 or 500, but got {response.status_code}"

            allure.attach(
                str(response.json()),
                name="Error Response",
                attachment_type=allure.attachment_type.TEXT
            )
