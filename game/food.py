import random

import pygame

class Food():
    def __init__(self,frame,snake):
        self.frame = frame
        self.snake = snake
        self.food_size = self.snake.snake_size
        self.food_image = pygame.Surface((self.food_size, self.food_size))
        self.food_velocity = 20
        self.food_color = (255, 255, 255)
        self.generate_food()

    def generate_food(self):
        self.food_x = random.randint(0,self.frame.width- self.food_size)
        self.food_y = random.randint(0,self.frame.width- self.food_size)
    
    def draw_food(self):
        pygame.draw.rect(self.frame.screen,(250,250,250) , (100,100, self.food_size, self.food_size)) # Beyaz snake
        print(self.food_x)