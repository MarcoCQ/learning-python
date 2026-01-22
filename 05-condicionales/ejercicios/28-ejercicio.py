"""
28. Sistema de calificación con letras
- A: 18 a 20
- B: 14 a 17
- C: 11 a 13
- D: 0 a 10

"""
let = int(input("ingresa tu califiación:"))

if let >= 0 and let <= 10:
    print("promedio D")
elif let >= 11 and let <= 13:
    print("promedio C")
elif let >= 14 and let <= 17:
    print("promedio B")
elif let >= 18 and let <= 20:
    print("promedio A")
else:
    print("ingrese una calificación en el rango establecido")
