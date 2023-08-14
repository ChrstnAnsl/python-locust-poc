import pytest
from locust.main import main

def test_spike_user():
    # Run the locust load test
    main("-f main.py".split())

if __name__ == "__main__":
    pytest.main(["-s", "test_spike_user.py"])
