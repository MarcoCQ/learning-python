numero = float(input("Ingresa un numero: "))

if numero >= 0 and numero <= 5:
    print("El rango de tu numero es de 0 - 5")
elif numero > 5 and numero <= 10:
    print("El rango de tu numero es de 6 - 10")
elif numero >= 11 and numero <= 15:
    print("El rango de tu numero es de 11 - 15")
else:
    print("El rango de tu numero no esta contemplado.")