import requests

respuesta = requests.get("https://catfact.ninja/fact")
datos = respuesta.json()
print(datos["fact"])