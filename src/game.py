import pygame
import sys
from src.constants import  LONGUEUR, BACKGROUND_COLOR
from src.snake import Snake

class Game : 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((LONGUEUR, LONGUEUR))
        pygame.display.set_caption("SNAKE GAME")  
        self.en_cours = True #variable qui permet de savoir si le jeu est en cours ou non (pour la boucle principal du jeu)
        self.snake = Snake(10, 10)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.en_cours = False
                
    
    def run(self) :
        while self.en_cours:
            self.handle_events()
            self.screen.fill(BACKGROUND_COLOR)
            self.snake.draw(self.screen)
            pygame.display.flip()
            
        pygame.quit()
        sys.exit()

