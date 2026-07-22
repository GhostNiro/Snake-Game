import pygame
import sys
from src.constants import  *
from src.snake import Snake
from src.food import Food

class Game : 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((LONGUEUR, LONGUEUR))
        pygame.display.set_caption("SNAKE GAME")  
        self.en_cours = True #variable qui permet de savoir si le jeu est en cours ou non (pour la boucle principal du jeu)
        self.snake = Snake(10, 10)
        self.food = Food(self.snake.body)
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.speed = FPS 
    
    def handle_events(self):
        '''fonction qui s'occupe de la gestion des evenements (clavier et souris)'''
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.en_cours = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
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

            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food.regenerate(self.snake.body)
                self.score += 1
                if self.score % 10 == 0 and self.score > 0 :
                    self.speed += 5

            if self.snake.wall_collision() or self.snake.self_collision():
                self.en_cours = False
                print("GAME OVER")

            self.screen.fill(BACKGROUND_COLOR)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            #ce qui suit c'est pour afficher le score en haut à gauche de l'ecran
            score_texte = self.font.render(f"SCORE : {self.score}", True, (255, 255, 255))
            self.screen.blit(score_texte, (10, 10))
            pygame.display.flip()
            pygame.time.Clock().tick(self.speed)
            
        pygame.quit()
        sys.exit()

