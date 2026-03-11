from db import save_player_stats
from functions.display_rules import afficher_regles
from functions.managed_stats import recuperer_stats_joueur
from functions.say_yes_or_no import demander_oui_non
from functions.display_stats import afficher_stats
from functions.play_game import jouer_partie


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
