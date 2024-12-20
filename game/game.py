import pygame
from game.frame import Frame
from game.snake.snake import Snake
from game.key_controller import KeyController
from game.snake.snake_controller import SnakeController
from game.food import Food

class Game():

    def __init__(self):
        self.frame = Frame()
        self.snake = Snake(self.frame)
        self.key_controller = KeyController(self.snake)
        self.snake_controller =SnakeController(frame=self.frame, snake=self.snake)
        self.food = Food(frame=self.frame,snake=self.snake)
        self.game_resume = True
    
    def run(self):

        #Frame oluştur
        self.frame.write_screen_title()
        self.frame.clear_screen()
        

        while self.key_controller.game_resume:
            # Keyboard Controller
            self.key_controller.handle_events(pygame.event.get())
            # Pencereyi güncelle
            self.frame.clear_screen()      
            # Snake hareket et
            self.snake_controller.run()
            # snakeyi çiz
            self.snake.draw_snake()    

            # Yem çiz
            self.food.draw_food()

            # Ekranı güncelle
            pygame.display.flip()
