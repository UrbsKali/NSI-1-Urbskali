"""
Même si votre réponse à la Q.3 était juste, il y a une erreur dans votre programme qui répond à la Q. 3: Imaginez qu'il y ait seulement 2 prénoms: (Gabriel: 20, et Marie: 15) Quelle est la réponse donnée par votre programme?
Quant au 6., vous pourriez trouver une réponse plus efficace.
"""

import Cours.cours_1_4.Cours1Serie4 as cs
import matplotlib.pyplot as plt



# Le délimiteur est le point virgule
# ligne : 652058
# columne : 4
# sexe;preusuel;annais;nombre
# int; str; int; int
# 1 ou 2; prenom; 1900-2019; 0-90000000
importer = []
def main():

	# 1)
	content, the_nt = cs.lecture_csv_nt('nat2019.csv', "Prenom")
	content = [n for n in content if n.preusuel != "_PRENOMS_RARES"]

	for n in content:
		try:
			sexe = int(n.sexe)
			annais = int(n.annais) if n.annais != "XXXX" else 0
			nombre = int(n.nombre)
			importer.append(the_nt(sexe, n.preusuel,annais,nombre))
		except:
			print(n)
	"""

	#	2)
	for n in content:
		if n.annais == '2005':
			if n.preusuel == "URBAIN":
				print(f"Le Prenom Urbain a été attribué {n.nombre} fois en 2005")


	#	3)
	name1 = ""
	max1 = 0
	max2 = 0 
	name2 = ""
	for n in content:
		if int(n.nombre) >= max1 and n.annais == "2019":
			max1 = int(n.nombre)
			name1 = n.preusuel
			max2 = max1
			name2 = name1
		if int(n.nombre) > max2 and int(n.nombre) < max1 and n.annais == "2019":
			max2 = int(n.nombre)
			name2 = n.preusuel

	print(f"Le 1er prenom de 2019 est {name1} avec {max1} occurance\nLe 2e prenom de 2019 est {name2} avec {max2} occurance ")
	"""

	# 4)

	THE_dict = {} # name : occurance
	for i in range(len(content)):
		n = content[i]
		if n.preusuel not in THE_dict.keys():
			THE_dict.update({n.preusuel : int(n.nombre)})
		else:
			THE_dict.update({n.preusuel : int(n.nombre)+THE_dict[n.preusuel]})

	"""
	#	5)
	name1 = ""
	max1 = 0
	max2 = 0 
	name2 = ""
	for nom, nombre in THE_dict.items():
		if int(nombre) >= max1:
			max1 = int(nombre)
			name1 = nom
			max2 = max1
			name2 = name1
		if int(nombre) > max2 and int(nombre) < max1:
			max2 = int(nombre)
			name2 = nom

	print(f"Le 1er prenom de tt est {name1} avec {max1} occurance\nLe 2e prenom de tt est {name2} avec {max2} occurance ")
	"""

	# 6 )
	
	y = [n.nombre for n in content if n.annais != "XXXX" and n.preusuel == "URBAIN"]
	annes = [n.annais for n in content if n.annais != "XXXX" and n.preusuel == "URBAIN"]
	print(len(y))
	plt.plot(annes, y)
	plt.show()
