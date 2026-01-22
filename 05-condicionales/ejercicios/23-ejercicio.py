"""
23. Validar acceso por edad y DNI
Permite el acceso solo si la edad es mayor o igual a 18 y tiene DNI.

"""
dni = int(input("ingresa tu dni:"))
edad = int(input("ingresa tu edad:"))

print(len(dni))

if  not dni == 8:
    print(f"dni valido{dni}")
elif edad >=18:
    print("acseso perimitido")
else:
    print("edad o dni no valida")



