from math import *

def archimede(p):
	a, b = 0, 1 # valeurs arbitraires
	n=6
	while (b-a) > 10**(-p):
		a = n * sin( radians(180/n) )
		b = n * tan( radians(180/n) )
		n = n + 1
	return a,b