import pygame

class SnakeController():

    def __init__(self, frame,snake):
        self.frame = frame
        self.snake = snake

    def frame_out(self):
        # snake hareketini güncelle (sağa doğru)
        if self.snake.snake_x > self.frame.width - self.snake.snake_size:
            self.snake.snake_x = 0 # Ekranın solundan tekrar başla
        if self.snake.snake_x < 0:
            self.snake.snake_x = self.frame.width -self.snake.snake_size # Ekranın sağından tekrar başla
        if self.snake.snake_y > self.frame.height - self.snake.snake_size: 
            self.snake.snake_y = 0 # Ekranın solundan tekrar başla
        if self.snake.snake_y < 0:
            self.snake.snake_y = self.frame.height - self.snake.snake_size # Ekranın solundan tekrar başla
        # print(self.snake.snake_x,self.snake.snake_y,)

    