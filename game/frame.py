import pygame

class Frame():
    
    def __init__(self):
        # Pencere boyutları
        self.width = 200
        self.height = 200
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_title ="Hareketli Kare"
        self.fps = 7
        self.kolay = 7
        self.orta = 10
        self.zor = 13

    # Pencere başlığı
    
    def clear_screen(self):
                # Ekranı temizle (arka plan rengi)
        self.screen.fill((0, 0, 0)) # Siyah

    def write_screen_title(self):
        pygame.display.set_caption(self.screen_title)

    def change_fps(self):
        fps = input("-zorluk: 0 1 2: ") 
        if fps == 0:
            self.fps = self.kolay 
        elif fps == 1:
            self.fps = self.orta
        elif fps == 2:
            self.fps = self.zor

    def change_size(self):
        pass

            
