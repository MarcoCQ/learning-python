"""
33. Validar división segura
Evita dividir entre cero.

"""
num1 = float(input("ingresa el primer número:"))
num2 = float(input("ingresa el segundo número"))

if num2 == 0:
    print("error")
else:
    x = num1 / num2
    print(f"la divison es {x}")
