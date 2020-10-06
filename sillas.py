def frecuente(precio):
    return precio*.80

def normal(precio):
    if precio >= 10000 and precio < 20000:
        return precio*.90

    elif precio >= 20000:
        return precio*.85

    else:
        return precio

def main():
    try:
        precios = {"B": 700, "E": 900, "L": 1500}
        silla = input("Ingrese tipo de silla\n B - basica\n E - estandar \n L - lujo\n>>>")
        cliente = input(" F - frecuente\n N - normal\n>>>")
        cantidad = input("Cuantas sillas quiere?: ")
        pt = precios[silla]*int(cantidad)
        try:
            if cliente == "F":
                total = frecuente(pt)

            elif cliente == "N":
                total = normal(pt)
            
            else:
                print("No hay clientes de ese tipo")

            print(f"Precio bruto: {pt} MXN\nDescuento: {pt-total} MXN\nTotal a pagar: {total} MXN")
        
        except UnboundLocalError:
            print("Datos invalidos")

    except (ValueError, KeyError):
        print("Datos invalidos")

if __name__=="__main__":main()



            
    
     