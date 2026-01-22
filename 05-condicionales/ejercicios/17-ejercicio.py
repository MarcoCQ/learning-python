"""
17. Hora del día
Solicita una hora (0 a 23) y muestra:
- Mañana
- Tarde
- Noche

"""
hor = int(input("ingresa la hora:"))

if hor >= 0 and hor <= 11:
    print("horario mañana")
elif hor >= 12 and hor <= 17:
    print("horario tarde")
elif hor >= 18 and hor <= 23:
    print("horario nocturno")
else:
    print("ingresa una hora correcta")