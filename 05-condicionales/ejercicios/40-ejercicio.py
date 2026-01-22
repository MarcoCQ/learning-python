"""
40. Validar saldo bancario
Si el saldo es negativo, mostrar alerta; si es cero, saldo en cero; si es positivo, saldo disponible.

"""
sal = float(input("ingresa tu saldo bancario:"))

if sal <= -1:
    print("alerta")
elif sal == 0:
    print("saldo en 0")
else:
    print("saldo disponible")