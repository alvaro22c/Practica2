review = """La película sigue a un grupo de astronautas que 
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo 
a través
de tormentas solares y fallos en el sistema de navegación. Al 
llegar
a Marte descubren que la base está abandonada y los 
suministros
destruidos. Torres decide sacrificar la nave nodriza para 
salvar
al equipo y logran volver a la Tierra en una cápsula de 
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje 
secreto."""

def FiltrodeSpoilers(palabras):
    lista = []
    for p in palabras.split(","):
        lista.append(p.lower())

    texto = review.split()

    for i in lista:
        for  n in range(len(texto)):
            if texto[n].lower() == i:
                texto[n]= "*" * len(i)  

    for  j in texto:
       print(j,end=" ")