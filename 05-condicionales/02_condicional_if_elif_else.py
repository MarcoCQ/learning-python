numero1 = float(input("Ingresa su primero numero: "))
numero2 = float(input("Ingresa su segundo numero: "))

if numero1 > numero2: # Si esta condicion cumple
    print(f"El numero 1 es mayor: {numero1}")
elif numero2 > numero1: # Se evalúa solo si el if o el elif anterior no cumple
    print(f"El numero 2 es mayor: {numero2}")
elif numero2 == 1:
    print("Es uno")
else: # Si no cumple las condiciones
    print("Los numeros son iguales.")