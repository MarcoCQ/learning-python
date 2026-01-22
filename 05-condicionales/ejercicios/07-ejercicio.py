"""
7. Edad válida
Valida que la edad no sea negativa ni mayor a 120.

"""
edad = int(input("ingresa tu edad:"))

if edad <= 120 and edad >= 1:
    print("ya estas viejo")
elif edad <= 0:
    print("ingresa bien tu edad")
else:
    print("deberias estar muerto")