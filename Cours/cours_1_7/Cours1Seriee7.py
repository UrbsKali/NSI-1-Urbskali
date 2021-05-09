def main():
    # on va utiliser un timestamp depuis 00h00 pour les heures
    events = [
        {
            "début": 32400,  # 9h00
            "fin": 39600,  # 11h00
            "nom": "Match de foot 1"
        },
        {
            "début": 39900,  # 11h05
            "fin": 47100,  # 13h05
            "nom": "Match de foot 2"
        },
        {
            "début": 39300,  # 10h55
            "fin": 40500,  # 11h15
            "nom": "Match de ping-pong"
        },
        {
            "début": 34200,  # 9h30
            "fin": 39600,  # 11h00
            "nom": "Match de basket"
        },
    ]

    autre = [{'début': 32400, 'fin': 39600, 'nom': 'Match de foot 1', 'compatible': [0], 'id': 3}, {'début': 34200, 'fin': 39600, 'nom': 'Match de basket', 'compatible': [0], 'id': 2}, {'début': 39300, 'fin': 40500, 'nom': 'Match de ping-pong', 'compatible': [], 'id': 1}, {'début': 39900, 'fin': 47100, 'nom': 'Match de foot 2', 'compatible': [], 'id': 0}]

    return gymnase(events)
    #return choose_compatible(autre[0]["compatible"],autre)


def rendu_monnai(argent):
    pieces = [200, 100, 50, 20, 5]
    argent *= 100
    result = []
    for piece in pieces:
        result.append(argent // piece)
        argent = argent % piece
    return result


def sac_a_dos(objs, taille):
    poids_total = 0
    valeur_total = 0
    builtin = []
    obj = []
    for i in range(len(objs)):
        for j in range(objs[i]["nombre"]):
            obj.append({
                "poids": objs[i]["poids"],
                "valeur": objs[i]["valeur"],
                "vm": valeur_massique(objs[i])
            })
    obj = sorted(obj, reverse=True, key=lambda d: d.get('vm'))
    for item in obj:
        if item['poids'] + poids_total > taille:
            continue
        else:
            poids_total += item['poids']
            valeur_total += item['valeur']
            builtin.append(item)
    return builtin, poids_total, valeur_total


def valeur_massique(dict_):
    return round(dict_["valeur"] / dict_["poids"], 3)


def est_present(liste, item_to_check):
    for item in liste:
        if item == item_to_check:
            return True
    return False


def nb_present(liste, item_to_check):
    compteur = 0
    for item in liste:
        if item == item_to_check:
            compteur += 1
    return compteur


def summ(liste):
    total = 0
    longeur = 0
    for item in liste:
        total += item
        longeur += 1
    return total / longeur


def recherche_dichotomique(liste, nombre):
    """
	Fonction recursive (qui s'appelle elle-meme), pour rechercher un valeur dans un liste trie dans l'ordre croissant
	"""
    if not liste:
        # Condition d'arret de la boucle recursive
        return False
    elif len(liste) == 1:
        # Condition d'arret de la boucle recursive
        return liste[0] == nombre
    else:
        milieu = len(liste) // 2
        pivot = liste[milieu]
        small_list = liste[:milieu]
        big_list = liste[milieu:]
        return recherche_dichotomique(
            small_list if pivot > nombre else big_list, nombre)


def gymnase(events):
    # je suis parti trop loin ?
    # en plus il n'est pas optimisé
		early_event = sorted(events, reverse=True, key=lambda d: d.get('début'))
		result = []
		early_event = list_compatible(early_event)
		sorted_event = sorted(sorted(early_event,
													reverse=True,
													key=lambda g: g.get('compatible')), key=lambda g : g.get("début"))
	
		result.append(sorted_event[0])
		tmp = choose_compatible(
								sorted_event[0]["compatible"], early_event)
		for i in range(len(sorted_event)):
				if sorted_event[i]['id'] == tmp:
						print(tmp)
						tmp = choose_compatible(
								sorted_event[i]["compatible"], early_event)
						result.append(sorted_event[i])

		return result


def list_compatible(early_event):
    for event in range(len(early_event)):
        tmp = []
        for event_ in range(len(early_event)):
            if event_ == event:
                continue
            if early_event[event].get("fin") <= early_event[event_].get(
                    "début"):
                tmp.append(event_)
        early_event[event]["compatible"] = tmp
        early_event[event]["id"] = event
    return early_event


def choose_compatible(compatibles, events):
		if compatibles == []:
				return 0
		tmp = []
		for i in compatibles:
				tmp.append({"nb": len(events[i]["compatible"]), "id": i})
		
		return sorted(tmp, reverse=True, key=lambda h: h.get("nb"))[0]["id"]
