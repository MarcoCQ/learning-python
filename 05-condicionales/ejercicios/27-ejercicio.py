"""
27. Validar acceso por horario
Solicita la hora (0 a 23) y permite acceso solo de 8 a 18.

"""

hor = int(input("ingresas la hora:"))

if hor >=0 and hor <=7:
    print("acceso no permitido")
elif hor >= 8 and hor <=18:
    print("acceso permitido")
elif hor >= 19 and hor <=3:
    print("acceso no permitido")
else:
    print("ingresa un hora correcta")