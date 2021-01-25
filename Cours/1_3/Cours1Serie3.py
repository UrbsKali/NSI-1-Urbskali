from math import sqrt

def printTab(tab):
    for ligne in tab:
      for ele in ligne:
        print(ele, end="\t")
      print()

def main():

	# 1 P 34
	def multiple(nombre):
		for i in range(10):
			print(nombre*i, end="\t")
		print()

	# 2 P 34
	def multiple_pair(nombre):
		for i in range(0,40, 2):
			print(nombre*i, end="\t")
		print()

	# 3 P 34
	def eeeeeeeee(text):
		nb = 0
		for i in range(len(text)):
			if text[i] == "e":
				nb += 1
		print(nb)
	
	# 4 P 34
	def atox(text):
		print(text.replace("a", "x"))

	# 5 P 34
	def multiple_180(nombre):
		n = [i*nombre for i in range(181) if i*nombre <= 180]
		for val in n:
			print(val)

	# 6 P 34
	def try_again_14():
		yes = False
		while not yes:
			if input("chiffre : ") == "14":
				yes = True
	
	# 7 P 34
	def suite_somme(n):
		x= (n+1)*((n)/2)
		print(x)
	
	# 8 P 34
	def print_50():
		for i in range(51):
			print(i, end=" ")

	# 9 P 34
	def print_50_2():
		for i in range(0,101,2):
			print(i, end=" ")
	
	# 10 P 34 
	def bizzare():
		ligne = 0
		for i in range(0,101, 10):
			print(i, end="\t")
			ligne += 1
			if ligne == 7:
				ligne = 0
				print()
		print()

	# 11 P 34
	def premier(n):
		max_prem = int(sqrt(n))
		premier_ = True
		try_l = [i for i in range(2,max_prem+1)] # il faudrait faire une liste de premiers
		print(try_l)
		for i in try_l:
			if n%i == 0:
				premier_ = False
				break
		print(premier_)
		# Autre méthode : 
	def premiers(n):
		"""
		Créé une liste des nombres premier avant n et check ensuite si n est dans la liste
		:param n: type int devant être checker pour etre 1er
		:return: type Boolean True si premier false sinon
		"""
		if type(n) != int:
			raise TypeError 
		prem=list(range(2,n+1))
		k=2
		nRacine=n**0.5
		while k<nRacine :
				prem=[p for p in prem if p<=k or p%k!=0]
				k=prem[prem.index(k)+1]   # nouveau nombre premier
		return prem[-1] == n

	def palindrome(mot):
		"""
		Check si le mot est un palindrome
		:param mot: type str deveant être checker
		:return: type Boolean True si palindrome false sinon
		"""
		if type(mot) != str:
			raise TypeError 
		return mot == mot[::-1]

	# 12 P 34
	def reste(n, diviseur):
		i = 0
		while n > diviseur:
			n -= diviseur
			i += 1
		print("Quotien :", i, ", Reste :", n)
	
	# 13 P 34 
	def colume(n):
		for lettre in str(n):
			print(lettre)

	# 14 P 34
	def voyelles(tyes):
		voyelles = ["a","e","i","o","u","y"]
		for lettres in tyes:
			if lettres in voyelles:
				print(lettres)

	
	