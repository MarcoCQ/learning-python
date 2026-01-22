"""
26. Validar número múltiplo de 3 y 5
Indica si el número es múltiplo de 3, de 5, de ambos o de ninguno.

"""

num = int(input("ingresa un número:"))

if num % 3 == 0:
    print("es multiplo de 3")
elif num % 5 ==0:
    print("es multiplo de 5")
elif num % 3 == 0 and num % 5 == 0:
    print("es multiplo de ambos")
else:
    print("no es multiplo de ninguno")
