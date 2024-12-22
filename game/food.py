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
        self.loc = None
        self.foodlenght = 0  # Kişinin yediği yemeklerin sayısı

    def generate_food(self):
        katlar_x = [i for i in range(0, self.frame.width + 1 -self.snake.snake_size, 20)]
        katlar_y = [i for i in range(0, self.frame.height + 1 - self.snake.snake_size, 20)]
        self.food_x = random.choice(katlar_x)
        self.food_y = random.choice(katlar_y)


    def draw_food(self):
        pygame.draw.rect(self.frame.screen,self.food_color , (self.food_x,self.food_y, self.food_size, self.food_size)) # Beyaz snake
        

    def check_food_collision(self):
        head = self.snake.get_head_snake()
        if head[0] == self.food_x and head[1] == self.food_y:
            self.snake.grow(self.snake.last_snake_location)
            self.generate_food()
            self.foodlenght += 1
            return True
        return False
        
    