"""
31. Validar número mayor entre tres números
Solicita tres números y muestra el mayor.


"""

num1 = int(input("ingresa el primer número:"))
num2 = int(input("ingresa el segundo número:"))
num3 = int(input("ingresa el tercer número:"))

if num1 > num2 and num1 > num3:
    print("el primer número es mayor")
if num2 > num1 and num2 > num3:
    print("el segundo número es meyor")
else:
    print("el tercer número es mayor")