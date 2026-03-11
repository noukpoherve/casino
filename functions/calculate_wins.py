def calculer_gain(nb_coup, mise):
  if nb_coup == 1:
      return mise * 2
  if nb_coup == 2:
      return mise
  if nb_coup == 3:
      return mise * 0.5
  return mise * 0.25