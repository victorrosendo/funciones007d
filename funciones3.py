#Funciones
def ficha_producto(nombre, precio, stock): #no importa el orden de los parametros
    print("====================")
    print(f"||Nombre del Producto: {nombre} ||")
    print(f"||Stock del Producto: {stock} ||")
    print(f"||Precio del Producto: {precio} ||")
    print("====================")

#Código Principal
nombre1 = input("Ingrese el nombre del producto: ")
while True:
    try:
        stock1 = int(input("Ingrese el stock: "))
        if stock1 < 0:
            print("Debe ser mayor o igual a cero")
        else:
            break
    except ValueError:
        print("Debe ingresar números")

while True:
    try:
        precio1 = int(input("Ingrese el precio: "))
        if precio1 <= 0:
            print("Debe ser un número positivo")
        else:
            break
    except ValueError:
        print("Debe ingresar números")
        
ficha_producto(nombre1, precio1, stock1) #debemos enviarlo en el mismo orden que los creamos en la función
