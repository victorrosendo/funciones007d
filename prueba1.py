#Funciones

#opcion 2
def buscar_mascota(lista_m, nombre_m):
    #recorrer la lista
    for x in range(len(lista_m)):
        #verificando si el nombre coincide
        if nombre_m == lista_m[x]["nombre"]:
            return x #retorno la posición
    #si no lo encuentro
    return -1

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

#opcion 4
def actualizar_vacunas(lista_m):
    #recorrer la lista
    for m in lista_m:
        #validar la edad
        if m["edad"] >= 1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False
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
        print("*** Buscar Mascota ***")
        nombre = input("Ingrese el nombre de la mascota: ")
        posicion = buscar_mascota(lista_mascotas, nombre)
        #validar que devolvio la funcion
        if posicion != -1: #la encontro
            print(f"La posición encontrada es: {posicion + 1}")
            #almacenar el diciconario en una variable
            m = lista_mascotas[posicion]
            print(f"Nombre Mascota: {m["nombre"]}")
            print(f"Especie Mascota: {m["especie"]}")
            print(f"Edad Mascota: {m["edad"]}")
            print(f"Vacunada: {m["vacunada"]}")
        else:
            print("La mascota no se ha encontrado")
    elif op == 3:
        print("*** Eliminar Mascota ***")
        nombre = input("Ingrese el nombre de la mascota a eliminar: ")
        posicion = buscar_mascota(lista_mascotas, nombre)
        #validar que devolvio la funcion
        if posicion != -1: #la encontro
            lista_mascotas.pop(posicion)
            print("La mascota ha sido eliminada de la lista")
        else:
            print(f"La mascota '{nombre}' no se encuentra en la lista")
    elif op == 4:
        actualizar_vacunas(lista_mascotas)
        print("Vacunas actualizadas")
    elif op == 5:
        #actualizar las vacunas
        actualizar_vacunas(lista_mascotas)
        #mostrar los datos de las mascotas
        if len(lista_mascotas) == 0: #lista vacia
            print("No hay mascotas en la lista")
        else:
            print("== Lista de Mascotas ==")
            for m in lista_mascotas:
                print(f"Nombre: {m["nombre"]}")
                print(f"Especie: {m["especie"]}")
                print(f"Edad: {m["edad"]}")
                estado = "AL DÍA" if m["vacunada"] else "PENDIENTE"
                print(f"Estado Vacuna: {estado}")
                print("=========================")
                print()

    elif op == 6:
        print("Gracias por usar el sistema")
    