# Carga de empleados

archivo = open("empleados.txt", "a")

continuar = "S"

while continuar == "S":

    cod = input("Codigo de empleado: ")
    nombre = input("Nombre y apellido: ")
    categoria = input("Categoria: ")
    fecha_ing = input("Fecha de ingreso: ")
    fecha_baja = input("Fecha de baja: ")
    sueldo = float(input("Sueldo basico: "))

    registro = cod + ";" + nombre + ";" + categoria + ";" + fecha_ing + ";" + fecha_baja + ";" + str(sueldo)

    archivo.write(registro + "\n")

    continuar = input("Desea cargar otro empleado? (S/N): ")
    continuar = continuar.upper()

archivo.close()

print("Archivo generado correctamente.")