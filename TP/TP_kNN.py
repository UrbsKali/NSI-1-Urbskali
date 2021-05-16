import csv
import matplotlib.pyplot as plt

def main():
	listeDePoints = [[2,3,'R'],[-1,5,'B'],[3,3,'B'],[6,5,'R'],[-2,4,'R'],
									[-1,-1,'B'],[0,0,'R'],[1,1,'B'],[0,2,'B'],[3,0,'R']]
	setosa, virginica, versicolor = donnee_fleur(import_csv())
	
	return k_nn(import_csv(),[5.1,3.5,1.4,0.2], 5)

def distance_point(data, cible):
		tmp = 0
		for i in range(len(data)-1):
				tmp += (data[i]-cible[i])**2
		return tmp


def liste_distance(data_set, cible):
		tmp = []
		for i in range(len(data_set)):
				tmp.append(distance_point(data_set[i], cible))
		return tmp


def pp_voisin(liste_distance):
		return min(enumerate(liste_distance), key=lambda x:x[1])[0]


def classes_k_nn_voisins(data_set, cible, k):
		liste_distances = liste_distance(data_set, cible) 	# liste les distances 
		liste_k_nn_voisins = [] 														# initialise la liste de stockage des k-nn
		for i in range(k):
				indice = pp_voisin(liste_distances)  						# récupère l'index du plus petit element 
				liste_k_nn_voisins.append(data_set[indice][-1])	# récupère la valeur (ex : 'R') du nn
				del liste_distances[indice]											# delete le knn car il a deja ete selectione
				del data_set[indice]														# delete le knn car il a deja ete selectione
		return liste_k_nn_voisins


def dictionaire_classes(classes_k_nn_voisins):
		tmp = {}
		for item in classes_k_nn_voisins:
				tmp[item] = tmp.get(item, 0) + 1
		return tmp


def k_nn(data_set, cible, k):
		return sorted(dictionaire_classes(classes_k_nn_voisins(data_set, cible, k)).items(), reverse=True, key=lambda g: g[1])[0][0]


def import_csv(file="iris_data.csv"):
		csvfile1 = open(f"/home/runner/NSI-1-Urbain/TP/{file}", "r")
		lines1 = csv.reader(csvfile1)
		dataSet1 = list(lines1)
		#On regarde le contenu des 5 premiers éléments de dataSet1
		data = dataSet1[1:] #liste contenant les attributs de chaque fleur du jeu
		for i in range(len(data)):
				for j in range(len(data[i])-1):
						data[i][j] = float(data[i][j])
		return data


def plot_(setosa,virginica,versicolor):
		n=40 #nombres de fleurs de chaque espèce dans le jeu de données
		plt.scatter([setosa[i][0] for i in range(n)],[setosa[i][1] for i in range(n)],c='red',label='setosa')
		plt.scatter([virginica[i][0] for i in range(n)],[virginica[i][1] for i in range(n)],c='blue', label='virginica')
		plt.scatter([versicolor[i][0] for i in range(n)],[versicolor[i][1] for i in range(n)],c='orange', label='versicolor')
		plt.xlabel('longueur sepale' )
		plt.ylabel('largeur sepale')
		plt.legend(loc='upper right')
		plt.show()


def donnee_fleur(donnee):
		virginica = []
		versicolor = []
		setosa = []
		for fleur in donnee:
				if fleur[4] == 'setosa':
						setosa.append(fleur[:4])
				elif fleur[4] == 'virginica':
						virginica.append(fleur[:4])
				else :
						versicolor.append(fleur[:4])
		return setosa, virginica, versicolor




