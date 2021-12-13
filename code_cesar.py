def dechiffrer(message, cle_chiffrement):
    int(cle_chiffrement)
    resultat = ""
    for lettre in message:
        resultat = resultat + chr(ord(lettre) - cle_chiffrement)
    return resultat

def chiffrer(message, cle_chiffrement):
    return dechiffrer(message, -cle_chiffrement)


if __name__ == "__main__":
    assert dechiffrer("Nsktwrfynvzj", 5) == "Informatique", "Erreur 1"
    assert dechiffrer(chiffrer("azertyuiop", 3), 3) == "azertyuiop", "Erreur 2"
    print("Tests validés.\n\n")