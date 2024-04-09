import requests
import pytest
import allure

@allure.feature("User API Testing")
class TestUserAPI:

    @allure.story("Get User")
    @allure.title("Test getting user data")
    def test_get_user(self):
        
        with allure.step("Send a GET request to retrieve user data"):
            url = "https://reqres.in/api/users/2"
            response = requests.get(url)

        with allure.step("Verify the response status code is 200"):
            assert response.status_code == 200, "Response status code is not 200"

        with allure.step("Verify the presence of expected fields in the response data"):
            data = response.json()
            assert "data" in data
            user_data = data["data"]
            assert "id" in user_data
            assert "email" in user_data
            assert "first_name" in user_data
            assert "last_name" in user_data

    @allure.story("Create User")
    @allure.title("Test creating a new user")
    def test_create_user(self):

        with allure.step("Send a POST request to create a new user"):
            url = "https://reqres.in/api/users"
            payload = {"name": "dmytro", "job": "leader"}
            response = requests.post(url, json=payload)

        with allure.step("Verify the response status code is 201"):
            assert response.status_code == 201, "Response status code is not 201"

        with allure.step("Verify the presence of expected fields in the response data"):
            data = response.json()
            assert "name" in data
            assert "job" in data
            assert "id" in data
            assert "createdAt" in data

    @allure.story("Update User")
    @allure.title("Test updating user data")
    def test_update_user(self):

        with allure.step("Send a PUT request to update user data"):
            url = "https://reqres.in/api/users/2"
            payload = {"name": "dmytro", "job": "bro"}
            response = requests.put(url, json=payload)

        with allure.step("Verify the response status code is 200"):
            assert response.status_code == 200, "Response status code is not 200"

        with allure.step("Verify the presence of expected fields in the response data"):
            data = response.json()
            assert "name" in data
            assert "job" in data
            assert "updatedAt" in data

    @allure.story("Delete User")
    @allure.title("Test deleting user data")
    def test_delete_user(self):

        with allure.step("Send a DELETE request to delete user data"):
            url = "https://reqres.in/api/users/2"
            response = requests.delete(url)

        with allure.step("Verify the response status code is 204"):
            assert response.status_code == 204, "Response status code is not 204"
