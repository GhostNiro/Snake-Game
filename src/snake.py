import pygame
from src.constants import TAILLE_CASE, SNAKE_HEAD_COLOR, SNAKE_BODY_COLOR

class Snake :
    def __init__(self, x , y):
        self.body = [(x,y)] #liste de tuples qui representent les cases que le snake occupe, le premier tuple correspond aux coordonnees de la tete

    def draw(self, screen):
        for i, (x,y) in enumerate(self.body):
            if i == 0 :
                color = SNAKE_HEAD_COLOR
            else :
                color = SNAKE_BODY_COLOR
                
            pygame.draw.rect(screen, color, (x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))