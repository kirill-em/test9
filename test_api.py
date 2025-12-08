import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user():
    """Тест 1: GET запрос"""
    url = f"{BASE_URL}/users/1"
    response = requests.get(url)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    json_data = response.json()
    assert json_data['id'] == 1
    assert json_data['username'] == "Bret"
    assert json_data['email'] == "Sincere@april.biz"

def test_create_user():
    """Тест 2: POST запрос"""
    url = f"{BASE_URL}/users"
    payload = {
        "name": "Ivan Ivanov",
        "username": "ivanov",
        "email": "ivan@test.com"
    }
    
    response = requests.post(url, json=payload)

    assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"

    json_data = response.json()
    assert json_data['username'] == "ivanov"
    assert json_data['id'] == 11 

def test_update_user():
    """Тест 3: PUT запрос"""
    url = f"{BASE_URL}/users/1"
    payload = {
        "id": 1,
        "name": "Ivan Updated",
        "username": "Bret",
        "email": "Sincere@april.biz"
    }

    response = requests.put(url, json=payload)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    json_data = response.json()
    assert json_data['name'] == "Ivan Updated"

if __name__ == "__main__":
    pytest.main(["-v", __file__])