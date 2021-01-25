import pygame

game = [['','',''],['','',''],['','','']] # représentation de la partie 

joueur = "O" # car il y a une inversion au début


def draw_windows(r = 126, g = 161, b = 201, width=600, height=600):
	"""
	dessine la fenetre principal, aucun paramètre n'est nessecaisre
	:param r:
	:param g:
	:param b:
	:param width:
	:param height:
	:return: surface, et dimension
	"""
	surf = pygame.display.set_mode((width,height))
	surf.fill(pygame.Color(r,g,b))
	pygame.draw.line(surf,(0,0,0),(width/3,0),(width/3, height),2)
	pygame.draw.line(surf,(0,0,0),(2*width/3,0),(2*width/3,height),2)
	pygame.draw.line(surf,(0,0,0),(0,height/3),(width,height/3),2)
	pygame.draw.line(surf,(0,0,0),(0,2*height/3),(width,2*height/3),2)
	pygame.display.flip()
	return surf, width, height


def add_case(symbole, case, surface):
    """
    Pour rajouter un symbole sur le tableau game
    """
    if case < 3:
        if game[0][case] == '':
            game[0][case] = symbole
    elif 3 <= case < 6:
        if game[1][case - 3] == '':
            game[1][case - 3] = symbole
    elif 6 <= case < 9:
        if game[2][case - 6] == '':
            game[2][case - 6] = symbole
    draw_symbole(symbole, case, surface)
    pygame.display.flip()
    return game


def get_case_val(case):
    """
    Pour get un symbole sur le tableau game
    """
    if case < 3:
        return game[0][case]
    elif 3 <= case < 6:
        return game[1][case - 3]
    elif 6 <= case < 9:
        return game[2][case - 6]


def player_():
    """
    Pour get le joueur actuel
    """
    global joueur
    if joueur == "O":
        joueur = "X"
        return "X"
    elif joueur == "X":
        joueur = "O"
        return "O"


def get_case(x, y):
	"""
	Renvoie la case en fonction des coordonées
	:param x:int
	:param y: int
	:return: int la case
	"""
	# Rangée 1
	if x < 200 and y < 200:
			return 0
	if 200 < x < 400 and y < 200:
			return 1
	if 400 < x < 600 and y < 200:
			return 2

	# Rangée 2
	if x < 200 and 200 < y < 400:
			return 3
	if 200 < x < 400 and 200 < y < 400:
			return 4
	if 400 < x < 600 and 200 < y < 400:
			return 5

	# Rangée 3
	if x < 200 and 400 < y < 600:
			return 6
	if 200 < x < 400 and 400 < y < 600:
			return 7
	if 400 < x < 600 and 400 < y < 600:
			return 8


def clear():
	"""
	Clear le tableau pour lancer une nouvelle partie, ne renvoie rien
	"""
	global game
	global joueur
	draw_windows()
	game = [['','',''],['','',''],['','','']]
	joueur = "O"


def win(surface):
	"""
	Determine si un joueur a gagné, si oui dessine le symbole gagnant en rouge, ne renvoie rien
	:param surface: surface pygame
	"""
	if game[0] == ['X','X','X']:
			couleur_rouge("X", surface, 0,1,2)
	elif game[1] == ['X','X','X']:
			couleur_rouge("X", surface, 3,4,5)
	elif game[2] == ['X','X','X']:
			couleur_rouge("X", surface, 6,7,8)

	elif game[0] == ['O','O','O']:
			couleur_rouge("O", surface, 0,1,2)
	elif game[1] == ['O','O','O']:
			couleur_rouge("O", surface, 3,4,5)
	elif game[2] == ['O','O','O']:
			couleur_rouge("O", surface, 6,7,8)

	elif game[2][1] == 'O' and game[1][1] == 'O' and game[0][1] == 'O':
			couleur_rouge("O", surface, 1,4,7)
	elif game[2][0] == 'O' and game[1][0] == 'O' and game[0][0] == 'O':
			couleur_rouge("O", surface, 0,3,6)
	elif game[2][2] == 'O' and game[1][2] == 'O' and game[0][2] == 'O':
			couleur_rouge("O", surface, 2,5,8)

	elif game[2][1] == 'X' and game[1][1] == 'X' and game[0][1] == 'X':
			couleur_rouge("X", surface, 1,4,7)
	elif game[2][0] == 'X' and game[1][0] == 'X' and game[0][0] == 'X':
			couleur_rouge("X", surface, 0,3,6)
	elif game[2][2] == 'X' and game[1][2] == 'X' and game[0][2] == 'X':
			couleur_rouge("X", surface, 2,5,8)

	elif game[2][0] == 'X' and game[1][1] == 'X' and game[0][2] == 'X':
			couleur_rouge("X", surface, 2,4,6)
	elif game[2][2] == 'X' and game[1][1] == 'X' and game[0][0] == 'X':
			couleur_rouge("X", surface, 0,4,8)

	elif game[2][2] == 'O' and game[1][1] == 'O' and game[0][0] == 'O':
			couleur_rouge("O", surface, 0,4,8)
	elif game[2][0] == 'O' and game[1][1] == 'O' and game[0][2] == 'O':
			couleur_rouge("O", surface, 2,4,6)
	else:
		return False

def draw_symbole(symbole, case, surface, color=(0,0,0)):
	"""
	dessine un symbole ( X ou O ) sur la surface pygame, ne renvoie rien
	:param symbole: str le symbole à dessine
	:param case: int la case sur laquel dessinée
	:param surface: surface pygame
	:param color: tuple<int> couleur rgb
	"""
	if symbole == "O":
			if case < 3:
					draw_o(case*200+100, 100, surface, color)
			elif 3 <= case < 6:
					draw_o((case-3)*200+100, 300, surface, color)
			elif 6 <= case < 9:
					draw_o((case-6)*200+100, 500, surface, color)
	else:
			if case < 3:
					draw_x(case*200+100, 100, surface, color)
			elif 3 <= case < 6:
					draw_x((case-3)*200+100, 300, surface, color)
			elif 6 <= case < 9:
					draw_x((case-6)*200+100, 500, surface, color)


def draw_x(x, y, surface, color=(0,0,0)):
	"""
	Dessine un X sur la surface pygame, ne renvoie rien
	:param x: int coordonné x
	:param y: int coordonné y
	:param surface: surface pygame
	:param color: tuple<int> optionel, change la couleur du X
	"""
	pygame.draw.line(surface,color,(x - 80,y - 80),(x + 80, y + 80),25)
	pygame.draw.line(surface,color,(x + 80, y - 80),(x - 80, y + 80),25)
  

def draw_o(x, y, surface, color=(0,0,0)):
	"""
	Dessine un O sur la surface pygame, ne renvoie rien
	:param x: int coordonné x
	:param y: int coordonné y
	:param surface: surface pygame
	:param color: tuple<int> optionel, change la couleur du O
	"""
	pygame.draw.circle(surface, color, (x, y), 80)
	pygame.draw.circle(surface,(126,161,201),(x, y), 60)


def couleur_rouge(symbole, surface,*cases):
	"""
	Change la couleur des cases, ne renvoie rien
	:param symbole: str le symbole X ou O
	:param surface: surface pygame
	:param cases: int les cases sur lequel il faut dessiner
	"""
	for case in cases:
		draw_symbole(symbole,case,surface,(255,0,0))

	pygame.display.flip()
