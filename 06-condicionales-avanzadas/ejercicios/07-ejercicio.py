"""
Solicita una calificación en letras (A, B, C, D, F) y muestra su equivalencia en texto

"""
cali = input("ingrsa tu calificación:")

if cali == "A":
    print("destacado")
elif cali == "B":
    print("muy bien")
elif cali == "C":
    print("bien")
elif cali == "D":
    print("mal")
elif cali == "F":
    print("muy mal")
else:
    print("ingresa una nota desde la A hasta la F")