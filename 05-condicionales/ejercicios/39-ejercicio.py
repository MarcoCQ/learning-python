"""
39. Validar tipo de usuario
- admin → acceso total
- usuario → acceso limitado
- invitado → solo lectura


"""

usu = input("ingresa tu usuario:")

if usu == "admin":
    print("acceso total")
elif usu == "usuario":
    print("acceso limitado")
elif usu == "invitado":
    print("solo lectura")
else:
    print("ingrese un usuario correspondiente")