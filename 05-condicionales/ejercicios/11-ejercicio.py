"""

11. Clasificación de notas
- 18 a 20: Excelente
- 14 a 17: Bueno
- 11 a 13: Regular
- 0 a 10: Malo

"""
nota = int(input("ingresa tu nota:"))

if nota >= 18 and nota <= 20:
    print("excelente nota")
elif nota >=14 and nota <=17:
    print("buena nota")
elif nota >=11 and nota <= 13:
    print("regular nota")
elif nota >= 0 and nota <= 10:
    print("mala nota")
else:
    print("ingrese una nota en el rango")