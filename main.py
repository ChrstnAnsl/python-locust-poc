from locust import HttpUser, task, between
import random

class SpikeUser(HttpUser):
    wait_time = between(1, 5)  # 1 second to 5 seconds
    host = "https://ansel-mock-api.azurewebsites.net"

    user_counter = 0  # Class variable to track user count
    
    def on_start(self):
        self.username = "test123"
        self.password = "Test1234!"

    @task
    def register_and_login(self):
        headers = {'Content-Type': 'application/json'}

        # Register
        register_payload = {
            "username": self.username,
            "password": self.password
        }
        response_register = self.client.post("/public/register", json=register_payload, headers=headers)
        print("Register response:", response_register.text, response_register.status_code)

        assert response_register.status_code == 200, f"{response_register.status_code}"
        # assert "message" in response_register.json(), "Registration failed"

        self.wait()

        # Login
        login_payload = {
            "username": self.username,
            "password": self.password
        }
        response_login = self.client.post("/public/login", json=login_payload, headers=headers)
        print("Login response:", response_login.text, response_login.status_code)

        assert response_login.status_code == 200, f"{response_login.status_code}"
        # assert "message" in response_login.json(), "Login failed"
