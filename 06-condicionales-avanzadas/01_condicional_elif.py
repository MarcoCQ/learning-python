"""

    Condicional avanzada:

    elif: se usa cuando quieres probar varias condiciones de manera secuencial.

"""


# if condicion1:
#     código si condicion1 es True
# elif condicion2:
#     código si condicion2 es True
# else:
#     código si ninguna condición anterior es True

# Ejemplo 1:

edad = 12
texto = ""

if edad < 13:
    texto = "Niño"
elif edad < 20:
    texto ="Adolecente"
else:
    texto ="Adulto"

print(texto)