import logging
import allure


def setup_logger():
    logger = logging.getLogger('api_tests')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    """Add output to the console"""
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()


def log_request_response(request_data, response):
    with allure.step("Request and Response Details"):
        logger.info(f"Request URL: {response.request.url}")
        logger.info(f"Request Method: {response.request.method}")
        logger.info(f"Request Data: {request_data}")
        logger.info(f"Response Status: {response.status_code}")
        logger.info(f"Response Body: {response.text}")