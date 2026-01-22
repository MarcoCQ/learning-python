"""
5. Solicita la temperatura en grados y muestra:
   Frío (menor a 15), Templado (15–25) o Caluroso (mayor a 25).

"""
temp = int(input("ingresa los grados de tu temperatura:"))

if temp <= 14:
    input("clima frio")
elif temp >= 15 and temp <= 24:
    input("clima templado")
else:
    input("caluroso")