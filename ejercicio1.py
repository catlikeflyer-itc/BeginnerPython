# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:02:47 2020

@author: D. Nam
"""
# Ejercicio 1

def main():
    
    not_valid = True
    while not_valid:
        price = int(input("Introduzca el precio: "))
        if price >= 0:
            print("El precio es valido")
            return False
        else: 
            print("Precio invalido")

if __name__ == "__main__":main()

#%%
# Ejercicio 2

def main():
    
    d = float(input("Ingresa la distancia en km: "))
    t = float(input("Ingresa el tiempo en horas: "))
    
    v = d/t
    
    print("La velocidad promedio es de {} km/h".format(v))

if __name__ == "__main__":main()

#%%
# Ejercicio 3

def main():
    
    m = float(input("Longitud en metros: "))
    f = m*100/2.54/12
    
    print("{} metros equivalen a {} pies".format(str(m), str(f)))
 
if __name__ == "__main__":main()

#%%
# Ejercicio 4

def main():
    
    age = int(input("Introduzca su edad: "))
    id_ = input("Trae consigo una identificacion? [si/no]: ")
    
    if age >= 18 and id_ == "si":
        print("Puede tramitar su licencia")
    else: print('No cumple con los requerimientos')

if __name__ == "__main__":main()


