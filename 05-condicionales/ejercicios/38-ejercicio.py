"""

38. Validar estado civil
Solicita el estado civil (soltero, casado, viudo, divorciado).

"""
civil = input("ingresa tu estado civil:")

if civil == "soltero":
    print("su estado civil es soltero")
elif civil == "casado":
    print("tu estado civil es casado")
elif civil == "viudo":
    print("tu estado civil es viudo")
elif civil == "divorciado":
    print("tu estado cicil es divorsiado")
else:
    print("ingresa tu estado civil correctamente")
