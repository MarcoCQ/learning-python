"""

2. Crea un programa que pida la edad de una persona y muestre si es:
   Niño (menor de 12), Adolescente (12–17), Adulto (18–59) o Adulto mayor (60 o más).

"""
edad = int(input("ingresa tu edad:"))

if edad >= 0 and edad <= 11:
   print("eres un niño")
elif edad >=12 and edad <= 17:
   print("eres un adolescente")
elif edad >= 18 and edad <=59:
   print("eres un adulto")
elif edad >= 60:
   print("eres un adulto mayor")
else:
   print("ingresa una edad real")