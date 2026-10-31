import random
import string
from words import words

word = ""
vidas = 6

def gvalidword(words):
    word = random.choice(words) # pega uma aleatória
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = gvalidword(words).upper()
    wletters = set(word) #letras que já estão
    alphabet = set(string.ascii_uppercase)
    usedlett = set()

    vidas = 6

    while len(wletters) > 0 and vidas > 0:
        #join transforma a lista em string
        print("Você já tentou as seguintes letras: ", " ".join(usedlett))

        # palavra atual
        wlist = [letter if letter in usedlett else '-' for letter in word]
        print(" ".join(wlist))

        uslett = input("Algum chute? ").upper()
        if uslett in alphabet - usedlett:
            usedlett.add(uslett)
            if uslett in wletters:
                wletters.remove(uslett)
            else:
                vidas = vidas - 1 #funcionalidade principall
                print("A letra não faz parte da palavra :(")
        elif uslett in usedlett:
            print("Você já chutou essa... Tente novamente.")
        else:
            print("Caractere inválido. Tente de novo.")
    
    if vidas == 0:
      print("Game Over! Suas vidas acabaram! A palavra era:", word)
    else:
      print("Parabéns! Você advinhou a palavra!")  

#acaba quando termina a palavra ou as vidas
hangman()
