import time
import os


def clear_console():
    # mac/linux = clear, windows = cls
    os.system("cls" if os.name == "nt" else "clear")


def effet_victoire():
    frame_up = [
        "   \\o/    \\o/    \\o/   ",
        "    |      |      |    ",
        "   / \\    / \\    / \\   ",
    ]

    frame_down = [
        "    o      o      o    ",
        "   /|\\    /|\\    /|\\   ",
        "   / \\    / \\    / \\   ",
    ]

    print("YOUPIIII !!!")
    for _ in range(6):  # nombre de mouvements
        clear_console()
        print("YOUPIIII !!!")
        print("\n".join(frame_up))
        time.sleep(0.25)

        clear_console()
        print("YOUPIIII !!!")
        print("\n".join(frame_down))
        time.sleep(0.25)

    print("Bravo, tu as gagne !")