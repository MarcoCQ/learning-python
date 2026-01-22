"""
15. Calculadora básica
Solicita dos números y una operación (+, -, *, /) y muestra el resultado.

"""
num1 = float(input("ingrese le primer número:"))
num2 = float(input("ingrese el segundo número:"))
oper = input("ingrese la operación que quiere realizar:")

if oper == "+":
    suma = num1 + num2 
    print(f"la suma es: {suma}")
elif oper == "-":
    rs = num1 - num2
    print(f"la resta es: {resta}")
elif oper == "*":
    mt = num1 * num2
    print(f"la multiplicación es: {mt}")
elif oper == "/":
    dv = num1 / num2
    print(f"la división es {dv}")
else:
    print("operación no registrada")

