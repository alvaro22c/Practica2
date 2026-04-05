def CifradoCesar(mensaje,desplazamiento):
    for i in mensaje:
        if i.isalpha():
            letra = ord("A")if i.isupper() else ord("a")
            desplazar = chr((ord(i)-letra+desplazamiento)%26 + letra)
            print(desplazar,end="")
        else:
            print(i,end="")