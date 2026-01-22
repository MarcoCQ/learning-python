"""

22. Validar promedio de 3 notas
Solicita tres notas y muestra si el alumno aprueba (promedio >= 11).

"""
not1 = int(input("ingresa la primera nota:"))
not2 = int(input("ingresa la segunda nota:"))
not3 = int(input("ingresa la tercera nota:"))

x = (not1 + not2 + not3)/3

if x >= 0 and x <= 10:
    print("estas aprovado")
elif x >= 11 and x <= 20:
    print("estas desaprobado")
else:
    print("ingresa una nota en el rango establecido")
