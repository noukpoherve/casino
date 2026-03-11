from functions.select_a_level import jouer_un_level
from functions.choose_starting_level import choisir_level_depart
from functions.add_int_value import demander_entier
from functions.say_yes_or_no import demander_oui_non
from functions.say_yes_or_no import demander_oui_non
from functions.victory_effect import effet_victoire

DOTATION_INITIALE = 10

def jouer_partie(name_user, player_stats):
    print(f"\nBonjour {name_user}, vous avez {DOTATION_INITIALE} €.")

    level = choisir_level_depart(player_stats)
    solde = float(DOTATION_INITIALE)
    plus_haut_level_session = level

    while solde >= 1 and level <= 3:
        print(f"\nSolde actuel : {solde:.2f} €")
        mise_max = int(solde)
        mise = demander_entier(f"Entrez votre mise (1 a {mise_max}) : ", 1, mise_max)
        solde -= mise

        if mise > player_stats["highest_mise"]:
            player_stats["highest_mise"] = float(mise)
        player_stats["sum_mise"] += float(mise)

        won, nb_coup, gain, nb_python = jouer_un_level(level, mise)

        if won:
            solde += mise + gain
            player_stats["wins"] += 1
            player_stats["wins_with_attempts"] += 1
            player_stats["sum_attempts_on_win"] += nb_coup

            if nb_coup == 1:
                player_stats["first_try_wins"] += 1
            if gain > player_stats["highest_gain"]:
                player_stats["highest_gain"] = gain
            if level > player_stats["best_level"]:
                player_stats["best_level"] = level

            if level > plus_haut_level_session:
                plus_haut_level_session = level

            print(f"Bingo ! Gagne en {nb_coup} coup(s). Gain : {gain:.2f} €")
            effet_victoire()
            print(f"Nouveau solde : {solde:.2f} €")

            if level == 3:
                print("Bravo ! Vous avez termine le level 3.")
                break

            continuer = demander_oui_non("Voulez-vous passer au niveau suivant ? (oui/non) : ")
            if continuer:
                level += 1
                print(f"Super, vous passez au level {level}.")
            else:
                break
        else:
            player_stats["losses"] += 1
            print(f"Perdu ! Mon nombre etait {nb_python}.")
            level -= 1
            if level < 1:
                level = 1
            print(f"Vous rejouez au level {level}.")

    if solde < 1:
        print("Vous n'avez plus assez d'argent pour continuer.")

    player_stats["games_played"] += 1
    if plus_haut_level_session > player_stats["best_level"]:
        player_stats["best_level"] = plus_haut_level_session

    print(f"\nFin de partie. Vous terminez avec {solde:.2f} €.")