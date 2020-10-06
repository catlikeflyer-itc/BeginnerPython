q = int(input('Ingrese cantidad de numeros a operar >>> '))

lista = []
listacubo = []

for i in range(0,q):
    num = int(input('Ingrese numero >>> '))
    lista.append(num)
    listacubo.append(num**3)
    i += 1

print(f'Lista de numeros: {lista}')
print(f'Lista al cubo: {listacubo}')
