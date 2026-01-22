"""
4. Pide el sueldo mensual e indica si es:
   Bajo (menos de 1500), Medio (1500–3000) o Alto (más de 3000).

"""

suel = int(input("ingresa tu sueldo:"))

if suel >= 0 and suel <= 1499:
    input("tu sueldo es bajo")
elif suel >= 1500 and suel <= 2999:
    input("sueldo medio")
elif suel >= 3000:
    input("sueldo alto")
else:
    input("ingresa un sueldo real")