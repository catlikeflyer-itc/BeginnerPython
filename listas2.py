def fibonacci(n):
    if n<=0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        
fib = []

while True:
    reg = int(input('Cantidad de numeros de la serie deseados >>> '))

    if reg > 0:
        for i in range(1,reg+1):
            fib.append(fibonacci(i))
        break
    else: 
        print('Numero invalido')

print(f'La serie hasta la posicion {reg} esta compuesto por {fib}')

