def costo_local(peso):
    if peso < 1:
        return 500
    elif peso < 5:
        return 1000
    else:
        return 2000

def costo_regional(peso):
    if peso < 1:
        return 1000
    elif peso < 5:
        return 2500
    else:
        return 5000

def costo_nacional(peso):
    if peso < 1:
        return 2000
    elif peso < 5:
        return 4500
    else:
        return 8000
    
def CalculadoraDeEnvios(peso,zona):

    if zona in ["local","regional","nacional"]:
        match zona:
        
            case "local":
                print(costo_local(peso))
            case "regional":
                print(costo_regional(peso))
            case "nacional":
                print(costo_nacional(peso))
    else:
        print("zona no valida. las zonas disponibles son : local,regional,nacional.")