#Funciones
def conversion_notas(puntaje, puntaje_total):
    nota = (puntaje * 6 / puntaje_total) + 1
    return round(nota,1)

#Código Principal
while True:
    try:
        p = float(input("Ingrese la nota del estudiante: "))
        if p < 0:
            print("Debe ser una nota positiva")
        else:
            break
    except ValueError:
        print("Debe ingresar un número")

while True:
    try:
        pt = float(input("Ingrese la nota total de la evaluación: "))
        if pt < 0:
            print("Debe ser una nota positiva")
        else:
            break
    except ValueError:
        print("Debe ingresar un número")
#llamar a la funcion, enviar datos y mostrar la nota convertida
calif = conversion_notas(p,pt)
print(f"La nota chilena es: {calif}")