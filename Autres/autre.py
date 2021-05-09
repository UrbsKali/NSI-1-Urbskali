from random import random 

def main():
	# Aproximation de pi méthode de MonteCarlo
	N = 5000000
	Q = 0
	for i in range(N):
		x = random() ** 2
		y = random() ** 2 
		if x + y < 1.0:
			Q += 1
	return Q/N
