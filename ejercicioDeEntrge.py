import random
words = ["python","programa","variable","funcion","bucle","cadena","entero","lista",]
word = random.choice(words)
guessed = []
attempts = 6
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

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