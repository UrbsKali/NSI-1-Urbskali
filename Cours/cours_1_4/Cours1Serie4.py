import csv
from collections import namedtuple


def lecture_csv(nom_du_fichier="villes.csv"):
	"""
	Lit un fichier csv et return une liste de liste contenant les éléments du fichier
	:param nom_du_fichier: type str: nom du fichier csv
	:return: type list<list>: avec les informations
	"""
	fichier_csv = open(f'/home/runner/NSI-1-Urbain/Cours/cours_1_4/{nom_du_fichier}', 'r')
	content = csv.reader(fichier_csv, delimiter=";")
	header = next(content)

	elem = list()
	for ligne in content:
		elem.append(ligne)

	fichier_csv.close()

	return elem, header


def lecture_csv_dict(nom_du_fichier="villes.csv"):
	"""
	Lit un fichier csv et return une liste de dict contenant les éléments du fichier, avec comme indice le nom de la columne 
	:param nom_du_fichier: type str: nom du fichier csv
	:return: type list<dict>: avec les informations
	"""
	fichier_csv = open(f'/home/runner/NSI-1-Urbain/Cours/cours_1_4/{nom_du_fichier}', 'r')
	content = csv.DictReader(fichier_csv, delimiter=";")

	elem = list()
	for ligne in content:
		elem.append(ligne)

	fichier_csv.close()

	return elem




def lecture_csv_nt(nom_du_fichier="malaria.csv", titre="Patient"):
	"""
	Pour transformer un fichier csv en une liste de tuple nommé
	:param nom_du_fichier: type str: nom du fichier csv
	:return: type list<namedtuple>: avec les informations
	"""
	content, header = lecture_csv(nom_du_fichier)
	nt = namedtuple(titre, header)
	elem = []
	for i in range(len(content)):
		elem.append(nt(*content[i][:len(header)]))
	return elem, nt

tabac = namedtuple('Patient',['Id', 'Sexe', 'Age', 'Tension', 'Fume'])

def fumeur(nom_du_fichier="tabacco.csv"):
	"""
	Exos page 5 sur les fumeurs 
	:param nom_du_fichier: type str: nom du fichier csv
	:return: type list: avec les informations
	"""
	content = lecture_csv_dict(nom_du_fichier)

	elem = list()
	for ligne in content:
		elem.append(tabac(ligne['ID'], ligne['sexe'], int(ligne['age']), float(ligne['tension']), ligne["fume"]))
		
	oui = 0
	non = 0
	for Patient in [n for n in elem if n.Tension > 140 and n.Fume =="oui"]:
		oui += 1
	for Patient in [n for n in elem if n.Tension > 140 and n.Fume =="non"]:
		non += 1
	
	return f"patient non-fumeur soufrant d'hypertension : {non} \npatient fumeur soufrant d'hypertension : {oui}"

def moy(L):
	return sum(L)/len(L)
	
malaria = namedtuple('Patient',['Id', 'Age', 'Sexe', 'Poids', 'Temp', 'Hbconc', 'moustiquaire', 'malaria'])

def malaria(nom_du_fichier="malaria.csv"):
	"""
	Exos sur la malaria Page 6
	:param nom_du_fichier: type str: nom du fichier csv
	:return: type list: avec les informations
	"""
	fichier_csv = open(f'/home/runner/NSI-1-Urbain/Cours/cours_1_4/{nom_du_fichier}', 'r')
	content = csv.DictReader(fichier_csv, delimiter=",")

	elem = list()
	for ligne in content:
		elem.append(malaria(ligne['id'], ligne['age'], str(ligne['sex']), ligne['weight'], ligne["temp"], float(ligne['hbConc']), ligne['bednetuse'], ligne['malaria']))
		
	fichier_csv.close()
	oui = []
	non = []
	for Patient in [n for n in elem if n.malaria == "positive"]:
		oui.append(Patient.Hbconc)
	for Patient in [n for n in elem if n.malaria != "positive"]:
		non.append(Patient.Hbconc)

	return f"Negative : {moy(non)}\nPositive : {moy(oui)}"
	