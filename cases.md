# Pet Store API Test Cases

## Table of Contents
1. [Create Pet](#1-create-pet)
2. [Get Pet](#2-get-pet)
3. [Update Pet](#3-update-pet)
4. [Delete Pet](#4-delete-pet)
5. [Create Pet with Invalid Data](#5-create-pet-with-invalid-data)
6. [Create Order](#6-create-order)
7. [Create Pet with Different Statuses](#7-create-pet-with-different-statuses)

## 1. Create Pet
**Description**: Verify that a new pet can be created successfully

**Precondition**: None

**Test Data**:

Test Data: 
```json 
 "name": "doggie_{unique_id}", "category": { "id": 1, "name": "dogs" }, "photoUrls": ["string"], "tags": [ { "id": 0, "name": "string" } ], "status": "available" }
```
**Expected Result**:
- Status code: 200
- Response body contains correct pet data
- Pet name matches input
- Pet status matches input

## 2. Get Pet
**Description**: Verify that an existing pet can be retrieved

**Precondition**: Pet exists in the system

**Test Steps**:
1. Create a new pet
2. Get pet by ID

**Expected Result**:
- Status code: 200
- Response contains correct pet data
- All fields match the created pet data

## 3. Update Pet
**Description**: Verify that an existing pet can be updated

**Precondition**: Pet exists in the system

**Test Data**: 
```json
 "id": "{existing_pet_id}", "name": "updated_doggie_{unique_id}", "status": "pending" }
```
**Expected Result**:
- Status code: 200
- Pet name is updated
- Pet status is updated

## 4. Delete Pet
**Description**: Verify that a pet can be deleted

**Precondition**: Pet exists in the system

**Test Steps**:
1. Create a new pet
2. Delete pet by ID
3. Try to get deleted pet

**Expected Result**:
- Delete status code: 200
- Get request returns 404

## 5. Create Pet with Invalid Data
**Description**: Verify system handles invalid data correctly

**Test Data**: 
```json
 "category": { "id": "invalid", "name": 123 }, "name": "", "photoUrls": null, "status": "invalid_status" }
```
**Expected Result**:
- Status code: 400 or 500
- Error response received

## 6. Create Order
**Description**: Verify that a new order can be created

**Test Data**:
```json
 { "id": 1, "petId": 1, "quantity": 1, "shipDate": "{current_datetime}", "status": "placed", "complete": true }
```
**Expected Result**:
- Status code: 200
- Order created successfully
- Order details match input data

## 7. Create Pet with Different Statuses
**Description**: Verify pet creation with various status values

**Test Data**: 
```json
{ "statuses": ["available", "pending", "sold"], "pet_data": { "name": "doggie_{unique_id}", "category": { "id": 1, "name": "dogs" }, "photoUrls": ["string"], "tags": [ { "id": 0, "name": "string" } ] } }
```
**Expected Result**:
- Status code: 200 for each status
- Pet created successfully with each status
- Response data matches input data
Note: All test cases include detailed logging and Allure reporting for better test execution analysis and reporting.