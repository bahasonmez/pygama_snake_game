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

        head = self.snake.snake_items[0]
        self.snake.last_snake_location = self.snake.snake_items[-1][:]
        new_head = [head[0] + (self.x_change * self.snake.snake_velocity), head[1] + (self.y_change * self.snake.snake_velocity)]
        self.snake.snake_items.insert(0,new_head)
        self.snake.snake_items.pop(-1)


    def handle_events(self,events = None):
        for event in events:
            if event.type == pygame.QUIT:
                self.game_resume = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and self.x_change == 0 :
                    self.x_change = 1
                    self.y_change = 0
                elif event.key == pygame.K_a and self.x_change == 0:
                    self.x_change = -1
                    self.y_change = 0
                elif event.key == pygame.K_w and self.y_change == 0:
                    self.y_change = -1
                    self.x_change = 0
                elif event.key == pygame.K_s and self.y_change == 0:
                    self.y_change = 1
                    self.x_change = 0
            