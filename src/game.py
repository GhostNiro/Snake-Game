import pygame
import sys
from src.constants import  LONGUEUR, BACKGROUND_COLOR, FPS
from src.snake import Snake

class Game : 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((LONGUEUR, LONGUEUR))
        pygame.display.set_caption("SNAKE GAME")  
        self.en_cours = True #variable qui permet de savoir si le jeu est en cours ou non (pour la boucle principal du jeu)
        self.snake = Snake(10, 10)
    
    def handle_events(self):
        '''fonction qui s'occupe de la gestion des evenements (clavier et souris)'''
        for event in pygame.event.get():       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.en_cours = False
                elif event.key == pygame.K_UP:
                    self.snake.set_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.snake.set_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction((1, 0))
    
    def run(self) :
        while self.en_cours:
            self.handle_events()
            self.snake.update()
            self.screen.fill(BACKGROUND_COLOR)
            self.snake.draw(self.screen)
            pygame.display.flip()
            pygame.time.Clock().tick(FPS)
            
        pygame.quit()
        sys.exit()

