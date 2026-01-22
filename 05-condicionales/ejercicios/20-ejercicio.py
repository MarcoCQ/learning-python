"""
20. Sistema de multas
Según la velocidad:
- Hasta 60 km/h: Sin multa
- 61 a 80 km/h: Multa leve
- Más de 80 km/h: Multa grave

"""
vel = float(input("ingresa el km/h:"))

if vel >= 0 and vel <= 60:
    print("sin multa")
elif vel >= 61 and vel <= 80:
    print("multa leve")
else:
    print("multa grave")
