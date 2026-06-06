frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

contador = 0

for caracter in frase:

    if caracter == letra:
        contador = contador + 1

print("La letra aparece", contador, "veces")