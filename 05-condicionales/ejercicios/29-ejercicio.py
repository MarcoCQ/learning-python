"""
29. 29. Validar nombre no vacío
Solicita un nombre y valida que no esté vacío.

"""
nom = input("ingresa tu nombre:")

print(len(nom))

if not nom:
    print("esta vacio")


