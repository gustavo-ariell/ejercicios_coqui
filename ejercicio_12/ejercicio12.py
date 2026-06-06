contador = 1
suma_pares = 0
suma_impares = 0

while contador <= 100:

    print(contador)

    if contador % 2 == 0:
        suma_pares = suma_pares + contador
    else:
        suma_impares = suma_impares + contador

    contador = contador + 1

print("Suma de pares:", suma_pares)
print("Suma de impares:", suma_impares)