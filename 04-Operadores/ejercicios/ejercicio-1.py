"""

1. Potencia de números
Crea un programa que pida dos números y muestre:
- El resultado de elevar el primer número al segundo
- El resultado de elevar el segundo número al primero

"""
num1 =float(input("ingresa un número:"))
num2 =float(input("ingresa otro número:"))

x = num1 ** num2

d = num2 ** num1

print(f"el primer número elevando al segundo es {x} y el segundo número elevado al primero es {d}")