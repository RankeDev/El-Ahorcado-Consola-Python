import random
import json
from palabras import words

"""
# Cargo el JSON
with open("palabras.json") as words:
    wordsJSON = json.load(words) # Guardo el JSON cargado en una variable para poder referenciarlo

# Selecciono la clave que me interesa
words_pool = wordsJSON.get("words") # Con la referencia al JSON, uso el metodo referencia.get("clave") y guardo ese array que obtiene en la variable words_pool
"""

# Seleccionar una palabra al azar
word = random.choice(words)
hidden_word = ["_"] * len(word)
chances = 5
failed_letters = list()
guess_word = False

print("Intente adivinar la palabra")

while chances > 0 and "_" in hidden_word and guess_word == False:
    print("\nPalabra:", " ".join(hidden_word))
    print(f"Le quedan {chances} intentos")
    guess = input("Adivine una letra o la palabra: ").lower()
    
    if guess == word:
        guess_word = True
    elif guess in word:
        for i, l in enumerate(word):
            if l == guess:
                hidden_word[i]= guess
        print("Las siguentes letras no están en la palabra: ", failed_letters)
    else:
        if guess not in failed_letters:
            chances -= 1
            print("Letra incorrecta.")
            failed_letters.append(guess)
            print("Las siguentes letras no están en la palabra: ", failed_letters)
        else:
            print("Letra incorrecta, ya la ha dicho previamente.")
            print("Las siguentes letras no están en la palabra: ", failed_letters)

if "_" not in hidden_word or guess_word == True:
    print("\n¡Felicidades! Adivinó la palabra:", word)
else:
    print("\n¡Perdiste! La palabra era:", word)

input("Presione enter para cerrar el juego")