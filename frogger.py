import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 500))

clock = pygame.time.Clock()

# Carregar imagens

road_img = pygame.image.load('images/road.png')
car_left_img = pygame.image.load('images/car_left.png')
car_left_img.set_colorkey((255, 0, 255))
car_right_img = pygame.image.load('images/car_right.png')
car_right_img.set_colorkey((255, 0, 255))
frog_img = pygame.image.load('images/frog.png')
frog_img.set_colorkey((255, 0, 255))

# Coordenadas

road_x, road_y = 0, 50
car_left_x, car_left_y = 880, 135
car2_left_x, car2_left_y = 880, 285
car_right_x, car_right_y = 10, 210
car2_right_x, car2_right_y = 10, 360
frog_x, frog_y = 500, 455


running = True
while running:
    ######    Eventos    ######

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pass

    ######    Lógica     ######



    ######     Ecrã      ######

    # Iniciar as imagens no ecrã

    screen.fill(pygame.Color('blue')) # Os 50px na parte superior do ecrã poderão ser utilizado para um sistema de vidas.
    screen.blit(road_img, (road_x, road_y))
    screen.blit(frog_img, (frog_x, frog_y))
    screen.blit(car_left_img, (car_left_x, car_left_y))
    screen.blit(car_left_img, (car2_left_x, car2_left_y))
    screen.blit(car_right_img, (car_right_x, car_right_y))
    screen.blit(car_right_img, (car2_right_x, car2_right_y))
    
    pygame.display.flip()

pygame.quit()
