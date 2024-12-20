import pygame
from game.game import Game

def main():
    # Pygame'i başlat
    pygame.init()
    Game().run()
    # Pygame'i kapat
    pygame.quit()

if __name__ == "__main__":
    main()