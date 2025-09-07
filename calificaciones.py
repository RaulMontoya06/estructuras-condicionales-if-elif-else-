print("CONVERSOR DE CALIFICACIONES")
cal = float(input("ingresa la calificacion a convertir:"))
if cal >= 90 and cal <= 100:
    print("la calificacion ",cal," es igual a: A")
elif cal >= 80 and cal <= 89:
    print("la calificacion ",cal," es igual a: B")
elif cal >= 70 and cal <= 79:
    print("la calificacion ",cal," es igual a: C")
elif cal >= 60 and cal <= 69:
    print("la calificacion ",cal," es igaul a: D")
else:
    print("la calificacion ",cal," es igual a: F")