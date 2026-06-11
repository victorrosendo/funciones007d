#Funciones
def mostrar_encabezado():
    print("======================")
    print("|| Sistema de Admisión Escolar ||")
    print("======================")

def solicitar_datos():
    estudiantes = {}
    estudiantes["rut"] = input("Ingrese el rut del estudiante: ")
    estudiantes["nombre"] = input("Ingrese el nombre del estudiante: ")
    estudiantes["carrera"] = input("Ingrese la carrera que estudia: ")
    while True:
        try:
            estudiantes["semestre"] = int(input("Ingrese el semestre que cursa: "))
            if estudiantes["semestre"] < 1 or estudiantes["semestre"] > 4:
                print("Debe ser del 1 al 4")
            else:
                break
        except ValueError:
            print("Debe ingresar un número")
    return estudiantes

def mostrar_datos(alumnos):
    print(f"Nombre del Estudiante: {alumnos["nombre"]}")
    print(f"Rut del Estudiante: {alumnos["rut"]}")
    print(f"Carrera del Estudiante: {alumnos["carrera"]}")
    print(f"Semestre del Estudiante: {alumnos["semestre"]}")

#Código Principal
datos = solicitar_datos()
#imprimir el encabezado
mostrar_encabezado()
mostrar_datos(datos)
