cantidad = int(input("Numeros a analizar: "))
pares = []
impares = []

for i in range(0, cantidad):
    num = int(input("Numero: "))
    if (num % 2) == 0: 
        pares.append(num)
    else:
        impares.append(num)

try:
    print(f"\nPares: {len(pares)} numeros\nSuma: {sum(pares)}\nPromedio: {sum(pares)/len(pares)}")
except ZeroDivisionError:
    print("\nNo hay pares")
    
try:
    print(f"\nImpares: {len(impares)} numeros\nSuma: {sum(impares)}\nPromedio: {sum(impares)/len(impares)}")
except ZeroDivisionError:
    print('\nNo hay impares')

