# Programa de carga de votos

archivo = open("votos.txt", "a")

opcion = "s"

while opcion == "s":

    nombre = input("Ingrese nombre de la persona: ")
    voto = input("Ingrese voto (SI / NO / SE ABSTUVO): ")

    # Guardar datos en el archivo
    linea = nombre + "," + voto + "\n"

    archivo.write(linea)

    opcion = input("Desea cargar otro voto? (s/n): ")

archivo.close()

print("Datos guardados correctamente")