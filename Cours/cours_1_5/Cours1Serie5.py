from random import randrange

t = [randrange(0,100) for i in range(50)]

def is_croissant(liste):
	for i in range(len(liste)):
		if liste[i] > liste[i+1]:
			return False

	return True

