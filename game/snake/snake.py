import pygame
from game.frame import Frame


class Snake():
    def __init__(self,frame):
        self.frame = frame

        # snake özellikleri
        self.snake_size = 20
        self.snake_items=[]
        self.snake_velocity = 20
        self.snake_color = (255, 255, 255)
        self.last_snake_location = None
        self.snake_new_head = [0,0]

    def get_head_snake(self):
        return self.snake_items[0]

    def draw_snake(self):

        for item in self.snake_items:
            pygame.draw.rect(self.frame.screen,self.snake_color , (item[0],item[1],self.snake_size, self.snake_size)) # Beyaz snake

        # print(snake[0],snake[1])
        
    def get_last_snake_location(self):
        return self.snake_items[-1]

    def grow(self,loc):
        loc_x, loc_y = loc
        snake_item = SnakeItem(loc_x,loc_y)
        self.snake_items.append([snake_item.x,snake_item.y])
        # print(loc[0],loc[1])

class SnakeItem():
    def __init__(self, x=20, y=20):
        self.x = x
        self.y = y