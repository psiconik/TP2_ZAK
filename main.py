# Zak Alexandre Kiraly
# 12 sept 2023
# TP2
import random


chiffre_aleatoire = random.randint(1, 1000)

guessed_number = int(input("quel est ton essait (nombre)? \n"))

if guessed_number < chiffre_aleatoire :
    print("c'est gratuit!")

if guessed_number > chiffre_aleatoire :
    print("cela coute 5,78$ ")

if guessed_number = chiffre_aleatoire :
    print("cela coute 13,01$")