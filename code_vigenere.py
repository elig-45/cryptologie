# pylint: disable=unused-variable
import code_cesar
from random_word import RandomWords
r = RandomWords()

def chiffrer(message, cle_chiffrement):
    message = str(message)
    resultat = ""
    cle_chiffrement = str(cle_chiffrement)
    cle_temp = 0
    c = 0
    for lettre in message:
        if (c >= len(cle_chiffrement)):
            c = 0
        cle_temp = ord(cle_chiffrement[c]) - 97
        resultat = resultat + code_cesar.chiffrer(lettre, cle_temp)
        c+=1
    return resultat

def dechiffrer(message, cle_chiffrement):
    message = str(message)
    resultat = ""
    cle_chiffrement = str(cle_chiffrement)
    cle_temp = 0
    c = 0
    for lettre in message:
        if (c >= len(cle_chiffrement)):
            c = 0
        cle_temp = ord(cle_chiffrement[c]) - 97
        resultat = resultat + code_cesar.dechiffrer(lettre, cle_temp)
        c+=1
    return resultat


if __name__ == "__main__":
    mot_aleatoire = r.get_random_word()
    print(mot_aleatoire)
    assert chiffrer("bonjour", "bac") == "copkows", "Erreur 1"
    assert chiffrer("copkows", "bac") == "dorloyt", "Erreur 2"
    assert dechiffrer(chiffrer(mot_aleatoire, "masupercle"), "masupercle") == mot_aleatoire, "Erreur 3"
    print("Tests validés.\n\n")