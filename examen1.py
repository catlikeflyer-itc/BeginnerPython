def imc(peso, estatura):
    return peso/(estatura**2)

def info_categoria(categoria, tag):
    try:
        print("\n"+tag)
        print(f"{tag}: {len(categoria)} personas\nSuma de IMC: {sum(categoria)}\nPromedio de IMC: {sum(categoria)/len(categoria)}")
    except ZeroDivisionError:
        print("No hay registros para esta categoria")
        
def main():
    personas = int(input("Cantidad de personas a ser evaluadas: "))
    acumulador = 0
    bajo_peso = []
    peso_normal = []
    sobrepeso = []
    obesidad = []


    while acumulador < personas:
        peso = float(input("Peso en kilogramos: "))
        estatura = float(input("Estatura en metros: "))
        imc_ = round(imc(peso, estatura), 2)
        if imc_ < 18.5:
            print(f"Su IMC es de {imc_}, bajo peso")
            bajo_peso.append(imc_)
        elif imc_ >= 18.5 and imc_ <= 25:
            print(f"Su IMC es de {imc_}, peso normal")
            peso_normal.append(imc_)
        elif imc_ > 25 and imc_ <= 30:
            print(f"Su IMC es de {imc_}, sobrepeso")
            sobrepeso.append(imc_)
        else: 
            print(f"Su IMC es de {imc_}, obesidad")
            obesidad.append(imc_)
        acumulador += 1
    
    info_categoria(bajo_peso, "Bajo Peso")
    info_categoria(peso_normal, "Normal")
    info_categoria(sobrepeso, "Sobrepeso")
    info_categoria(obesidad, "Obesidad")

if __name__ == "__main__": main()