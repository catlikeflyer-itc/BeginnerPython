def pies(centimetros):
    return centimetros*30.48

def pulgadas(centimetros):
    return centimetros*2.54

def yardas(centimetros):
    return centimetros*91.44

def main():
    mod = input("Seleccione la opcion correspondiente 1 –pies a cm, 2 -pulgadas a cm, 3 –yardas a cm: ")
    if int(mod) <= 3 and int(mod) > 0:
        num = float(input("Inserte medida: "))
        txt = "{} {} equivalen a {} cm"
        if mod == "1":
            print(txt.format(num, "pies", pies(num)))
        elif mod == "2":
            print(txt.format(num, "pulgadas", pulgadas(num))) 
        elif mod == "3":
            print(txt.format(num, "yardas", yardas(num))) 
    else:
        print("Opcion invalida")

if __name__ == "__main__":main()
    
        