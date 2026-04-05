posts = [
"Arrancando el lunes con energía #Motivación #NuevaSemana",
"Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
"No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
"Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
"Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
"Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
"Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
"Finde de lluvia, maratón de series #SerieAdicta #Relax",
"Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
]
def AnalisisDeHashtags():
    dic_hashtags = {}
    hashtags_unicos = 0
    for i in posts:
        lista = i.split()
        for j in lista:
            if j.startswith("#"):

                if j in dic_hashtags:
                    dic_hashtags[j] += 1
                else:
                    dic_hashtags[j] = 1
                    hashtags_unicos += 1

    print("hashtags trending (mas de una aparicion) :")
    for  i,j in dic_hashtags.items():
        if j > 1:
            print(i,j)
    print()
    print(f"total hashtags unicos: {hashtags_unicos}")