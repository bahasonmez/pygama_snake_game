import pygame
from game.frame import Frame
from game.game import Game
from game.food import Food

def main():
    Frame().change_fps()
    # Pygame'i başlat
    pygame.init()
    Game().run()
    # Pygame'i kapat
    pygame.quit()

if __name__ == "__main__":
    main()