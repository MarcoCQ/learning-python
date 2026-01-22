"""
36. Validar año dentro de rango
Valida que el año esté entre 1900 y 2100.

"""
año = int(input("ingresa un año:"))

if año >= 1900 and año <= 2100:
    print("tu año esta en el rango correspondiente")
else:
    print("tu año no esta en el rango correspondiente")