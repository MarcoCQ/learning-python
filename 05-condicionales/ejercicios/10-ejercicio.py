"""

10. Acceso a sistema
Solicita usuario y contraseña y valida el acceso.


"""
usu = input("ingresa tu usuario:")
contra = input("ingresa tu contraseña:")

if usu == "marco" and contra == "gatito":
    print("acseso concedido")
else:
    print("intatenta otra vez")