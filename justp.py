print ("bienvenue au juste prix", end=" ") ; print ("indiquer une valeur !")
print ("x--------------x vous avez 120 essaies pour trouver le bon prix ! x--------------x")
prix = 34651564787632124

for loop in range(120):
 value = int(input()) 
 if  prix < value:
        print("le prix est trop haut bro ")
 if prix > value:
    print("prix trop bas bro ")

 if  prix == value:
    print("wow ta gagné") ; print("la partie est terminée") 
