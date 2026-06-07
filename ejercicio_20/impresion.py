# Informe de empleados dados de baja

archivo = open("empleados.txt", "r")

linea = archivo.readline()

cont = 0
total = 0

def titulo():
    print()
    print("INFORME DE EMPLEADOS DADOS DE BAJA")
    print("-" * 60)
    print("Cod. Empl.   Nombre y Apellido              Sueldo Basico")
    print("-" * 60)

titulo()

while linea != "":

    datos = linea.strip().split(";")

    cod = datos[0]
    nombre = datos[1]
    fecha_baja = datos[4]
    sueldo = float(datos[5])

    # Se imprime solo si tiene fecha de baja
    if fecha_baja != "":

        print(f"{cod:10} {nombre:30} {sueldo:12.2f}")

        total = total + sueldo
        cont = cont + 1

        # Titulo cada 70 renglones
        if cont % 70 == 0:
            titulo()

    linea = archivo.readline()

archivo.close()

print("-" * 60)
print("TOTAL                :", cont)
print("TOTAL GENERAL        :", total)

if cont > 0:
    promedio = total / cont
else:
    promedio = 0

print("DIFERENCIA           :", total - promedio)