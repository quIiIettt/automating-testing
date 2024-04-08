import requests

url = "https://reqres.in/api/users/2"
response = requests.delete(url)

assert response.status_code == 204, "Статус код відповіді не є 204"

print("Користувача успішно видалено")