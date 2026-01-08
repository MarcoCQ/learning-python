"""

    SESION 03: Tipo de concadenación

    Un texto en python se define con '' o "".

"""

# 1. Concadenacion con el operador (+)

nombre = "Deyvids"
apellido = "Alvino"

# Ejemplo 1: Variable
nombre_completo = "Mi nombre es " + nombre + " " + apellido
print(nombre_completo)

# Ejemplo 2: Directo en el print
print(nombre + " " + apellido)

# 2. Concadenación por f-strings

libro = "Clean code"
author = "Marco"
edad = 21

# Ejemplo 1: Variable
texto = f"Hola, soy {author} y tengo {edad} años. Publique el libro {libro}."
print(texto)

# Ejemplo 2: Directo en el print
print(f"Hola, soy {author} y tengo {edad} años. Publique el libro {libro}.")
