"""
35. Validar consumo eléctrico
- Bajo: <100 kWh
- Medio: 100–300 kWh
- Alto: >300 kWh


"""
consu = int(input("ingresa tu consumo electrico:"))

if consu >= 0 and consu <= 99:
    print("el consumo es bajo")
elif consu >= 100 and consu <= 299:
    print("el consumo es medio")
elif consu > 300:
    print("el consumo es alto")
else:
    print("ingresa un consumo valido")