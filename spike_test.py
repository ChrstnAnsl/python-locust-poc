from locust import HttpUser, task, between
import random
import string

class SpikeUser(HttpUser):
    wait_time = between(1, 5)  # 1 second to 5 seconds
    host = "https://ansel-mock-api.azurewebsites.net"
    
    @task
    def register_and_login(self):
        headers = {'Content-Type': 'application/json'}

        # Generate a random username and use the constant password
        username = self.generate_random_username()
        password = "Test1234!"

        # Register
        register_payload = {
            "username": username,
            "password": password
        }
        response_register = self.client.post("/public/register", json=register_payload, headers=headers)
        print("Register response:", response_register.text, response_register.status_code)
        assert response_register.status_code == 200

        # if response_register.status_code == 200:

        #     login_payload = {
        #         "username": username,
        #         "password": password
        #     }

        #     print("Login payload:", login_payload)  # Print the login payload
        #     response_login = self.client.post("/public/login", json=login_payload, headers=headers)
        #     print("Login response:", response_login.text, response_login.status_code)

        #     assert response_login.status_code == 200

    def generate_random_username(self):
        return ''.join(random.choice(string.ascii_letters) for _ in range(8))
