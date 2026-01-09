"""
    Ejercicio: Calculadora simple

    Desarrolla un programa en Python que solicite al usuario ingresar dos números.
    El programa debe realizar las siguientes operaciones matemáticas con dichos números:

    -   Suma
    -   Resta
    -   Multiplicación
    -   División

    Finalmente, el programa debe mostrar en pantalla el resultado de cada operación.

    📝 Recomendación

    Utiliza la función input() para capturar los datos y convierte 
    los valores a tipo numérico para poder realizar los cálculos correctamente.

    str()
    float()
    int()

"""
num1 = float(input("ingrese el primer número:"))
num2 = float(input("ingrese el segundo número:"))

sm = num1 + num2
rs = num1 - num2
mt = num1 * num2
dv = num1 / num2

print(f"la respuesta de la suma es {sm}, de la resta es {rs}, de la multiplicación es {mt} y de la división es {dv}")





