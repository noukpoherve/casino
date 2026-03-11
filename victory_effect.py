import time

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
      
        print("YOUPIIII !!!")
        print("\n".join(frame_up))
        time.sleep(0.25)

        print("YOUPIIII !!!")
        print("\n".join(frame_down))
        time.sleep(0.25)

    print("Bravo, tu as gagne !")