"""
20/20

Bravo.
Revoyez absolument l'usage de la méthode join qui n'est pas du tout utilisé comme il faudrait.
La fonction decode_cesar peut être codée de façon beaucoup plus simple.
"""


alphabet = "abcdefghijklmnopqrstuvwxyz"
# 1 ) Hello World => Khoor Zruog

def codage_lettre(clettre, idecalage=3):
	"""
	Retourne le codage ceasar de la lettre avec un décalage au choix \n
	:arg str: lettre devant être modifier \n
	:arg int: décalage devant être utiliser, par deffaut 3 \n 
	"""
	if type(clettre) != str or type(idecalage) != int or len(clettre) > 1:
		raise TypeError
	else:
		i = alphabet.index(clettre.lower())+idecalage
		while i > len(alphabet):
			i -= len(alphabet)
		return alphabet[i]

def code_ceasar(strMessage, iDecalage=3):
	"""
	Retourne le codage ceasar du texte avec un décalage au choix, conserve la casse et les caratères spéciaux \n
	:arg str: texte devant être modifier \n
	:arg int: décalage devant être utiliser, par deffaut 3 \n 
	"""
	tmp = ""
	tmp_txt = list(strMessage) #INUTILE
	for val in tmp_txt:
		if val.lower() not in alphabet:
			tmp += val
			continue
		if val.isupper():
			tmp += tmp.join(codage_lettre(val, iDecalage).upper())
		else:
			tmp += tmp.join(codage_lettre(val, iDecalage))
	return tmp
# 4 ) Oui

def decode_ceasar(strMessage, iDecalage=3):
	"""
	Décode un code ceasar strMessage avec iDecalage de decalage, par deffaut 3 \n 
	:arg str: texte devant être décodé \n
	:arg int: décalage devant être utiliser, par deffaut 3 \n 
	"""
	tmp = ""
	tmp_txt = list(strMessage)
	for val in tmp_txt:
		if val.lower() not in alphabet:
			tmp += tmp.join(val)
			continue
		if val.isupper():
			tmp += tmp.join(codage_lettre(val, -iDecalage).upper())
		else:
			tmp += tmp.join(codage_lettre(val, -iDecalage))
	return tmp

def code_Vigenere(strMessage, strCle):
	"""
	Encode un message en viginaire avec comme paramètre strMessage le text à encoder et strCle la clé
	"""
	cle_bonne_longeur = get_cle_viginaire(strMessage, strCle)
	tmp = ""
	tmp_txt = list(strMessage)
	espace = 0
	for i in range(len(tmp_txt)):
		val = tmp_txt[i]
		iDecalage = alphabet.index(cle_bonne_longeur[i- espace].lower()) 
		if val.lower() not in alphabet:
			espace += 1
			tmp += tmp.join(val)
			continue
		if val.isupper():
			tmp += tmp.join(codage_lettre(val, iDecalage).upper())
		else:
			tmp += tmp.join(codage_lettre(val, iDecalage))
	return tmp

def decode_Vigenere(strMessage, strCle):
	"""
	decode un message en viginaire avec comme paramètre strMessage le text à encoder et strCle la clé
	"""
	cle_bonne_longeur = get_cle_viginaire(strMessage, strCle)
	tmp = ""
	espace = 0
	tmp_txt = list(strMessage)
	for i in range(len(tmp_txt)):
		val = tmp_txt[i]
		iDecalage = alphabet.index(cle_bonne_longeur[i- espace].lower()) 
		if val.lower() not in alphabet:
			tmp += tmp.join(val)
			espace += 1 
			continue
		if val.isupper():
			tmp += tmp.join(codage_lettre(val, -iDecalage).upper())
		else:
			tmp += tmp.join(codage_lettre(val, -iDecalage))
	return tmp

def find_decalage(messsage):
	"""
	Trouve le décalage d'un message crypté en ceasar
	"""
	list_msg = list(messsage)
	max_ = 0
	tmp = ""
	for val in alphabet:
		if max_ < list_msg.count(val):
			tmp = val
			max_ = list_msg.count(val)
	
	if tmp == "e":
		return 0
	else:
		return alphabet.index(tmp) - 4

def get_cle_viginaire(message, cle):
	"""
	créé une clé utilisable pour le codage/décodage du viginaire
	"""
	cle_bonne_longeur = ""
	if len(cle) == len(message):
		cle_bonne_longeur = cle
	elif len(cle) <= len(message):
		i = 0
		while not(len(cle_bonne_longeur) == len(message)):
			if i >= len(cle):
				i -= len(cle)
			cle_bonne_longeur += cle[i]
			i+=1
	else:
		for i in range(len(message)):
			cle_bonne_longeur += cle[i]
	return cle_bonne_longeur


def bruteforce_viginaire(message):
	pass


def main():
	print(find_decalage("QLBKP, H TPKP, KLZ YLUMVYAZ CPLUULUA WHY SH TLY".lower()))
	print(decode_ceasar("“QLBKP, H TPKP, KLZ YLUMVYAZ CPLUULUA WHY SH TLY”.", 7))
	print(code_Vigenere("CHIFFRE DE VIGENERE", "BACHELIER"))
	print(decode_Vigenere("DHKMJCM HV WIILRPZI", "BACHELIER"))


