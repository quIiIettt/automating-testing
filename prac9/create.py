import requests

url = "https://reqres.in/api/users"
payload = {
    "name": "dmytro",
    "job": "leader"
}
    
response = requests.post(url, json=payload)

assert response.status_code == 201, "Статус код відповіді не є 201"

data = response.json()

assert "name" in data, "Поле 'name' відсутнє у відповіді"
assert "job" in data, "Поле 'job' відсутнє у відповіді"
assert "id" in data, "Поле 'id' відсутнє у відповіді"
assert "createdAt" in data, "Поле 'createdAt' відсутнє у відповіді"

print("Створений користувач:")
print("Ім'я:", data["name"])
print("Посада:", data["job"])
print("ID:", data["id"])
print("Дата створення:", data["createdAt"])