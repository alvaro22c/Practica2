students = [
{"name": "  Ana García ", "grade": "8", "status":"aprobado"},
{"name": "pedro lópez", "grade": "4", "status":"DESAPROBADO"},
{"name": "MARÍA FERNÁNDEZ", "grade": "10", "status":"Aprobado"},
{"name": "ana garcía", "grade": "9", "status":"aprobado"},
{"name": None, "grade": "7", "status": "aprobado"},
{"name": "Luis Martínez  ", "grade": None, "status":"aprobado"},
{"name": " carlos RUIZ", "grade": "6", "status":"aprobado"},
{"name": "PEDRO LÓPEZ ", "grade": "3", "status":"desaprobado"},
{"name": "  ", "grade": "5", "status": "aprobado"},
{"name": "María Fernández", "grade": "7", "status":"APROBADO"},
{"name": "Sofía Torres", "grade": "9", "status":"Aprobado"},
{"name": "  sofía torres ", "grade": "8", "status":"aprobado"},
{"name": "Carlos Ruiz", "grade": "6", "status":"APROBADO"},
{"name": "Roberto Díaz", "grade": "absent", "status":"ausente"},
{"name": "roberto díaz", "grade": "", "status":"Ausente"},
{"name": None, "grade": None, "status": None},
{"name": "Laura Méndez", "grade": "7", "status":"aprobado"},
{"name": "  laura méndez", "grade": "8", "status":"Aprobado"},
{"name": "GABRIELA RÍOS", "grade": "5", "status":"aprobado"},
{"name": "gabriela ríos ", "grade": "4", "status":"Desaprobado"}]


def NormalizacionDeAlumnos():
    lista =[]
    for i in students:
        name = i["name"]
        grade = i["grade"]
        status = i["status"]
        eliminar = True
        if not(name == None) and name.strip() != "":
            eliminar = False


        if grade==None or grade == "" or grade == "absent":
            eliminar =True
        
        if not  eliminar:
            i["name"] = i["name"].strip().title()
            i["status"] = i["status"].strip().title()
            if i.get("name") not in [j["name"]for j in lista]: 
                lista.append(i)
            

            nombre =i["name"].strip().title()
            estado = i["status"].strip().title()
            nota = i["grade"]
    
            for j in lista:       
                if nombre== j["name"] :
                    if  int(nota )>int(j["grade"]) :
                        j["grade"]= nota
                        j["status"]= estado

    lista = sorted(lista,key= lambda x:x["name"])


    print("Registro limpios de alumnos :  ")
    print("-"*50)
    print(f"Nombre{"Nota":>25}{"Estado":>10}")
    for j in lista:
        nombre,nota,Estado = j.values()
        print(f"{nombre:<28}{nota:<9}{Estado:<10}")



    #for dic in lista:
    #    print(dic)