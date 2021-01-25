import turtle as tur

def etoile():
	tur.goto(0,0)
	for i in range(20):
		tur.forward(i*10)
		tur.right(144)

def cercle(taille=50, couleur='blue'):
	tur.goto(0,0)
	tur.pencolor(couleur)
	for i in range(34):
		tur.forward(taille)
		tur.left(142)

def carre(longeur,couleur='black'):
	tur.pencolor(couleur)
	for i in range(4):
		tur.forward(longeur)
		tur.right(90)

def triangle(longeur=50,couleur='black'):
	tur.pencolor(couleur)
	for i in range(3):
		tur.forward(longeur)
		tur.right(120)

def frise():
	tur.penup()
	tur.goto(-150, 0)
	for i in range(5):
		tur.pendown()
		carre(10*i, 'blue')
		tur.penup()
		tur.forward(10*i+10)
		tur.pendown()
		triangle(10*i, 'red')
		tur.penup()
		tur.forward(10*i+10)

def frise1():
	tur.penup()
	tur.goto(-150, 0)
	for i in range(5):
		tur.pendown()
		carre(20)
		tur.penup()
		tur.forward(30)

def main():
	frise()