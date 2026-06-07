# Programa de impresion de empleados

archivo = open("empleados.txt", "r")

total_empleados = 0
total_mecanicos = 0
total_administrativos = 0
total_casados = 0
total_sueldos = 0

for linea in archivo:

    datos = linea.split(",")

    categoria = datos[2]
    sueldo = float(datos[3])
    estado = datos[5].strip()

    total_empleados = total_empleados + 1

    # Contador de mecanicos y administrativos
    if categoria == "1":
        total_mecanicos = total_mecanicos + 1
    else:
        total_administrativos = total_administrativos + 1

    # Contador de casados
    if estado == "2":
        total_casados = total_casados + 1

    # Acumulador de sueldos
    total_sueldos = total_sueldos + sueldo

archivo.close()

# Impresion final
print("----------------------------------------------")
print("          INFORME DE EMPLEADOS")
print("----------------------------------------------")
print("Total de empleados:           ", total_empleados)
print("Total de mecanicos:           ", total_mecanicos)
print("Total de administrativos:     ", total_administrativos)
print("Total de empleados casados:   ", total_casados)
print("Total de sueldos a pagar:     ", total_sueldos)
print("----------------------------------------------")