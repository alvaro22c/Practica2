
rounds = [{
'theme': 'Entrada','scores': {
'Valentina':  {'judge_1': 8, 'judge_2': 7,'judge_3': 9},
'Mateo':      {'judge_1': 7, 'judge_2': 8,'judge_3': 7},
'Camila':     {'judge_1': 9, 'judge_2': 9,'judge_3': 8},
'Santiago':   {'judge_1': 6, 'judge_2': 7,'judge_3': 6},
'Lucía':      {'judge_1': 8, 'judge_2': 8,'judge_3': 8},}},

{'theme': 'Plato principal','scores': {
'Valentina':  {'judge_1': 9, 'judge_2': 9,'judge_3': 8},
'Mateo':      {'judge_1': 8, 'judge_2': 7,'judge_3': 9},
'Camila':     {'judge_1': 7, 'judge_2': 6,'judge_3': 7},
'Santiago':   {'judge_1': 9, 'judge_2': 8,'judge_3': 8},
'Lucía':      {'judge_1': 7, 'judge_2': 8,'judge_3': 7},}},

{
'theme': 'Postre','scores': {
'Valentina':  {'judge_1': 7, 'judge_2': 8,'judge_3': 7},
'Mateo':      {'judge_1': 9, 'judge_2': 9,'judge_3': 8},
'Camila':     {'judge_1': 8, 'judge_2': 7,'judge_3': 9},           
'Santiago':   {'judge_1': 7, 'judge_2': 7,'judge_3': 6},
'Lucía':      {'judge_1': 9, 'judge_2': 9,'judge_3': 9},}},

{
'theme': 'Cocina internacional','scores': {
'Valentina': {'judge_1': 8, 'judge_2': 9,'judge_3': 9},
'Mateo':     {'judge_1': 7, 'judge_2': 6,'judge_3': 7},
'Camila':    {'judge_1': 9, 'judge_2': 8,'judge_3': 8},
'Santiago':  {'judge_1': 8, 'judge_2': 9,'judge_3': 7},
'Lucía':     {'judge_1': 7, 'judge_2': 7,'judge_3': 8},}},

{
'theme': 'Final libre','scores': {
'Valentina': {'judge_1': 9, 'judge_2': 8,'judge_3': 9},
'Mateo':     {'judge_1': 8, 'judge_2': 9,'judge_3': 8},
'Camila':    {'judge_1': 7, 'judge_2': 7,'judge_3': 7},
'Santiago':  {'judge_1': 9, 'judge_2': 9,'judge_3': 9},
'Lucía':     {'judge_1': 8, 'judge_2': 8,'judge_3': 7},}}]


def CompetenciaDeCocineros():
    j = 0
    dic = {'Valentina': {'Puntaje': 0, 'Rondas_Ganadas': 0,'mejor_ronda': 0},
       'Mateo': {'Puntaje': 0, 'Rondas_Ganadas': 0,'mejor_ronda': 0},
       'Camila': {'Puntaje': 0, 'Rondas_Ganadas': 0,'mejor_ronda': 0},
       'Santiago': {'Puntaje': 0, 'Rondas_Ganadas': 0,'mejor_ronda': 0},
       'Lucía': {'Puntaje': 0, 'Rondas_Ganadas': 0,'mejor_ronda': 0}}

    for i in rounds:   
        Max = -1
        ganador = ""
        for  participante,puntaje in i["scores"].items():
            total = sum(puntaje.values())

            if total > Max:
                Max = total
                ganador = participante
                
            dato = dic[participante]
            dato["Puntaje"]+= total  
            dato["mejor_ronda"] = total if total > dato['mejor_ronda'] else dato['mejor_ronda']
            
        
        j += 1
        print(f"Ronda {j}  - {i['theme']}")
        print(" ")
        print(f"El ganador es :{ganador}({Max}pts)")
        
        dato = dic[ganador]
        dato["Rondas_Ganadas"] += 1

        dic_ordenado =dict(sorted(dic.items(), key=lambda x : x[1]["Puntaje"],reverse=True))
        #dic = dict(sorted(dic.items(),reverse=True))
        print(f"{"Cocinero":<15} {"Puntaje":<12}{"Rondas ganadas":<19}{"Mejor puntaje":<18}{"Promedio"}")
        print("-"*60)
        for t in dic_ordenado.items():
            cocinero = t[0]
            puntaje,rondas_ganadas,mejor_ronda =t[1].values()
            print(f"{cocinero:<18}{puntaje:<15}{rondas_ganadas:<18}{mejor_ronda:<17}{puntaje/5:<15}")
        print("-"*60)     
        print(" ")