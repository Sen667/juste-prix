import random

while True:
    print("Bienvenue au Juste Prix")
    longueur = int(input("Indiquez la longueur du nombre : "))
    essaies = int(input("Combien d'essais voulez-vous ?"))

    # Génération d'un prix aléatoire avec la longueur spécifiée
    prix = random.randint(10 ** (longueur - 1), (10 ** longueur) - 1)

    print("x--------------x Vous avez", essaies, "essais pour trouver le bon prix ! x--------------x")

    for loop in range(essaies):
        try:
            value = int(input("Essai " + str(loop + 1) + ": "))
            if prix < value:
                print("Le prix est trop haut, essayez à nouveau.")
            elif prix > value:
                print("Le prix est trop bas, essayez à nouveau.")
            else:
                print("Bravo, vous avez gagné ! La partie est terminée.")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    if loop == essaies - 1:
        print("Désolé, vous avez épuisé vos essais. La partie est terminée. Le prix était", prix)

    replay = input("Voulez-vous rejouer ? (Oui/Non) ").lower()
    if replay != "oui":
        break
