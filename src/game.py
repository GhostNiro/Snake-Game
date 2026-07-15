import pygame
import sys
from src.constants import LARGEUR , LONGUEUR
class Game : 
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((LONGUEUR, LARGEUR))
        pygame.display.set_caption("SNAKE GAME")  
        self.en_cours = True #variable qui permet de savoir si le jeu est en cours ou non (pour la boucle principal du jeu)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.en_cours = False
                
    
    def run(self) :
        while self.en_cours:
            self.handle_events()
            
        pygame.quit()
        sys.exit()

