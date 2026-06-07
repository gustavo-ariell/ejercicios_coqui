archivo = open("alumnos.txt", "r")

cantidad_mujeres_20_30 = 0
cantidad_mujeres_casadas_30_40 = 0
cantidad_mujeres_casadas = 0
cantidad_varones = 0
cantidad_varones_solteros_25 = 0
cantidad_varones_casados = 0

for linea in archivo:

    datos = linea.split(",")

    edad = int(datos[0])
    sexo = datos[1]
    estado_civil = datos[2]
    nombre = datos[3]

    # a) Cantidad de mujeres entre 20 y 30 años
    if sexo == "2" and edad >= 20 and edad <= 30:
        cantidad_mujeres_20_30 = cantidad_mujeres_20_30 + 1

    # b) Cantidad de mujeres casadas entre 30 y 40 años
    if sexo == "2" and estado_civil == "2" and edad >= 30 and edad <= 40:
        cantidad_mujeres_casadas_30_40 = cantidad_mujeres_casadas_30_40 + 1

    # c) Cantidad de mujeres casadas
    if sexo == "2" and estado_civil == "2":
        cantidad_mujeres_casadas = cantidad_mujeres_casadas + 1

    # d) Total de varones
    if sexo == "1":
        cantidad_varones = cantidad_varones + 1

    # e) Total de varones solteros con edad de 25 años
    if sexo == "1" and estado_civil == "1" and edad == 25:
        cantidad_varones_solteros_25 = cantidad_varones_solteros_25 + 1

    # f) Total de varones casados
    if sexo == "1" and estado_civil == "2":
        cantidad_varones_casados = cantidad_varones_casados + 1

archivo.close()

print("Cantidad de mujeres entre 20 y 30 años:", cantidad_mujeres_20_30)
print("Cantidad de mujeres casadas entre 30 y 40 años:", cantidad_mujeres_casadas_30_40)
print("Cantidad de mujeres casadas:", cantidad_mujeres_casadas)
print("Total de varones:", cantidad_varones)
print("Total de varones solteros con 25 años:", cantidad_varones_solteros_25)
print("Total de varones casados:", cantidad_varones_casados)