import pygame

# Pygame'i başlat
pygame.init()

# Pencere boyutları
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Pencere başlığı
pygame.display.set_caption("Hareketli Kare")

# Kare özellikleri
kare_boyut = 20
kare_x = 20
kare_y = 20
kare_hiz = 20

# Oyun döngüsü
oyun_devam = True
while oyun_devam:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oyun_devam = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                kare_x += kare_hiz
            if event.key == pygame.K_LEFT:
                kare_x -= kare_hiz  
            if event.key == pygame.K_UP:
                kare_y -= kare_hiz  
            if event.key == pygame.K_DOWN:
                kare_y += kare_hiz  
            
    # Ekranı temizle (arka plan rengi)
    screen.fill((0, 0, 0)) # Siyah

    # Kareyi çiz
    pygame.draw.rect(screen, (255, 255, 255), (kare_x, kare_y, kare_boyut, kare_boyut)) # Beyaz kare

    # Kare hareketini güncelle (sağa doğru)
    if kare_x > WIDTH - kare_boyut:
        kare_x = 0 # Ekranın solundan tekrar başla
    if kare_x < 0:
        kare_x = WIDTH -kare_boyut # Ekranın sağından tekrar başla
    if kare_y > HEIGHT - kare_boyut: 
        kare_y = 0 # Ekranın solundan tekrar başla
    if kare_y < 0:
        kare_y = HEIGHT - kare_boyut # Ekranın solundan tekrar başla
    print(kare_x,kare_y,)
    # Ekranı güncelle
    pygame.display.flip()

# Pygame'i kapat
pygame.quit()