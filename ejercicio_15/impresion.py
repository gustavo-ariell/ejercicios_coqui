archivo = open("alumnos.txt", "r")

cantidad_alumnos = 0
cantidad_varones = 0
cantidad_mujeres_solteras = 0

for linea in archivo:

    datos = linea.split(",")

    edad = datos[0]
    sexo = datos[1]
    estado_civil = datos[2]
    nombre = datos[3]

    cantidad_alumnos = cantidad_alumnos + 1

    if sexo == "1":
        cantidad_varones = cantidad_varones + 1

    if sexo == "2" and estado_civil == "1":
        cantidad_mujeres_solteras = cantidad_mujeres_solteras + 1

archivo.close()

print("Cantidad de alumnos:", cantidad_alumnos)
print("Cantidad de varones:", cantidad_varones)
print("Cantidad de mujeres solteras:", cantidad_mujeres_solteras)