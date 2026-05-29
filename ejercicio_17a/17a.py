# EJERCICIO 17
# Informe de operaciones con mercaderia

# Crear archivo para guardar datos
archivo = open("mae.txt", "w")

# Ingreso de datos
resp = "s"

while resp == "s":

    cod = input("Ingrese codigo de articulo: ")
    desc = input("Ingrese descripcion: ")
    precio = float(input("Ingrese precio unitario: "))
    entrada = int(input("Ingrese entrada: "))
    salida = int(input("Ingrese salida: "))

    # Guardar en el archivo
    archivo.write(cod + "," +
                  desc + "," +
                  str(precio) + "," +
                  str(entrada) + "," +
                  str(salida) + "\n")

    resp = input("Desea ingresar otro articulo? (s/n): ")

archivo.close()

print()
print("ARCHIVO mae.txt GUARDADO")
print()

# -----------------------------------------
# LEER ARCHIVO Y MOSTRAR INFORME
# -----------------------------------------

archivo = open("mae.txt", "r")

# Totales
te = 0
ts = 0
td = 0

print("==============================================")
print("     INFORME DE OPERACIONES CON MERCADERIA")
print("==============================================")
print()

print("Cod\tDesc\t\tEntrada\tSalida\tDiferencia")

for linea in archivo:

    datos = linea.strip().split(",")

    cod = datos[0]
    desc = datos[1]
    precio = float(datos[2])
    entrada = int(datos[3])
    salida = int(datos[4])

    diferencia = entrada - salida

    print(cod, "\t", desc, "\t\t", entrada, "\t", salida, "\t", diferencia)

    # Acumuladores
    te = te + entrada
    ts = ts + salida
    td = td + diferencia

archivo.close()

print("------------------------------------------------")
print("TOTALES\t\t\t", te, "\t", ts, "\t", td)