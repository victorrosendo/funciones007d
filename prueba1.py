#Funciones
#validaciones
def validar_nombre(name):
    #una funcion de python que elimina los espacios al inicio o al final de un string y si queda vacia devuelve un False
    return name.strip() != "" #Retorna True si es valido - False si es invalido
def validar_especie(especie):
    #verificar que es perro, gato o ave solamente (sin diferenciar mayusculas o minusculas)
    especies_validas = ["perro","gato","ave"]
    return especie.strip().lower() in especies_validas
def validar_edad(edad):
    #que sean numeros y mayor a cero
    #isdigit() --> revisa que el string contenga solo digitos (no negativo, no decimal)
    return edad.isdigit() and int(edad) > 0



def mostrar_menu():
    print("=======Menú Principal=========")
    print("||1.- Agregar Mascota    ||")
    print("||2.- Buscar Mascota    ||")
    print("||3.- Eliminar Mascota    ||")
    print("||4.- Marcar como Vacunada||")
    print("||5.- Mostar Mascotas    ||")
    print("||6.- Salir            ||")
    print("=====================")

def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 6:
                print("Debe seleccionar una opción del 1 al 6")
            else:
                break
        except ValueError:
            print("Debe ingresar un número")
    return opcion
#Funcion para agregar una mascota nueva
def agregar_mascota(lista):
    nombre = input("Ingrese el nombre de la mascota: ")
    #llamar la funcion que valida el nombre para mostrar el mensaje
    correcto = validar_nombre(nombre)
    if not correcto:
        print("El nombre no puede estar vacío")
        return
    
    especie = input("Ingrese la especie de la mascota (perro, gato o ave): ")
    correcto = validar_especie(especie)
    if not correcto:
        print("La especie solo puede ser perro, gato o ave")
        return
    
    edad = input("Ingrese la edad de la mascota: ")
    correcto = validar_edad(edad)
    if not correcto:
        print("La edad debe ser un número entero mayor a cero")
        return
    #aqui agrego al diccionario
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad": int(edad),
        "vacunada": False
    }
    #agrego a la lista
    lista.append(mascota)
    print("Mascota agregada correctamente")

#Código Principal
#declaro la lista de mascotas
lista_mascotas = []

op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()

    if op == 1:
        agregar_mascota(lista_mascotas)
    elif op == 2:
        print()
    elif op == 3:
        print()
    elif op == 4:
        print()
    elif op == 5:
        print()
    elif op == 6:
        print("Gracias por usar el sistema")
    