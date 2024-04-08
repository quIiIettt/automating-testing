import requests

url = "https://reqres.in/api/users/2"
response = requests.get(url)

assert response.status_code == 200, "Статус код відповіді не є 200"

data = response.json()

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