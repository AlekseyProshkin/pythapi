import requests
from src.models.order import Order

class StoreApi:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.order_endpoint = f"{base_url}/store/order"

    def create_order(self, order_data: dict):
        response = requests.post(self.order_endpoint, json=order_data)
        return response

    def get_order(self, order_id: int):
        response = requests.get(f"{self.order_endpoint}/{order_id}")
        return response

    def delete_order(self, order_id: int):
        response = requests.delete(f"{self.order_endpoint}/{order_id}")
        return response
