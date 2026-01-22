"""
32. Validar tipo de triángulo
Según sus lados:
- Equilátero
- Isósceles
- Escaleno

"""
lad = int(input("ingresa los lados iguales de tu triangulo:"))

if lad == 3:
    print("es un triangulo equilatero")
elif lad == 2:
    print("es un triangulo isóceles")
elif lad == 0:
    print("es un triangulo escaleno")
else:
    print("ingresa los lados iguales de un triangulo correctamente ")

