# Programa de carga de empleados

archivo = open("empleados.txt", "a")

continuar = "s"

while continuar == "s":

    codigo = input("Ingrese codigo de empleado: ")
    nombre = input("Ingrese nombre y apellido: ")

    print("Categoria:")
    print("1 - Mecanico")
    print("2 - Administrativo")
    categoria = input("Ingrese categoria: ")

    sueldo = input("Ingrese sueldo basico: ")

    print("Sexo:")
    print("1 - Masculino")
    print("2 - Femenino")
    sexo = input("Ingrese sexo: ")

    print("Estado Civil:")
    print("1 - Soltero")
    print("2 - Casado")
    estado = input("Ingrese estado civil: ")

    # Guardar datos en el archivo
    linea = codigo + "," + nombre + "," + categoria + "," + sueldo + "," + sexo + "," + estado + "\n"

    archivo.write(linea)

    continuar = input("Desea cargar otro empleado? (s/n): ")

archivo.close()

print("Datos guardados correctamente")