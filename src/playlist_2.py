playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]


def DuracionDeUnaPlaylist():

    duracion_total=0
    maximo = -1
    minimo = 9999

    for elem in playlist:
        duracion = elem["duration"].split(":")
        min = int(duracion[0])*60
        seg = int(duracion[1])
        duracion_total += min + seg
        
        if min+seg>maximo:
            maximo = min+seg
            cancion_maslarga = elem["title"]
        if min+seg< minimo:
            minimo = min+seg
            cancion_mascorta = elem["title"]
            
    print(duracion_total/60)
    print(f" la cancion mas larga es :{cancion_maslarga}")
    print(f" la cancion mas corta es :{cancion_mascorta}")
