"""
18. Tarifa de transporte
Según la edad:
- Menor de 12: Niño
- 12 a 59: Adulto
- 60 o más: Adulto mayor

"""
edad = int(input("ingresa tu edad:"))

if edad >= 0 and edad <= 11:
    print("eres niño")
elif edad >= 12 and edad <= 59:
    print("eres adulto")
elif edad >= 60 and edad <= 120:
    print("adulto mayor")
else:
    print("ingresa una edad real")
