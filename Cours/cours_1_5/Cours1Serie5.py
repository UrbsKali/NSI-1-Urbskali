from random import randrange, shuffle


def trie_insert(liste):
    for i in range(len(liste)):
        tmp = liste[i]
        j = i
        while j > 0 and liste[j - 1] > tmp:
            liste[j] = liste[j - 1]
            j = j - 1
        liste[j] = tmp
    return liste


def trie_insert_decroissnat(liste):
    for i in range(len(liste)):
        tmp = liste[i]
        j = i
        while j > 0 and liste[j - 1] < tmp:
            liste[j] = liste[j - 1]
            j = j - 1
        liste[j] = tmp
    return liste


t = [randrange(0, 100) for i in range(50)]


def is_croissant(liste):
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            return False

    return True


def is_decroissant(liste):
    for i in range(len(liste) - 1):
        if liste[i] < liste[i + 1]:
            return False

    return True


def trie_singe(liste):
    i = 0
    while not is_croissant(liste):
        shuffle(liste)
        i += 1
    return liste


def trie_postal(liste):
    # a = + grand nombre
    # 2n + 2 + n + 1 + n(x+1) + a + 1 = 4n + nx + a + 4
    # O(5n+a)
    maximum = max_(liste)  # 2n + 2
    sorted_list = [0 for i in range(maximum + 1)]  # a + 1
    for val in liste:  # n fois
        sorted_list[val] += 1  # 1
    tmp = []  # 1
    for i in range(len(sorted_list)):  # n fois
        for y in range(sorted_list[i]):  # x fois
            tmp.append(i)  # 1
    return tmp


def max_(arr):
    #2n + 1 dans le pire des cas
    max_ = arr[0]  # 1
    for item in arr:  # n fois
        if item > max_:  # 1
            max_ = item  # 1
    return max_


def main():
    print(is_croissant(tri_selection(t)))


def indice_min(tab, indice_=0):
    tab = tab[indice_:]
    min_ = tab[0]
    index_min = 0
    for index in range(len(tab)):
        if tab[index] <= min_:
            min_ = tab[index]
            index_min = index
    return index_min + indice_


def selection(tab, indice_):
		to_permute = indice_min(tab, indice_)
		tab[indice_], tab[to_permute] = tab[to_permute], tab[indice_]
		return tab

def tri_selection(tab):
	for i in range(len(tab))
		tab = selection(tab,i)
	return tab
