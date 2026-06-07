archivo = open("alumnos.txt", "a")

respuesta = "s"

while respuesta == "s":

    edad = input("Ingrese edad: ")
    sexo = input("Ingrese sexo (1=Varon / 2=Mujer): ")
    estado_civil = input("Ingrese estado civil (1=Soltero / 2=Casado): ")
    nombre = input("Ingrese nombre y apellido: ")

    archivo.write(edad + "," + sexo + "," + estado_civil + "," + nombre + "\n")

    respuesta = input("Desea cargar otro alumno? (s/n): ")

archivo.close()

print("Datos guardados correctamente")