from random import randrange, shuffle

t = [randrange(0,100) for i in range(50)]

def is_croissant(liste):
	for i in range(len(liste)-1):
		if liste[i] > liste[i+1]:
			return False

	return True


def trie_singe(liste):
	i=0
	while not is_croissant(liste):
		shuffle(liste)
		print(i)
		i+=1
	return liste
		

def trie_insert(liste):
	pass



def main():
	print(is_croissant(trie_singe()))