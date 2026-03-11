def demander_oui_non(message):
    while True:
        rep = input(message).strip().lower()
        if rep in ["oui", "o", "yes", "y"]:
            return True
        if rep in ["non", "n", "no"]:
            return False
        print("Reponse invalide. Ecrivez oui ou non.")