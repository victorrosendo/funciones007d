#Funciones
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

#Código Principal
#declaro la lista de mascotas
lista_mascotas = []

op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()
