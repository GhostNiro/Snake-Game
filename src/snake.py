import pygame
from src.constants import *

class Snake :
    def __init__(self, x , y):
        self.body = [(x,y)] #liste de tuples qui representent les cases que le snake occupe, le premier tuple correspond aux coordonnees de la tete
        self.direction = (1,0) #par defaut le snake se deplace vers la droite

    def set_direction(self, new_dir) :
        '''fonction qui permet de changer la direction du snake'''
        #on ne peut pas faire un demi-tour
        if ( new_dir[0], new_dir[1]) != (- self.direction[0], -self.direction[1]) :
            self.direction = new_dir
    
    def update(self):
        '''fonction qui va mettre a jour la position du snake'''
        #on calcule les nouvelles coordonnees de la tete du snake
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        #on ajoute la nouvelle tete au debut de la liste
        self.body.insert(0, new_head)
        #on supprime la queue du snake
        self.body.pop()

    def draw(self, screen):
        '''fonction qui va dessiner le snake a l'ecran'''
        for i, (x,y) in enumerate(self.body):
            if i == 0 :
                color = SNAKE_HEAD_COLOR
            else :
                color = SNAKE_BODY_COLOR
                
            pygame.draw.rect(screen, color, (x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))