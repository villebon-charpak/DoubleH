# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:15:21 2018

@author: Haroon
"""

import pygame
from pygame.locals import *

pygame.init()

def Somme(morpion):
	somme = 0
	for k in range(4):
		somme = 0
		for l in range(4):
			somme += morpion[k][l]
			if somme == 3:
				return 1
			if somme == -3:
				return -1

	for l in range(4):
		somme = 0
		for k in range(4):
			somme += morpion[k][l]
			if somme == 3:
				return 1
			if somme == -3:
				return -1

	somme = morpion[0][0] + morpion[1][1] + morpion[2][2]# + morpion[3][3]  

	if somme == 3:
		return 1
	if somme == -3:
		return -1

	somme = morpion[0][3] + morpion[1][2] + morpion[2][1]# + morpion[3][0]
	if somme == 3:
		return 1
	if somme == -3:
		return -1
    
	somme = morpion[1][3] + morpion[2][2] + morpion[3][1]# + morpion[3][0]
	if somme == 3:
		return 1
	if somme == -3:
		return -1

	somme = morpion[2][0] + morpion[1][1] + morpion[0][2]# + morpion[3][0]
	if somme == 3:
		return 1
	if somme == -3:
		return -1

	somme = morpion[0][1] + morpion[1][2] + morpion[2][3]# + morpion[3][0]
	if somme == 3:
		return 1
	if somme == -3:
		return -1

	somme = morpion[1][0] + morpion[2][1] + morpion[3][2]# + morpion[3][0]
	if somme == 3:
		return 1
	if somme == -3:
		return -1

	somme = morpion[1][1] + morpion[2][2] + morpion[3][3]  

	if somme == 3:
		return 1
	if somme == -3:
		return -1

	somme = morpion[1][2] + morpion[2][1] + morpion[3][0]
	if somme == 3:
		return 1
	if somme == -3:
		return -1


	return 0



fenetre = pygame.display.set_mode((930, 930))

#Chargement des images
fond4 = pygame.image.load("plateau4x4.png").convert()
fond = pygame.image.load("plateau3.png").convert()
fondmenu = pygame.image.load("fondcroix.png").convert()
fondinfo = pygame.image.load("help.png").convert()
croix4 = pygame.image.load("Croix4.png").convert_alpha()
croix5 = pygame.image.load("Croix5.png").convert_alpha()
croix = pygame.image.load("Croix.png").convert_alpha()
rond4 = pygame.image.load("Rond4.png").convert_alpha()
rond5 = pygame.image.load("Rond5.png").convert_alpha()
rond = pygame.image.load("Rond.png").convert_alpha()
joueur1 = pygame.image.load("joueur1 losange.png").convert_alpha()
joueur2 = pygame.image.load("joueur2 losange.png").convert_alpha()
#fondcroix = pygame.image.load("fondcroix.png").convert_alpha()

#Definition de la police de charactère
font = pygame.font.Font(None,70)

menu = 1
continuer = 1
jeu = 0
fin = 0
suivant = 1


while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0     #On arrête la boucle


	#Affichage du menu de debut
	while menu:
		for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
			if event.type == QUIT:     #Si un de ces événements est de type QUIT
				menu = 0     #On arrête la boucle
				continuer = 0 
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				if 1<event.pos[1]<2:
					jeu = 1
					joueurs = 1
					menu = 0
				if 550<event.pos[1]<928:
					jeu = 1
					joueurs = 2
					menu = 0
				if 0<event.pos[1]<1:
					continuer = 0
					menu = 0
                    
		#fenetre.blit(fondcroix, (0,0))
		fenetre.blit(fondmenu, (0,0))
		fenetre.blit(joueur1, (50,320)) 
		fenetre.blit(joueur2, (570,320))
		fenetre.blit(font.render("Start Game", 1, (255,255,255)), (330,723))
		fenetre.blit(font.render("Welcome", 1, (255,255,255)), (357,140))
		pygame.display.flip()  

	#On initialise les variables du jeu
	morpion = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	tour = 0

	#Boucle infinie du jeu
	while jeu:
		for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
			if event.type == QUIT:     #Si un de ces événements est de type QUIT
				jeu = 0      #On arrête la boucle
				continuer = 0 

			#Recheche de la cible du clic
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				#On recherche la colonne k
				for k in range(4):
					if k*234 < event.pos[0] < (k+1)*234:
						#On recherche la ligne l
						for l in range(4):
							if l*234 < event.pos[1] < (l+1)*234:
								signe = morpion[k][l]
								#On met la croix ou le rond en fonction du tour qui se joue
								if signe == 0:
									if tour % 2 == 0:
										morpion[k][l]=1
									else:
										morpion[k][l]=-1
									tour += 1

		somme = Somme(morpion)
		if somme != 0 or tour == 16: # On detecte si le jeu est fini
			fin = 1 # On enclenche le menu de fin
			jeu = 0 # On arrete le jeu

		#Affichage du tableau de jeu de morpion
		fenetre.blit(fond4, (0,0))
		for i,col in enumerate(morpion):
			for j,ligne in enumerate(col):
				if ligne == 1:
					fenetre.blit(croix4,(i*234,j*234))
				if ligne == -1:
					fenetre.blit(rond4,(i*234,j*234) )
		#fenetre.blit(font.render("Morpion", 1, (0,0,0)), (0,400))
		pygame.display.flip()

	while fin:
		for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
			if event.type == QUIT:     #Si un de ces événements est de type QUIT
				fin = 0      #On arrête la boucle
				continuer = 0 
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				if 0<event.pos[0]<270:
					jeu = 1
					fin = 0
					menu = 0
				if 630 < event.pos[0] < 928:
					jeu = 0
					fin = 0
					menu = 1

		fenetre.blit(fondmenu, (0,0))
		if somme == 1:
			fenetre.blit(font.render("Croix a gagné", 1, (255,255,255)), (310,150))
		if somme == -1:
			fenetre.blit(font.render("Rond a gagné", 1, (255,255,255)), (320,150))
		if tour == 16:
			fenetre.blit(font.render("Egalité", 1, (255,255,255)), (380,150))
		fenetre.blit(font.render("Rejouer", 1, (255,255,255)), (120,430))
		fenetre.blit(font.render("Menu", 1, (255,255,255)), (670,430))
		fenetre.blit(font.render("Suivant", 1, (255,255,255)), (370,720))
		pygame.display.flip()
        
