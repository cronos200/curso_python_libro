import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
usuarios = response.jhon()

for usuario in usuarios:
    nombre = usuario['name']
    correo = usuario['email']
    print(f'El nombre del usuario es {nombre} y su correo es {correo}')