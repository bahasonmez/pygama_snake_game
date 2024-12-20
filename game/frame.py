import pygame

class Frame():
    
    def __init__(self):
        # Pencere boyutları
        self.width = 600
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_title ="Hareketli Kare"

    # Pencere başlığı
    
    def clear_screen(self):
                # Ekranı temizle (arka plan rengi)
        self.screen.fill((0, 0, 0)) # Siyah

    def write_screen_title(self):
        pygame.display.set_caption(self.screen_title)
