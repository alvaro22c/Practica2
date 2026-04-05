def sorteo(lista):
     aux = lista.copy()
     valido = True
     while valido:
           aux = random.sample(aux,len(aux))
        
           for i in range(len(lista)):
           
                if lista[i] != aux[i]:
                     break
           valido = False
     return aux


import random
def SorteoDeAmigos(nombres):

    lista = nombres.split(",")

    valido = True
    if len(lista) >= 3:
        for i in lista:
            if lista.count(i) != 1:
                valido = False


    if valido:
        aux = sorteo(lista)
    
        for j in range(len(lista)):
            print(f"{lista[j]} -> {aux[j] }")

    else:
        print(" error por nombre repetido:")