"""
3. Solicita un número entero e indica si es positivo, negativo o cero.


"""
num = int(input("ingresa un número:"))

if num <= 1:
    input("es un número negativo")
elif num == 0:
    input("es cero")
else:
    input("es un número positivo")