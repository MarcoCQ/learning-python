"""

9. Descuento por edad
Si la edad es mayor o igual a 60, muestra "Descuento aplicado",
caso contrario "No aplica descuento".

"""
edad = int(input("ingresa tu edad"))

if edad >= 60 and edad <= 120:
    print("usted tiene un decuento aplicado")
elif edad <=59 and edad >=1:
    print("usted no recibe descuento")
elif edad <= 0:
    print("ingrese bien su edad")
else:
    print("sigue con vida?")