"""
30. Validar longitud de contraseña
La contraseña debe tener al menos 8 caracteres.


"""
contra = (input("ingresa tu contraseña:"))

print(len(contra))

if  not contra < 8:
    print("la contra cumple con los digitos")
else:
    print("no cumple con los 8 digitos")