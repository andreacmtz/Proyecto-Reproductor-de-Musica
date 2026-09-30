# simular un cajero automatico
saldo = 10000
contador = 0
while True:
    print("\n1. Depositar")
    print("2. Retirar")
    print("3. Consultar Saldo")
    print("4. Salir")
    opcion = int(input("¿Que opcion deseas realizar? \n"))
    if opcion == 1:
        contador = contador + 1
        cantidad = input("¿Cuanto desea depositar? ")
        saldo  = saldo + int(cantidad)
        print("Saldo actualizado correctamente")
    elif opcion == 2:
        contador = contador + 1
        cantidad = input("¿Cuanto desea retirar? ")
        if int(cantidad) <= saldo:
            saldo = saldo - int(cantidad)
            print("Saldo actualizado correctamente")
        elif int(cantidad) > saldo:
            print("Error, saldo insuficiente")
    elif opcion == 3:
        print(f"Tu saldo es: {saldo} ")
    elif opcion == 4:
        break
    else:
        print("Opcion No Valida")

print("Gracias por utilizar el programa")
print(f"Contador de movimientos: {contador}")