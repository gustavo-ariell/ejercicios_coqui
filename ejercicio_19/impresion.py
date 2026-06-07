# Impresion de empleados

archivo = open("empleados.txt", "r")

total_empleados = 0

total_sueldos = 0

total_mecanicos = 0
sueldo_mecanicos = 0

print("PADRON DE EMPLEADOS")
print("--------------------------------------------------------------")
print("Cod.   Nombre y Apellido        Sueldo      Observaciones")
print("--------------------------------------------------------------")

for linea in archivo:

    datos = linea.split(",")

    codigo = datos[0]
    nombre = datos[1]
    sueldo = float(datos[2])
    categoria = datos[3].strip()

    if categoria == "1":
        observacion = "Mecanico"
        total_mecanicos = total_mecanicos + 1
        sueldo_mecanicos = sueldo_mecanicos + sueldo

    else:
        observacion = "Conductor"

    print(codigo, "   ", nombre, "   ", sueldo, "   ", observacion)

    total_empleados = total_empleados + 1
    total_sueldos = total_sueldos + sueldo

print("--------------------------------------------------------------")
print("Total empleados:", total_empleados)

if total_empleados > 0:
    promedio = total_sueldos / total_empleados
    print("Promedio sueldo:", promedio)

if total_mecanicos > 0:
    promedio_mecanicos = sueldo_mecanicos / total_mecanicos
    print("Promedio sueldo mecanico:", promedio_mecanicos)

archivo.close()