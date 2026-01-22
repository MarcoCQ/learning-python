"""
1. Desarrolla un programa que solicite una nota (0–100).
   Muestra “Sobresaliente” si la nota es mayor o igual a 90,
   “Notable” si está entre 80 y 89,
   “Bien” si está entre 70 y 79,
   “Suficiente” si está entre 60 y 69,
   y “Insuficiente” si es menor a 60.

"""
nota= int(input("ingresa una nota:"))

if nota >= 0 and nota <= 59:
    print("notas insuficiente")
elif nota >= 60 and nota <= 69:
    print("nota suficiente")
elif nota >= 70 and nota <= 79:
    print("nota buena")
elif nota >= 80 and nota <= 89:
    print("nota notable")
elif nota >= 90:
    print("nota sobresaliente")
else:
    print("ingresa una nota correcta")
