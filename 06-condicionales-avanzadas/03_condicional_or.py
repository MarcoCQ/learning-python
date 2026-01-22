"""

    Los operadores lógicos permiten combinar condiciones:

    or: Verdadero si al menos una de las condiciones es verdadera.

"""

nota = 80
examen_recuperacion = False

if nota >= 70 or examen_recuperacion:
    print("Aprobado")
else:
    print("Reprobado")