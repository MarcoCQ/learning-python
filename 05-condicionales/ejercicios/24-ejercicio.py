"""
24. Clasificar temperatura
Según el valor:
- Menor a 10: Frío
- 10 a 25: Templado
- Mayor a 25: Caliente

"""

temp =  int(input("ingrese la temperatura:"))

if temp <= 9:
    print("hace frio")
elif temp >= 10 and temp <= 24:
    print("esta templado")
else: 
    print("esta caleinte")