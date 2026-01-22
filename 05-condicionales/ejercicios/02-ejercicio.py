"""
2. Número positivo o negativo
Pide un número y muestra si es positivo, negativo o cero.

"""
num = int(input("ingresa un número:"))

if num > 0:
    print("el número es positivo")
elif num < 0:
    print("el número es negativo")
else:
    print("el número es cero")