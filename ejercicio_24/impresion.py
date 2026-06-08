# Programa de impresion de votos

archivo = open("votos.txt", "r")

total_personas = 0
total_si = 0
total_no = 0
total_abstuvo = 0

print("LISTA DE VOTOS")
print("-" * 40)
print("Nombre\t\tVoto")
print("-" * 40)

for linea in archivo:

    datos = linea.split(",")

    nombre = datos[0]
    voto = datos[1].strip()

    print(nombre, "\t\t", voto)

    total_personas = total_personas + 1

    if voto == "SI":
        total_si = total_si + 1

    if voto == "NO":
        total_no = total_no + 1

    if voto == "SE ABSTUVO":
        total_abstuvo = total_abstuvo + 1

archivo.close()

print("-" * 40)
print("Total de personas que votaron:", total_personas)
print("Total de personas que dijeron SI:", total_si)
print("Total de personas que dijeron NO:", total_no)
print("Total de personas que se abstuvieron:", total_abstuvo)