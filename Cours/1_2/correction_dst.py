### Correction DST ###

  # N°3 :

L = [{"nom":"Robert", "tel":"0603537682"},
  {"nom":"Autre","tel":"0603537682"},
  {"nom":"Autre","tel":"0603537682"},
  {"nom":"Qlq un","tel":"0603537682"},
  {"nom":"Robert","tel":"0603537682"},
  {"nom":"Qlq un","tel":"0603537682"},
  {"nom":"Moi","tel":"0603537682"},]
  
Lplus = [ 
  {"nom":"Alfred", "tel":""},
  {"nom":"Urbain", "tel":""},
  {"nom":"Gabriel", "tel":""},
  {"nom":"Ugo", "tel":""},
  {"nom":"Alfred", "tel":""},
  {"nom":"Ugo", "tel":""},
]


def cherche_et_affiche(liste): 
  nom = []
  double = []
  for item in liste:
    nom.append(item["nom"])
  for i in range(len(nom)):
    tmp = nom.copy()
    tmp.pop(i)
    if nom[i] in tmp:
      if nom[i] not in double:
        double.append(nom[i])
  print(double)