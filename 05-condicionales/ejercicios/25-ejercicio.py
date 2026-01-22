"""
25. Validar descuento por monto de compra
Si el monto es mayor o igual a 500, aplica descuento; si no, no aplica.

"""
comp = int(input("ingresa el monto de tu compra:"))

if comp >= 500: 
    print("aplica descuento")
else:
    print("no aplica descuento")