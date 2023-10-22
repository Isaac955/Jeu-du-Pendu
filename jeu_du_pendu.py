# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:23:25 2023

@author: ISAAC
"""

from getpass import getpass

mot_a_deviner = getpass("Entrez votre mot : ")

liste = list(mot_a_deviner)
maListe = ["*"] * len(mot_a_deviner)
print("".join(maListe))

nombre_erreurs = 0

while nombre_erreurs < 10:
    lettre = input("Entrez une lettre : ")

    if len(lettre) > 1:
        if lettre == mot_a_deviner:
            print("Vous avez trouvé !")
            break

    if lettre in liste:
        for i, x in enumerate(liste):
            if x == lettre:
                maListe[i] = x
        w = "".join(maListe)
        print("Bonne lettre.", w)
    else:
        nombre_erreurs += 1
        print("Mauvaise lettre. Il vous reste %s essai(s)" % (10 - nombre_erreurs))

if nombre_erreurs == 10:
    print("Vous avez perdu... Le mot à deviner était :", mot_a_deviner)


