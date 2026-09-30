import json

try:
    with open("playlist.json", "r") as archivo:
        mi_playlist = json.load(archivo)
except FileNotFoundError:
    mi_playlist = []

num = input("¿Cuantas canciones desea agregar? ")
for i in range(int(num)):
    cancion = input("¿Que cancion deseas agregar? ")
    mi_playlist.append(cancion)

for i in range(len(mi_playlist)):
    print(f"{i+1}. {mi_playlist[i]}")

while True:
    respuesta = input("¿Deseas quitar alguna cancion? ").lower()
    if respuesta == "no":
        print("Entendido, Nos vemos! ")
        break
    elif respuesta == "si":
        delete = input("¿Que numero deseas eliminar? ").lower()
        if delete == "todo":
            mi_playlist = []
            print("Playlist Vacia.")
            continue
        reem = input("¿Deseas reemplazarlo por otra cancion? ").lower()
        if reem == "si":
            reemplazo = input("¿Que cancion deseas agregar? ")
            inciso = int(delete) - 1
            mi_playlist[inciso] = reemplazo 
        elif reem == "no":
            mi_playlist.pop(int(delete)-1)
        else:
            print("Intenta de nuevo. Escribe Si/No")

        for i in range(len(mi_playlist)):
            print(f"{i+1}. {mi_playlist[i]}")
    else:
        print("Intenta de nuevo. Escribe Si/No o todo")


print("Gracias por utilizar el programa")
    
with open("playlist.json", "w") as archivo:
    json.dump(mi_playlist, archivo)
