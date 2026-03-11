def get_user_input():
    name_user = input("Je suis Python. Quel est votre pseudo ? ")
    game_rule = input(f"Bonjour {name_user} ! Voulez-vous afficher les règles du jeu ? (oui/non) ")
    if game_rule.lower() not in ["oui", "non"]:
        print("Veuillez répondre par 'oui' ou 'non'.")
        return  
    
    if game_rule.lower() == "oui":
        get_game_rules()
        play_game()
    else:
        play_game()
        



def get_game_rules():
    print(
        "Le jeu comporte 3 levels avec la possibilié que le joueur choissise son level (si ce n'est pas sa 1è fois dans le Casino).\n"
        "\tEn d'autres termes, tout nouveau joueur doit passer par le 1è level. Suite à la 1è partie, il a le droit de choisir son level en lui rappelant / proposant le dernier niveau atteint.\n"
        "\n"
        "\tLors de chaque niveau, Python tire un nombre : level 1 (entre 1 et 10),\n"
        "\tlevel2 (1 et 20), level3 (1 et 30). C'est à vous de deviner le nombre mystérieux avec 3 essais (en tout) lors du 1è\n"
        "\tlevel, 5 au 2è level et 7 au 3è level. Chaque essai ne durera pas plus de 10 secondes. Au-delà,\n"
        "\tvous perdez votre essai. Att : si vous perdez un level, vous rejouez le level précédent.\n"
        "\tQuand vous souhaitez quitter le jeu, un compteur de 10 secondes est mis en place.\n"
        "\tEn absence de validation de la décision, le jeu est terminé.\n"
        "\tPython fournit enfin les statistiques du jeu."
    )

# def play_game():
#     import random
#     print("Très bien, passons directement au jeu !")
#     mise = input("Combien souhaitez-vous miser ? ")
#     if not mise.isdigit():
#         print("Veuillez entrer un montant valide.")
#         return
#     print(f"Vous avez misé {mise}€. Bonne chance !")
#     nb_python = random.randint(1,10)
#     i = 0
#     nb_coup = 3
#     if mise == 10:
#         print("Je viens de penser à un nombre entre 1 et 10. Devinez lequel ? /n"
#        "\tAttention: Vous n'avez doroit qu'a 3 essaies")
#         nb_user = input(f"Devinez la valeur choisi !")        
#         while(i <= nb_coup):
#             if (i == 0 and nb_user == nb_python ) : 
#                 print("bingo tu as reussi d'un coup !")
#         i += 1
                
#     else:
#         print("Montant insuffisant !")

def play_game():
    print("Très bien, passons directement au jeu !")
    mise_str = input("Combien souhaitez-vous miser ? ")
    
    if not mise_str.isdigit():
        print("Veuillez entrer un montant valide.")
        return
    
    mise = int(mise_str) # On transforme le texte en nombre

    if mise >= 10: # On accepte 10€ ou plus
        print(f"Vous avez misé {mise}€. Bonne chance !")
        nb_python = random.randint(1, 10)
        
        i = 1 # On commence au premier essai
        nb_coup = 3
        print("J'ai choisi un nombre entre 1 et 10. Devinez lequel ?")
        print(f"Attention : Vous avez {nb_coup} essais.")

        while i <= nb_coup:
            # On demande au joueur de deviner À L'INTÉRIEUR de la boucle
            devine = int(input(f"Essai n°{i} - Votre choix : "))
            
            if devine == nb_python:
                if i == 1:
                    print("Bingo ! Trouvé du premier coup ! Tu es devin ? 🔮")
                else:
                    print(f"Bravo ! Gagné en {i} coups.")
                return # On sort de la fonction car il a gagné
            
            print("Raté ! Essayez encore.")
            i += 1 # TRÈS IMPORTANT : on avance au coup suivant
            
        print(f"Dommage, vous avez perdu ! Le nombre était {nb_python}.")
    else:
        print("Montant insuffisant ! (Minimum 10€)")


def main():
    get_user_input()


if __name__ == "__main__":
    main()
