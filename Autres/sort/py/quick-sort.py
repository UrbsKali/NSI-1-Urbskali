def quick_sort(array_to_sort):
    # s'il n'y a pas de valeurs plus ou moins grandes, nous n'avons plus rien à trier
    # le tableau est trié !
    # c'est la condition d'arrêt récursif
    if not array_to_sort:
        return []
    else:
        # sinon, on choisi un pivot 
        # juste le dernier élément de l'array
        pivot = array_to_sort[-1]
        # nous passons en revue le tableau actuel et construisons un tableau 
        # de plus petites valeurs du pivot
        array_of_smaller_values = [value for value in array_to_sort if value < pivot]
        # on passe par le tableau courant (moins le pivot) et on construit un tableau
        # de plus grandes valeurs du pivot
        array_of_bigger_values = [value for value in array_to_sort[:-1] if value >= pivot]
        # nous retournons l'itération actuelle avec un nouveau tableau
        # des valeurs plus petites au début, un pivot au milieu, des valeurs plus grandes à la fin
        return quick_sort(array_of_smaller_values) + [pivot] + quick_sort(array_of_bigger_values)

if __name__ == "__main__":
  quick_sort([1,17,5498,5146,8,15,61,848,15,18,45,18,48,44,1,41,1,21,6,1])

