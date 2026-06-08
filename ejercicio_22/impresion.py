# Programa de impresión de planilla de compras

archivo = open("mercaderia.txt", "r")

contador = 0
total_diferencia = 0

# Título
print("PLANILLA DE COMPRAS")
print("-" * 75)
print("Cod.   Descripcion                 Entrada   Salida   Diferencia")
print("-" * 75)

for linea in archivo:

    datos = linea.split(",")

    codigo = datos[0]
    descripcion = datos[1]
    precio = datos[2]
    entrada = int(datos[3])
    salida = int(datos[4])

    diferencia = entrada - salida

    # Mostrar solo si la diferencia es menor a 5
    if diferencia < 5:

        print(codigo, "   ",
              descripcion.ljust(25),
              str(entrada).ljust(9),
              str(salida).ljust(8),
              diferencia)

        total_diferencia = total_diferencia + diferencia

        contador = contador + 1

        # Cada 70 registros volver a imprimir títulos
        if contador % 70 == 0:

            print()
            print("PLANILLA DE COMPRAS")
            print("-" * 75)
            print("Cod.   Descripcion                 Entrada   Salida   Diferencia")
            print("-" * 75)

print("-" * 75)
print("TOTAL DIFERENCIA:", total_diferencia)

archivo.close()