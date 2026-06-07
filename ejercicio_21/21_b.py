# -----------------------------------
# PROGRAMA DE IMPRESION
# -----------------------------------

archivo = open("articulos.txt", "r")

print("INFORME DE ARTICULOS")
print("-" * 70)

print(f"{'CODIGO':<10}{'ARTICULO':<20}{'ENTRADA':<10}{'SALIDA':<10}{'TOTAL':<10}")

total_entradas = 0
total_salidas = 0

for linea in archivo:

    datos = linea.strip().split(",")

    codigo = datos[0]
    articulo = datos[1]
    entrada = int(datos[3])
    salida = int(datos[4])

    total = entrada - salida

    print(f"{codigo:<10}{articulo:<20}{entrada:<10}{salida:<10}{total:<10}")

    total_entradas = total_entradas + entrada
    total_salidas = total_salidas + salida

print("-" * 70)
print("TOTAL ENTRADAS:", total_entradas)
print("TOTAL SALIDAS:", total_salidas)

archivo.close()