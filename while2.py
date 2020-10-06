count = 0
suma = 0

while suma >= 0:
    num = float(input("Ingresa numero flotante: "))

    if num >= 0:
        suma += num

    else: break

    count += 1

print(f"El promedio es {suma/count}")
