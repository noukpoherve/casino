from functions.add_int_value import demander_entier


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
