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