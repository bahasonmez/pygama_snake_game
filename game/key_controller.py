import pygame
from game.snake.snake import Snake


class KeyController():

    def __init__(self,snake):
        self.snake = snake
        self.game_resume = True

    def handle_events(self,events = None):
        for event in events:
            if event.type == pygame.QUIT:
                self.game_resume = False
            if event.type == pygame.KEYDOWN:
                print("sasssss")
                if event.key == pygame.K_RIGHT:
                    self.snake.snake_x += self.snake.snake_velocity
                if event.key == pygame.K_LEFT:
                    self.snake.snake_x -= self.snake.snake_velocity  
                if event.key == pygame.K_UP:
                    self.snake.snake_y -= self.snake.snake_velocity  
                if event.key == pygame.K_DOWN:
                    self.snake.snake_y += self.snake.snake_velocity 