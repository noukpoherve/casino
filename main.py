import random
from datetime import datetime
from db import load_player_stats, save_player_stats
from victory_effect import effet_victoire


DOTATION_INITIALE = 10

def afficher_regles():
    print("\nRegles du jeu :")
    print("- Niveau 1 : nombre entre 1 et 10, 3 essais.")
    print("- Niveau 2 : nombre entre 1 et 20, 5 essais.")
    print("- Niveau 3 : nombre entre 1 et 30, 7 essais.")
    print("- Si vous perdez un niveau, vous redescendez au niveau precedent.")
    print("- Gains : 1er coup x2, 2e coup x1, 3e coup x0.5, sinon x0.25.")
    print("- Les stats du joueur sont sauvegardees.\n")


def creer_stats_joueur():
    return {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "games_played": 0,
        "wins": 0,
        "losses": 0,
        "best_level": 1,
        "first_try_wins": 0,
        "highest_gain": 0.0,
        "highest_mise": 0.0,
        "sum_mise": 0.0,
        "sum_attempts_on_win": 0,
        "wins_with_attempts": 0,
    }


def recuperer_stats_joueur(name_user):
    data = load_player_stats(name_user)
    if data is None:
        return creer_stats_joueur()

    player_stats = creer_stats_joueur()
    for key in player_stats:
        if key in data:
            player_stats[key] = data[key]
    return player_stats


def demander_oui_non(message):
    while True:
        rep = input(message).strip().lower()
        if rep in ["oui", "o", "yes", "y"]:
            return True
        if rep in ["non", "n", "no"]:
            return False
        print("Reponse invalide. Ecrivez oui ou non.")


def demander_entier(message, mini, maxi):
    while True:
        txt = input(message).strip()
        try:
            value = int(txt)
        except ValueError:
            print(f"Entrez un entier entre {mini} et {maxi}.")
            continue
        if value < mini or value > maxi:
            print(f"Valeur invalide. Entrez un entier entre {mini} et {maxi}.")
            continue
        return value


def get_config_level(level):
    if level == 1:
        return 10, 3
    if level == 2:
        return 20, 5
    return 30, 7


def calculer_gain(nb_coup, mise):
    if nb_coup == 1:
        return mise * 2
    if nb_coup == 2:
        return mise
    if nb_coup == 3:
        return mise * 0.5
    return mise * 0.25


def jouer_un_level(level, mise):
    max_number, max_attempts = get_config_level(level)
    nb_python = random.randint(1, max_number)

    print(f"\nLevel {level}: je pense a un nombre entre 1 et {max_number}.")
    print(f"Vous avez {max_attempts} essais.")

    for i in range(1, max_attempts + 1):
        nb_user = demander_entier(f"Essai {i}/{max_attempts} - Votre nombre : ", 1, max_number)

        if nb_user > nb_python:
            print("Votre nombre est trop grand.")
        elif nb_user < nb_python:
            print("Votre nombre est trop petit.")
        else:
            gain = calculer_gain(i, mise)
            return True, i, gain, nb_python

        if i == max_attempts - 1:
            print("Attention : il vous reste une seule chance.")

    return False, max_attempts, 0.0, nb_python


def choisir_level_depart(player_stats):
    best_level = int(player_stats.get("best_level", 1))
    if best_level < 1:
        best_level = 1
    if best_level > 3:
        best_level = 3

    if best_level == 1:
        return 1

    print(f"Vous avez deja atteint le level {best_level}.")
    return demander_entier(f"Choisissez votre level de depart (1 a {best_level}) : ", 1, best_level)


def afficher_stats(name_user, player_stats):
    games = int(player_stats["games_played"])
    wins = int(player_stats["wins"])
    losses = int(player_stats["losses"])

    if games > 0:
        win_rate = (wins / games) * 100
        mise_moy = player_stats["sum_mise"] / games
    else:
        win_rate = 0
        mise_moy = 0

    if player_stats["wins_with_attempts"] > 0:
        avg_attempts = player_stats["sum_attempts_on_win"] / player_stats["wins_with_attempts"]
    else:
        avg_attempts = 0

    print(f"\nStatistiques de {name_user} :")
    print(f"- Parties jouees : {games}")
    print(f"- Victoires : {wins}")
    print(f"- Defaites : {losses}")
    print(f"- Reussite : {win_rate:.1f}%")
    print(f"- Plus haut level atteint : {player_stats['best_level']}")
    print(f"- Victoires au 1er coup : {player_stats['first_try_wins']}")
    print(f"- Gain max : {player_stats['highest_gain']:.2f} €")
    print(f"- Mise max : {player_stats['highest_mise']:.2f} €")
    print(f"- Mise moyenne : {mise_moy:.2f} €")
    print(f"- Tentatives moyennes (sur victoire) : {avg_attempts:.2f}")


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


def main():
    name_user = input("Je suis Python. Quel est votre pseudo ? ").strip()
    if name_user == "":
        name_user = "Joueur"

    player_stats = recuperer_stats_joueur(name_user)

    if player_stats["games_played"] > 0:
        print(f"\nRebonjour {name_user} !")
        afficher_stats(name_user, player_stats)

    voir_regles = demander_oui_non("Voulez-vous afficher les regles ? (oui/non) : ")
    if voir_regles:
        afficher_regles()

    jouer_partie(name_user, player_stats)
    afficher_stats(name_user, player_stats)
    ok = save_player_stats(name_user, player_stats)
    if not ok:
        print("Attention: echec de sauvegarde MongoDB.")


if __name__ == "__main__":
    main()
