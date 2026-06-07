# -----------------------------------
# PROGRAMA DE CARGA DE DATOS
# -----------------------------------

archivo = open("articulos.txt", "a")

seguir = "S"

while seguir == "S":

    codigo = input("Ingrese código del artículo: ")
    descripcion = input("Ingrese descripción: ")
    precio = float(input("Ingrese precio unitario: "))
    entrada = int(input("Ingrese cantidad de entrada: "))
    salida = int(input("Ingrese cantidad de salida: "))

    # Guardar datos en el archivo
    archivo.write(codigo + ",")
    archivo.write(descripcion + ",")
    archivo.write(str(precio) + ",")
    archivo.write(str(entrada) + ",")
    archivo.write(str(salida) + "\n")

    seguir = input("Desea cargar otro artículo? (S/N): ")

archivo.close()

print("Datos guardados correctamente")