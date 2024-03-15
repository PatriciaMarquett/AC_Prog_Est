"""
Programação Estruturada
2024.1
08/03/2024

AC5
"""

import random

def main ():
    rod = 1
    vida_a = random.randint(1,100)
    ataq_a = random.randint(10,20)
    def_a = random.randint(1,5)
    vida_m = random.randint(60,80)
    ataq_m = random.randint(20,30)
    print("Aventureiro:", "vida:" , vida_a , "at:" , ataq_a , "def:" , def_a)
    print("Monstro:", "vida:" , vida_m , "at:" , ataq_m)
    while True:
        print ("Rodada", rod)
        dano_a = random.randint(1, ataq_a)
        vida_m = vida_m - dano_a
        if vida_m <= 0:
            break
        if vida_m > 0:
            dano_m = (random.randint(1, ataq_m)) - def_a
            vida_a = vida_a - dano_m
        if vida_a > 0:
            print("Aventureiro:", "vida:" , vida_a , "at:" , ataq_a , "def:" , def_a)
            print("Monstro:", "vida:" , vida_m , "at:" , ataq_m)
            rod += 1
        elif vida_a <= 0:
            break
    if vida_m <= 0:
        print ("O monstro morreu!")
    elif vida_a <= 0:
        print ("Você morreu!")





main()

