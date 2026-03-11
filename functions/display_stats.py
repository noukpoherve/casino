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
