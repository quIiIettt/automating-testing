import requests
import pytest

def test_get_user():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)

    assert response.status_code == 200, "Статус код відповіді не є 200"

    try:
        data = response.json()
    except ValueError:
        pytest.fail("Не вдалося розшифрувати відповідь як JSON")

    assert "data" in data, "Ключ 'data' відсутній у відповіді"

    user_data = data["data"]
    assert "id" in user_data, "Поле 'id' відсутнє у відповіді"
    assert "email" in user_data, "Поле 'email' відсутнє у відповіді"
    assert "first_name" in user_data, "Поле 'first_name' відсутнє у відповіді"
    assert "last_name" in user_data, "Поле 'last_name' відсутнє у відповіді"

    print("Дані про користувача:")
    print("ID:", user_data["id"])
    print("Email:", user_data["email"])
    print("Ім'я:", user_data["first_name"])
    print("Прізвище:", user_data["last_name"])

def test_create_user():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "dmytro",
        "job": "leader"
    }
    
    response = requests.post(url, json=payload)

    assert response.status_code == 201, "Статус код відповіді не є 201"

    try:
        data = response.json()
    except ValueError:
        pytest.fail("Не вдалося розшифрувати відповідь як JSON")

    assert "name" in data, "Поле 'name' відсутнє у відповіді"
    assert "job" in data, "Поле 'job' відсутнє у відповіді"
    assert "id" in data, "Поле 'id' відсутнє у відповіді"
    assert "createdAt" in data, "Поле 'createdAt' відсутнє у відповіді"

    print("Створений користувач:")
    print("Ім'я:", data["name"])
    print("Посада:", data["job"])
    print("ID:", data["id"])
    print("Дата створення:", data["createdAt"])

def test_update_user():
    url = "https://reqres.in/api/users/2"
    payload = {
        "name": "dmytro",
        "job": "bro"
    }
   
    response = requests.put(url, json=payload)

    assert response.status_code == 200, "Статус код відповіді не є 200"

    try:
        data = response.json()
    except ValueError:
        pytest.fail("Не вдалося розшифрувати відповідь як JSON")

    assert "name" in data, "Поле 'name' відсутнє у відповіді"
    assert "job" in data, "Поле 'job' відсутнє у відповіді"
    assert "updatedAt" in data, "Поле 'updatedAt' відсутнє у відповіді"

    print("Оновлений користувач:")
    print("Ім'я:", data["name"])
    print("Посада:", data["job"])
    print("Дата оновлення:", data["updatedAt"])

def test_delete_user():
    url = "https://reqres.in/api/users/2"

    response = requests.delete(url)

    assert response.status_code == 204, "Статус код відповіді не є 204"

    print("Користувача успішно видалено")

if __name__ == "__main__":
    pytest.main()