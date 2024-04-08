import requests

url = "https://reqres.in/api/users/2"
payload = {
    "name": "dmytro",
    "job": "bro"
}
   
response = requests.put(url, json=payload)

assert response.status_code == 200, "Статус код відповіді не є 200"

data = response.json()

assert "name" in data, "Поле 'name' відсутнє у відповіді"
assert "job" in data, "Поле 'job' відсутнє у відповіді"
assert "updatedAt" in data, "Поле 'updatedAt' відсутнє у відповіді"

print("Оновлений користувач:")
print("Ім'я:", data["name"])
print("Посада:", data["job"])
print("Дата оновлення:", data["updatedAt"])