"""
6. Pide un número del 1 al 7 y muestra el día de la semana correspondiente.

"""

num = int(input("ingresa un número del 1 al 7:"))

if num == 1: 
    print("es lunes")
elif num == 2:
    print("es martes")
elif num == 3:
    print("es miercoles")
elif num == 4:
    print("es jueves")
elif num == 5:
    print("es viernes")
elif num == 6:
    print("es sabado")
elif num == 7:
    print("es domingo")
else:
    print("ingresa un número en el rango puesto")
