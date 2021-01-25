from random import randint, choice
from math import sqrt

def printTab(tab):
    for ligne in tab:
      for ele in ligne:
        print(ele, end="\t")
      print()

def main() :
  # Exos 1
  L = [i for i in range(100)]

  # Exos 2
  L = [i for i in range(200) if i % 2 == 0]

  # Exos 3
  L = [i for i in range(100) if i % 2 == 0]

  # Exos 3
  L = [i for i in range(100) if i % 2 == 0]

  # Exos 3 
  L = [i for i in range(100) if i%2 == 0]

  # Exos 4 
  L = [i**3 for i in range(100) if 10 <= i**3 <= 20]

  # Exos 5 
  L = [True] * 10000
  L = [True for i in range(10000)]
  for i in range(10000):
    L.append(True)

  # Exos 6
  L = [i for i in range(2002) if i%4 == 0 and ((i%100 == 0 and i%400 == 0) or i%100 != 0)]
  
  #Exos 7
  L = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

  #Exos 8
  Lun = L[1:4]
  Lde = L[-4:-1]
  Ltr = L[::2]
  Lqu = L[:2:-1]
  Lci = L[10::2]

  #Exos 9
  L = [0,1,2,3,4,5,6,7,8,9]
  Lun = [n%2 for n in L]
  Lde = [n for n in L if n > 4]
  Ltr = [n**2 for n in L if n < 4]
  Lqu = [n*4 for n in L if n%2==0]
  Lci = [n if n%2==0 else n**2 for n in L]
  
  #Exos 10
  L = ["Ugo","Samuel"]
  def classe () :
    inputstr = input("Nom ? : ").lower()
    for val in L :
      if inputstr == val.lower():
        print("cette eleve fait partie de la liste")
        break
  #Exos 11 
  t1 = [31, 29,31,30,31,30,31,30,31,30,31,30]
  t2 = "Janvier Février Mars Avril Mai Juin Juillet Aout Septembre Octobre Novembre Decembre".split(" ")   
  t3 = []
  for i in range(len(t1)):
    t3.append(t2[i])
    t3.append(t1[i])

  #Exos 12 
  L = [1,64,24,1,5,8,23]
  x = L[0]
  for val in L:
    if val >= x:
      x = val
  
  #Exos 13
  """" 
  L = [1,2,3,4,5,6,7,8,9,10]
  Lchoix = []
  first = []
  for i in range(3):
    x = choice(L)
    first += [x]
    L.remove(x)
    Lchoix.append(int(input("Choix du cheval {0} : ".format(i+1))))
  win = 0
  for i in range(len(first)):
    for val in Lchoix:
      if first[i] ==  val:
        win += 1 
  if win == 3 and first[0] == Lchoix[0] and first[1] == Lchoix[1] and first[2] == Lchoix[2]:
    print("Dans L'ordre")
  elif win == 3:
    print("Dans le desorde")
  else:
    print("Perdu !\nNb de Win : ", win )
      """

  ### Exercices Tuples ###

  # Exos 1

  def stat(L):
    return (sum(L), min(L), max(L))

  #Exos 2

  def trinome(a,b,c):
    delta = b**2 - (4*a*c)
    if delta > 0:
      return (2, (-b-sqrt(delta))/(2*a), (-b+sqrt(delta))/(2*a))
    elif delta == 0:
      return (1, -b/(2*a))
    else:
      return (0) 


  ### Utilisation et Manipulation des listes ###

  """inventaire = [("pommes", 22),("melon",4),("poires",18),("fraises",76),("prunes",51)]
  for 
    qu = inventaire[i][2]
  """


  ### Page 20-21 feuille 2 Exercices d'application str ###

  # a )
  """suffixe = 'ack'
  prefix = "JKLMNOPQ"
  for i in range(len(prefix)):
    print(prefix[i:i+1] + suffixe)
  """

  # b )

  def Table (n) :
    for i in range(1,11):
      print("{} * {} = {}".format(n, i, n*i))

  # c ) 

  def inverse(chaine, * chaines):
    print(chaine[::-1])
    for val in chaines:
      print(val[::-1])

  # d ) 

  def trie(chaine):
    group1 = "a b c d e f".split(" ")
    group2 = " g h i j k l m n o p".split(" ")
    if chaine[0].lower() in group1:
      print("groupe 1")
    elif chaine[0].lower() in group2:
      print("groupe 2")
    else:
      print("groupe 3")

  # e ) 

  def changement(chaine):
    removable = [" ", "a", "e", "u", 'v', 'y']
    tmp = ""
    for lettre in chaine:
      if not lettre in removable:
        tmp += lettre 
    
    print(tmp)

  # f ) 

  def replace(chaine):
    return chaine.replace(" ", "_")


  ### Tableau ###


  # f ) 

  """tab = [[0]*5 for i in range(5)]

  for i in range(5):
    tab[i][i] = 1

  tab = [[0]*5 for i in range(5)]

  for i in range(5):
    for j in range(5):
      tab[i][j] = 1 if i+j>3 else 0

  tab = [[0]*5 for i in range(5)]

  for i in range(5):
    for j in range(5):
      tab[i][j] = i*j

  tab = [[0]*5 for i in range(5)]

  
  
  for i in range(5):
    for j in range(5):
      tab[i][j] = (i+1)*(j+1)
  printTab(tab)
  """

  

  
