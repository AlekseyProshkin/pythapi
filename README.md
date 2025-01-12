# Pet Store API Test Automation
## Description
This project implements automated testing for the Pet Store API using Python, Pytest, and Allure for reporting. The test suite covers CRUD operations for pets and store orders, including both positive and negative test scenarios.

## Prerequisites
Python 3.13 or higher
pip (Python package installer)
Allure command-line tool
## Installation and Setup
1. Create and activate virtual environment:
```bash 
python -m venv .venv
source .venv/bin/activate  # For Unix/macOS
.venv\Scripts\activate     # For Windows
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Running Tests
To run all tests and generate Allure report:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```
To run specific test file:

```bash
pytest src/tests/test_pet_crud.py -v
```
## Test Cases
Detailed test cases are documented in cases.md. Main test scenarios include:

- Create Pet
- Get Pet
- Update Pet
- Delete Pet
- Create Pet with Invalid Data
- Create Order
- Create Pet with Different Statuses
## Reports
Test reports are generated using Allure Framework. After test execution, view the report:

```bash
allure serve allure-results
```
The report includes:

- Test execution results
- Test steps
- Request/response data
- Test duration
- Attachments and logs
## Technologies Used
- Python 3.13
- Pytest
- Allure Framework
- Requests library
- JSON Schema Validator
- Logging
