"""
34. Validar día de la semana
Solicita un número del 1 al 7 y muestra el día correspondiente.

"""
dia = int(input("ingresa un número del 1 al 7:"))

if dia == 1:
    print("el dia es lunes")
elif dia == 2:
    print("el dia es martes")
elif dia == 3:
    print("el dia es miercoles")
elif dia == 4:
    print("el dia es jueves")
elif dia == 5:
    print("el dia es viernes")
elif dia == 6:
    print("el dia es sabado")
elif dia == 7:
    print("el dia es domingo")
else: 
    print("ingresa el número correspondinte")
