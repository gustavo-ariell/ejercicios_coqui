# Programa de carga de mercaderia

archivo = open("mercaderia.txt", "a")

continuar = "s"

while continuar == "s":

    codigo = input("Ingrese codigo del articulo: ")
    descripcion = input("Ingrese descripcion del articulo: ")
    precio = input("Ingrese precio unitario: ")
    entrada = input("Ingrese cantidad de entrada: ")
    salida = input("Ingrese cantidad de salida: ")

    # Guardar datos en el archivo
    linea = codigo + "," + descripcion + "," + precio + "," + entrada + "," + salida + "\n"

    archivo.write(linea)

    continuar = input("Desea cargar otro articulo? (s/n): ")

archivo.close()

print("Datos guardados correctamente")