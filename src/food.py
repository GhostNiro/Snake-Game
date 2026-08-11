import random
import pygame
from src.constants import *

class Food :
    def __init__(self, snake_body):
        self.position = self.generate(snake_body)

    def generate(self, snake_body):
        '''methode qui genere une position aleatoire de la pomme'''
        while True:
            x = random.randint(0, LONGUEUR // TAILLE_CASE - 1)
            y = random.randint(0, LONGUEUR // TAILLE_CASE - 1)
            if (x, y) not in snake_body:
                return (x, y)
    
    def regenerate(self, snake_body):
        self.position = self.generate(snake_body)

    def draw(self, screen):
        pygame.draw.rect(screen, FOOD_COLOR, (self.position[0] * TAILLE_CASE, self.position[1] * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))