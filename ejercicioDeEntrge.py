import random
 # 3-la lista pasa a ser un diccionario
words = {"lenguaje y entorno":["python","programa"],"tipos de datos":["lista","cadena","entero","variable"],
         "estructuras de organizacion":["funcion","bucle"]}

puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

categoria= words[input("Elija una de las categorias :\n  "  # 3
                       "-lenguaje y entorno. \n   "
                       "-tipos de datos. \n  "
                       "-estructuras de organizacion. \n ")]  
# 4- ahora se juega hasta adivinar  todas la palabras de una categoria,sin repetir la palabras
palabra = random.sample(categoria,len(categoria))
for word in palabra:
   
   guessed = []
   attempts = 6

   while attempts > 0:
      # Mostrar progreso: letras adivinadas y guiones para las que faltan
      progress = ""
      for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
      print(progress)
      # Verificar si el jugador ya adivinó la palabra completa
      if "_" not in progress:
        # 2- se modifica el juego para que muestre el puntaje 
        puntaje += 6                          
        print("¡Ganaste!")
        print(f"el puntaje Obteido es : {puntaje}")
        break

      print(f"Intentos restantes: {attempts}")
      print(f"Letras usadas: {', '.join(guessed)}")

      letter = input("Ingresá una letra: ")
      
      if "a"<= letter <= "z" and len(letter) == 1:    # 1- verifica que se ingrese un caracter valido  
        if letter in guessed:
          print("Ya usaste esa letra.")
          attempts -= 1                              #2
          puntaje -= 1 
        elif letter in word:
          guessed.append(letter)
          print("¡Bien! Esa letra está en la palabra.")
        else:
          guessed.append(letter)
          attempts -= 1
          puntaje -= 1                               # 2
          print("Esa letra no está en la palabra.")
      else:
          print("entrada no valida")
          attempts-= 1
          puntaje -= 1                                # 2
      print()
      
   else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje = 0                                # 2
        print(f"el puntaje obtenido es :{puntaje}")