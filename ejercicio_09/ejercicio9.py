contador = 1
cantidad = 0

while contador <= 100:

    if contador % 2 != 0:
        print(contador)
        cantidad = cantidad + 1

    contador = contador + 1

print("Cantidad de impares:", cantidad)