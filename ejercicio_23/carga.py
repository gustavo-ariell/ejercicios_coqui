# Programa de carga de datos de lectores de diarios

archivo = open("lectores.txt", "a")

opcion = "s"

while opcion == "s":

    nombre = input("Ingrese nombre de la persona: ")

    diario_a = input("Lee diario A? (s/n): ")
    diario_b = input("Lee diario B? (s/n): ")
    diario_c = input("Lee diario C? (s/n): ")

    # Guardar datos en el archivo
    linea = nombre + "," + diario_a + "," + diario_b + "," + diario_c + "\n"

    archivo.write(linea)

    opcion = input("Desea cargar otra persona? (s/n): ")

archivo.close()

print("Datos guardados correctamente")