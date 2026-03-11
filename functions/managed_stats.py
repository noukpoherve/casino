from db import load_player_stats, save_player_stats

from datetime import datetime

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