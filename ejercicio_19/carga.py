# Carga de empleados

archivo = open("empleados.txt", "a")

respuesta = "s"

while respuesta == "s":

    codigo = input("Ingrese codigo de empleado: ")
    nombre = input("Ingrese nombre y apellido: ")
    sueldo = input("Ingrese sueldo basico: ")
    categoria = input("Ingrese categoria (1=Mecanico / 2=Conductor): ")

    archivo.write(codigo + "," + nombre + "," + sueldo + "," + categoria + "\n")

    respuesta = input("Desea cargar otro empleado? (s/n): ")

archivo.close()

print("Datos guardados correctamente")