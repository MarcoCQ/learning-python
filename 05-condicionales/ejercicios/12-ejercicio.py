"""

12. Semáforo
Solicita un color (rojo, amarillo, verde) y muestra la acción correspondiente.

"""
semá = input("ingrese el color del semáforo:")

if semá == "rojo":
    print("detengase")
elif semá == "amarillo":
    print("espere")
elif semá == "verde":
    print("avanze")
else:
    print("ingrese el color que esta en el semáforo")