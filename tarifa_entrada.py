print("TARIFA DE ENTRADA")
edad = int(input("ingrese su edad: "))
if edad <= 12:
    print("costo de entrada es de: $50")
elif edad >=12 and edad <=17:
    print("costo de entrada es de: $80")
else:
    print("costo de entrada es de: $120")