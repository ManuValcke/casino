import os
from random import randrange
print("\n\t\t\t\t\t\t========= Le juste prix ! =========\n\n")
print("Je suis python. Quel est votre pseudo\n")
pseudo = input()
print("\nHello",pseudo,", vous avez 10€, très bien ! Installez vous SVP à la table de pari.")
print("\nLes règles du jeu sont simples : vous devez deviner un chiffre compris entre 1 et 10")
print("\nSi vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !")
print("\nSi vous devinez du 2ème coup, vous gagnez exactement votre mise !")
print("\nSi vous devinez du 3ème coup, vous gagnez la moitié de votre mise !")
print("\nAttention, vous n'avez que 3 essais, vous pourrez retenter votre chance si votre cagnotte vous le permet ou quitter le jeu")
prixPropose = 0
nbessai = 1
solde = 10



##### FONCTIONS

def niveau_un():
    prixPropose = 0
    nbessai = 1
    solde = 10
    prixMystere = randrange(1, 10)
    mise = int(input("\nLe jeu commence, entrez votre mise (entre 1 et 10€): \n"))
    print("\nOK",pseudo,"vous avez misez",mise,"€. Vous devez maintenant trouvez un chiffre entre 1 et 10\n")
    solde = solde - mise
    while mise <= 0 or mise >= 11:
        print ("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 €.\n")
        mise = int(input("Entrez votre mise : \n"))
        solde = solde - mise
        print(solde)
        if mise > 1:
            break
    while prixPropose != prixMystere:
        while nbessai < 4:
            print("\nQuel est le juste prix ?\n")
            prixPropose = input()
            prixPropose = int(prixPropose)

            if prixPropose < prixMystere:
                print("\nC'est plus !\n")
                nbessai = nbessai +1
            elif prixPropose > prixMystere:
                print("\nC'est moins !\n")
                nbessai = nbessai +1
            if prixPropose == prixMystere:
                break
        else:
            print("\nVous avez perdu ",pseudo,"...\n")
            print("\nVotre solde est donc de",solde,"€")
            break
    else:
        print("\nET C'EST LE JUSTE PRIX !!! Felicitation",pseudo,"!\n")
        print("\nVous avez gagnez en",nbessai,"coups !\n")
        if nbessai == 1:
            print("\nVous gagnez le double de votre mise !")
            solde = solde + (mise * 2)
            print("\nVotre solde est donc de",solde,"€")
        elif nbessai == 2:
            print("\nVous ne perdez pas d'argent !")
            solde = (solde + mise)
            print("\nVotre solde est donc de",solde,"€")
        elif nbessai == 3:
            print("\nVous perdez la moitié de votre mise...")
            solde = solde + (mise / 2)
            print("\nVotre solde est donc de",solde,"€")


    suite = str(input("\nVoulez vous continuer le jeu ? (oui ou non)"))
    while suite != "oui" or "non":
        if suite == "oui":
            print("\nLourd ! Vous passez au niveau 2")
            break
        elif suite == "non":
            print("\nD'accord, vous repartez donc avec",solde,"€")
            break
        suite = str(input("Je ne comprends pas votre réponse, souhaitez-vous continuer la partie ? (oui ou non)"))

    ####### NIVEAU 2 FONCTIONS
    prixMystere = randrange(1, 20)
    print("\nAttention, au niveau 2 vous avez 5 essais")
    mise = int(input("\nLe jeu commence, entrez votre mise (entre 1 et 10€): \n"))
    print("\nOK",pseudo,"vous avez misez",mise,"€. Vous devez maintenant trouvez un chiffre entre 1 et 10\n")
    solde = solde - mise
    while mise <= 0 or mise >= 11:
        print ("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 €.\n")
        mise = int(input("Entrez votre mise : \n"))
        solde = solde - mise
        print(solde)
        if mise > 1:
            break
    while prixPropose != prixMystere:
        while nbessai < 6:
            print("\nQuel est le juste prix ?\n")
            prixPropose = input()
            prixPropose = int(prixPropose)

            if prixPropose < prixMystere:
                print("\nC'est plus !\n")
                nbessai = nbessai +1
            elif prixPropose > prixMystere:
                print("\nC'est moins !\n")
                nbessai = nbessai +1
            if prixPropose == prixMystere:
                break
        else:
            print("\nVous avez perdu ",pseudo,"...\n")
            print("\nVotre solde est donc de",solde,"€")
            break
    else:
        print("\nET C'EST LE JUSTE PRIX !!! Felicitation",pseudo,"!\n")
        print("\nVous avez gagnez en",nbessai,"coups !\n")
        if nbessai == 1:
            print("\nVous gagnez le double de votre mise !")
            solde = solde + (mise * 2)
            print("\nVotre solde est donc de",solde,"€")
        elif nbessai == 2:
            print("\nVous ne perdez pas d'argent !")
            solde = (solde + mise)
            print("\nVotre solde est donc de",solde,"€")
        elif nbessai == 3:
            print("\nVous perdez la moitié de votre mise...")
            solde = solde + (mise / 2)
            print("\nVotre solde est donc de",solde,"€")

    suite = str(input("\nVoulez vous continuer le jeu ? (oui ou non)"))
    while suite != "oui" or "non":
        if suite == "oui":
            print("\nLourd ! Vous passez au niveau 2")
            break
        elif suite == "non":
            print("\nD'accord, vous repartez donc avec",solde,"€")
            break
        suite = str(input("Je ne comprends pas votre réponse, souhaitez-vous continuer la partie ? (oui ou non)"))

####### NIVEAU 1
prixMystere = randrange(1, 10)
mise = int(input("Le jeu commence, entrez votre mise (entre 1 et 10€): \n"))
print("\nOK",pseudo,"vous avez misez",mise,"€. Vous devez maintenant trouvez un chiffre entre 1 et 10\n")
solde = solde - mise
while mise <= 0 or mise >= 11:
    print ("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 €.\n")
    mise = int(input("Entrez votre mise : \n"))
    solde = solde - mise
    print(solde)
    if mise > 1:
        break
while prixPropose != prixMystere:
    while nbessai < 4:
        print("\nQuel est le juste prix ?\n")
        prixPropose = input()
        prixPropose = int(prixPropose)

        if prixPropose < prixMystere:
            print("\nC'est plus !\n")
            nbessai = nbessai +1
        elif prixPropose > prixMystere:
            print("\nC'est moins !\n")
            nbessai = nbessai +1
        if prixPropose == prixMystere:
            break
    else:
        print("\nVous avez perdu ",pseudo,"...\n")
        print("\nVotre solde est donc de",solde,"€")
        suite = str(input("\nVoulez vous relancer le jeu ? (oui ou non)"))
        while suite != "oui" or "non":
            if suite == "oui":
                print("\nOk je relance le niveau 1")
                niveau_un()
                break
            elif suite == "non":
                print("\nD'accord, vous repartez donc avec",solde,"€")
                break
            suite = str(input("Je ne comprends pas votre réponse, souhaitez-vous continuer la partie ? (oui ou non)"))

        break
else:
    print("\nET C'EST LE JUSTE PRIX !!! Felicitation",pseudo,"!\n")
    print("\nVous avez gagnez en",nbessai,"coups !\n")
    if nbessai == 1:
        print("\nVous gagnez le double de votre mise !")
        solde = solde + (mise * 2)
        print("\nVotre solde est donc de",solde,"€")
    elif nbessai == 2:
        print("\nVous ne perdez pas d'argent !")
        solde = (solde + mise)
        print("\nVotre solde est donc de",solde,"€")
    elif nbessai == 3:
        print("\nVous perdez la moitié de votre mise...")
        solde = solde + (mise / 2)
        print("\nVotre solde est donc de",solde,"€")


suite = str(input("\nVoulez vous continuer le jeu ? (oui ou non)"))
while suite != "oui" or "non":
    if suite == "oui":
        print("\nLourd ! Vous passez au niveau 2")
        break
    elif suite == "non":
        print("\nD'accord, vous repartez donc avec",solde,"€")
        break
    suite = str(input("Je ne comprends pas votre réponse, souhaitez-vous continuer la partie ? (oui ou non)"))

####### NIVEAU 2
prixMystere = randrange(1, 20)
print("\nAttention, au niveau 2 vous avez 5 essais")
mise = int(input("\nLe jeu commence, entrez votre mise (entre 1 et 10€): \n"))
print("\nOK",pseudo,"vous avez misez",mise,"€. Vous devez maintenant trouvez un chiffre entre 1 et 10\n")
solde = solde - mise
while mise <= 0 or mise >= 11:
    print ("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 €.\n")
    mise = int(input("Entrez votre mise : \n"))
    solde = solde - mise
    print(solde)
    if mise > 1:
        break
while prixPropose != prixMystere:
    while nbessai < 6:
        print("\nQuel est le juste prix ?\n")
        prixPropose = input()
        prixPropose = int(prixPropose)

        if prixPropose < prixMystere:
            print("\nC'est plus !\n")
            nbessai = nbessai +1
        elif prixPropose > prixMystere:
            print("\nC'est moins !\n")
            nbessai = nbessai +1
        if prixPropose == prixMystere:
            break
    else:
        print("\nVous avez perdu ",pseudo,"...\n")
        print("\nVotre solde est donc de",solde,"€")
        break
else:
    print("\nET C'EST LE JUSTE PRIX !!! Felicitation",pseudo,"!\n")
    print("\nVous avez gagnez en",nbessai,"coups !\n")
    if nbessai == 1:
        print("\nVous gagnez le double de votre mise !")
        solde = solde + (mise * 2)
        print("\nVotre solde est donc de",solde,"€")
    elif nbessai == 2:
        print("\nVous ne perdez pas d'argent !")
        solde = (solde + mise)
        print("\nVotre solde est donc de",solde,"€")
    elif nbessai == 3:
        print("\nVous perdez la moitié de votre mise...")
        solde = solde + (mise / 2)
        print("\nVotre solde est donc de",solde,"€")

suite = str(input("\nVoulez vous continuer le jeu ? (oui ou non)"))
while suite != "oui" or "non":
    if suite == "oui":
        print("\nLourd ! Vous passez au niveau 2")
        break
    elif suite == "non":
        print("\nD'accord, vous repartez donc avec",solde,"€")
        break
    suite = str(input("Je ne comprends pas votre réponse, souhaitez-vous continuer la partie ? (oui ou non)"))
