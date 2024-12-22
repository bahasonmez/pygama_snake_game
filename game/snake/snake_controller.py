import pygame

class SnakeController():

    def __init__(self, frame,snake):
        self.frame = frame
        self.snake = snake
        self.game_resume = True

    def frame_out(self):
        for snake in self.snake.snake_items:
        # snake hareketini güncelle (sağa doğru)
            if self.snake.snake_items[0][0] > self.frame.width - self.snake.snake_size:
                snake[0] = 0 # Ekranın solundan tekrar başla
            if self.snake.snake_items[0][0] < 0:
                snake[0] = self.frame.width - self.snake.snake_size # Ekranın sağından tekrar başla
            if self.snake.snake_items[0][1] > self.frame.height - self.snake.snake_size: 
                snake[1] = 0 # Ekranın solundan tekrar başla
            if self.snake.snake_items[0][1] < 0:
                snake[1] = self.frame.height - self.snake.snake_size # Ekranın solundan tekrar başla
            # print(self.snake.snake_items[-1],self.snake.snake_y,)

    def snake_on_snake(self):
        for i in range(len(self.snake.snake_items)-1):
            if self.snake.snake_items[-1][0] == self.snake.snake_items[i][0] and self.snake.snake_items[-1][1] == self.snake.snake_items[i][1]:
                self.game_resume = False
        return False