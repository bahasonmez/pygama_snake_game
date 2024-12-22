import pygame
from game.frame import Frame
from game.snake.snake import Snake, SnakeItem
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
        
        self.fps = 10

    def run(self):

        #Frame oluştur
        self.frame.write_screen_title()
        self.frame.clear_screen()
        snake_item = SnakeItem()
        self.snake.snake_items.append([snake_item.x, snake_item.y])

        while self.key_controller.game_resume and self.snake_controller.game_resume:

            self.snake_controller.snake_on_snake()
            # Keyboard Controller
            self.key_controller.handle_events(pygame.event.get())

            # Pencere dışına çıkmasın
            self.snake_controller.frame_out()
            # Snake Location
            # Snake hareket et
            self.key_controller.update()
            # Pencereyi güncelle
            self.frame.clear_screen()      

            # snakeyi çiz
            self.snake.draw_snake()    

            # Yem çiz
            self.food.draw_food()
            self.food.check_food_collision()


            # Ekranı güncelle
            pygame.display.flip()
            clock = pygame.time.Clock()
            clock.tick(self.fps)
