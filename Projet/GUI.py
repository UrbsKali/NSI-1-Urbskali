import pygame
from .morpion import *

is_winner = False


def main():
	"""
	Mainloop pour lancer la fenetre principal et interagir avec l'user
	"""
	surf, width, height = draw_windows()
	run = True
	# Mainloop
	while run:
		# Event loop
		for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 : # si click gauche
					x, y = pygame.mouse.get_pos() # on get la pos de la souris
					if get_case_val(get_case(x,y)) == '' and is_winner == False: # si la case est vide et tant qu'il n'y a pas de gagnant 
						add_case(player_(),get_case(x,y), surf) # alors on ajoute le symbole (player_())

				is_winner = win(surf) # actualiser le gagnant

				# pour quitter la boucle
				if event.type == pygame.QUIT: # si on close la fenetre, on quite la boucle
						run = False 
				for key in pygame.key.get_pressed():
					if key == True:  # si une key est pressed 
							clear() # on clear la fenetre

		
		
	pygame.quit()


