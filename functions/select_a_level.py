import random
from functions.setup_level import get_config_level
from functions.calculate_wins import calculer_gain
from functions.add_int_value import demander_entier

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