



def ValidacionDeEmail(email):
    valido = True

    if email.count("@") != 1:          #• Contiene exactamente un @.
        valido = False

    if email.startswith("@") or email.startswith(".") or email.endswith("@") or email.endswith("."):#• No empieza ni termina con @ ni con ..
        valido = False

    if valido :
        lista = email.split("@")
        lado_izquierdo = lista[0]
        lado_derecho= lista[1]

        if not(len(lado_izquierdo) >= 1):  #• Tiene al menos un carácter antes del @.
            valido = False

        if not(lado_derecho[0] == ".") :  #• Tiene al menos un punto (.) después del @.
            valido = False

        if len(lado_derecho[1:]) < 2:  #• La parte después del último punto tiene al menos 2 caracteres (el dominio).
            valido = False

    print(f"El email ingresado: {email}")     

    if valido :
        print(" El email es valido.")
    else:
        print("El email no es valido.")