import pygame
from game.snake.snake import Snake
import time


class KeyController():

    def __init__(self,snake):
        self.snake = snake
        self.game_resume = True
        self.x_change = 0
        self.y_change = 0

    
    def update(self):
        self.snake.snake_x += self.x_change * self.snake.snake_velocity
        self.snake.snake_y += self.y_change * self.snake.snake_velocity

    def handle_events(self,events = None):
        for event in events:
            if event.type == pygame.QUIT:
                self.game_resume = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.x_change = 1
                    self.y_change = 0
                elif event.key == pygame.K_LEFT:
                    self.x_change = -1
                    self.y_change = 0
                elif event.key == pygame.K_UP:
                    self.y_change = -1
                    self.x_change = 0
                elif event.key == pygame.K_DOWN:
                    self.y_change = 1
                    self.x_change = 0