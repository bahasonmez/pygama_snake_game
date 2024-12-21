import pygame
from game.frame import Frame


class Snake():
    def __init__(self,frame):
        self.frame = frame

        # snake özellikleri
        self.snake_size = 20
        self.snake_x = 20
        self.snake_y = 120
        self.snakes=[[self.snake_x, self.snake_y]]
        self.snake_velocity = 20
        self.snake_color = (255, 255, 255)   
        # self.get_last_snake_location()
        
    
    def draw_snake(self):
        # for snake in self.snakes:
        pygame.draw.rect(self.frame.screen,self.snake_color , (self.snake_x,self.snake_y, self.snake_size, self.snake_size)) # Beyaz snake

        # print(snake[0],snake[1])
    def increase_snake_length(self,loc):
        self.snakes.append(loc)

        

    def get_last_snake_location(self):
        self.last_snake_location = self.snakes[-1]

    def grow(self):
        # Yılanı büyüt (kuyruğa yeni bir kare ekle)
        # tail_x, tail_y = self.snakes[-1]
        self.snakes.append([self.snake_x, self.snake_y])

