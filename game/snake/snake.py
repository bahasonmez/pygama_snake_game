import pygame
from game.frame import Frame


class Snake():
    def __init__(self,frame):
        self.frame = frame

        # snake özellikleri
        self.snake_size = 20
        self.snake_x = 20
        self.snake_y = 20
        self.snakes=[[self.snake_x, self.snake_y]]
        self.snake_velocity = 20
        self.snake_color = (255, 255, 255)    
    
    def draw_snake(self):
        self.snakes=[[self.snake_x, self.snake_y]]
        for snake in self.snakes:
            pygame.draw.rect(self.frame.screen,self.snake_color , (snake[0],snake[1], self.snake_size, self.snake_size)) # Beyaz snake
