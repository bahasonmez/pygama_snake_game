import random

import pygame

class Food():
    def __init__(self,frame,snake):
        self.frame = frame
        self.snake = snake
        self.food_size = self.snake.snake_size
        self.food_image = pygame.Surface((self.food_size, self.food_size))
        self.food_velocity = 20
        self.food_color = (255, 255, 102)
        self.generate_food()

    def generate_food(self):
        katlar_x = [i for i in range(0, 401-self.snake.snake_x, 20)]
        katlar_y = [i for i in range(0, 601 - self.snake.snake_x, 20)]
        self.food_x = random.choice(katlar_x)
        self.food_y = random.choice(katlar_y)
    
    def draw_food(self):
        pygame.draw.rect(self.frame.screen,self.food_color , (self.food_x,self.food_y, self.food_size, self.food_size)) # Beyaz snake
        

    def check_food_collision(self):
        if self.snake.snake_x == self.food_x and self.snake.snake_y == self.food_y:
            self.snake.grow()
            self.generate_food()
        return True
    