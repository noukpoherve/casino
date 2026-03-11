import time

def effet_victoire():
    print("\n" + "=" * 40)
    print("        *  *  *  YOUPIIII  *  *  *")
    print("            \\o/   \\o/   \\o/")
    print("             |     |     |")
    print("            / \\   / \\   / \\")
    print("      + + +  BRAVO, TU AS GAGNE !  + + +")
    for i in range(3):
        print("*" * (10 + i * 5))
        time.sleep(0.1)
    print("=" * 40 + "\n")