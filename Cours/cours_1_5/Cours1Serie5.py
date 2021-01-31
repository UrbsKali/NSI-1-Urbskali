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


t = [randrange(0, 100) for i in range(50)]


def is_croissant(liste):
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            return False

    return True


def trie_singe(liste):
    i = 0
    while not is_croissant(liste):
        shuffle(liste)
        i += 1
    return liste


def trie_postal(liste):
    pass


def main():
    print(is_croissant(trie_insert(t)))
