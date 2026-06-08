# Programa de impresion de datos

archivo = open("lectores.txt", "r")

leen_tres = 0
no_leen_ninguno = 0
leen_a = 0
no_leen_a_pero_otro = 0

for linea in archivo:

    datos = linea.split(",")

    nombre = datos[0]
    diario_a = datos[1]
    diario_b = datos[2]
    diario_c = datos[3].strip()

    # g) Leen los tres diarios
    if diario_a == "s" and diario_b == "s" and diario_c == "s":
        leen_tres = leen_tres + 1

    # h) No leen ningun diario
    if diario_a == "n" and diario_b == "n" and diario_c == "n":
        no_leen_ninguno = no_leen_ninguno + 1

    # i) Leen diario A
    if diario_a == "s":
        leen_a = leen_a + 1

    # j) No leen A pero si otro
    if diario_a == "n" and (diario_b == "s" or diario_c == "s"):
        no_leen_a_pero_otro = no_leen_a_pero_otro + 1

archivo.close()

print("RESULTADOS")
print("-----------------------------")
print("Leen los tres diarios:", leen_tres)
print("No leen ningun diario:", no_leen_ninguno)
print("Leen diario A:", leen_a)
print("No leen A pero si otro:", no_leen_a_pero_otro)