"""
6. Nota aprobatoria
Solicita una nota (0 a 20) y muestra si está aprobado (>=11) o desaprobado.

"""
num1 = int(input("ingrese tu nota:"))

if num1 >= 11 and num1 <= 20:
    print("usted aprobo")
elif num1 >= 0 and num1 <= 10:
    print("usted desaprovo")
else:
    print("ingresa una nota de del 0 al 20")
