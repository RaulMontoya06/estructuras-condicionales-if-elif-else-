print("CLASIFICACION DE TRIANGULOS")
long1 = float(input("ingrese la longitud del lado 1: "))
long2 = float(input("ingrese la longitud del lado 2: "))
long3 = float(input("ingrese la longitud del lado 3: "))
if long1 == long2 and long2 == long3:
    print("el triangulo es equilatero")
elif long1 == long2 or long1 == long3 or long2 == long3:
    print("el triangulo es isoceles")
else:
    print("el triangulo es escaleno")