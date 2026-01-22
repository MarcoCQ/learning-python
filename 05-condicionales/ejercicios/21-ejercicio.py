"""
21. Validar número mayor, menor o igual a 100
Solicita un número y muestra si es mayor, menor o igual a 100.

"""
num = int(input("ingresa un número:"))

if num <= 99:
    print("es menor a 100")
elif num == 100:
    print("es igual a 100")
else:
    print("el mayor a 100")