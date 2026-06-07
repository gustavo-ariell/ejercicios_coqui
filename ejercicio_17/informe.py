# Programa de impresion de mercaderia

archivo = open("mercaderia.txt", "r")

total_entrada = 0
total_salida = 0
total_diferencia = 0

print("---------------------------------------------")
print(" INFORME DE OPERACIONES CON MERCADERIA")
print("---------------------------------------------")

for linea in archivo:

    datos = linea.split(",")

    codigo = datos[0]
    descripcion = datos[1]
    entrada = int(datos[3])
    salida = int(datos[4])

    diferencia = entrada - salida

    total_entrada = total_entrada + entrada
    total_salida = total_salida + salida
    total_diferencia = total_diferencia + diferencia

    print("Codigo: ", codigo)
    print("Descripcion: ", descripcion)
    print("Entrada: ", entrada)
    print("Salida: ", salida)
    print("Diferencia: ", diferencia)
    print("---------------------------------------------")

archivo.close()

print("TOTALES")
print("Total entradas: ", total_entrada)
print("Total salidas: ", total_salida)
print("Total diferencia: ", total_diferencia)
print("---------------------------------------------")