import pygame

pygame.init()

frog_icon = pygame.image.load('images/frog_icon.png')

pygame.display.set_caption("Frogger")
pygame.display.set_icon(frog_icon)

screen = pygame.display.set_mode((1000, 500))

clock = pygame.time.Clock()

# Carregar imagens

road_img = pygame.image.load('images/road.png').convert()
car_left_img = pygame.image.load('images/car_left.png').convert()
car_left_img.set_colorkey((255, 0, 255))
car_right_img = pygame.image.load('images/car_right.png').convert()
car_right_img.set_colorkey((255, 0, 255))
frog_img = pygame.image.load('images/frog.png').convert()
frog_img.set_colorkey((255, 0, 255))

# Coordenadas

road_x, road_y = 0, 50
car_right_x, car_right_y = [200, 600, 1000], 135
car_left_x, car_left_y = [250, 550, 880, 1150], 210
car2_right_x, car2_right_y = [10, 380, 760], 285
car2_left_x, car2_left_y = [350, 650, 950, 1250], 360
frog_x, frog_y = 500, 455

# Constante das velocidades para os carros (uma velocidade por cada faixa)

car_speed = [0.1, 0.125, 0.16, 0.22]

# Funções

def car_mov_right(coord_x, dt, faixa):
    for i in range(len(coord_x)):
        if coord_x[i] >= 1100:
            coord_x[i] = -100
        else:
            coord_x[i] += car_speed[faixa] * dt

def car_mov_left(coord_x, dt, faixa):
    for i in range(len(coord_x)):
        if coord_x[i] <= -100:
            coord_x[i] = 1100
        else:
            coord_x[i] -= car_speed[faixa] * dt

running = True
while running:
    dt = clock.tick(30)

    ######    Eventos    ######

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            # Fazer rotação da rã

            if event.key == pygame.K_UP:
                if frog_y - 80 > 0:
                    frog_y -= 80
            elif event.key == pygame.K_DOWN:
                if frog_y + 80 < 500:
                    frog_y += 80
            elif event.key == pygame.K_LEFT:
                if frog_x - 60 > 0:
                    frog_x -= 60
            elif event.key == pygame.K_RIGHT:
                if frog_x + 60 < 980:
                    frog_x += 60

    ######    Lógica     ######

    # Movimento dos carros

    car_mov_right(car_right_x, dt, 3)
    car_mov_left(car_left_x, dt, 2)
    car_mov_right(car2_right_x, dt, 1)
    car_mov_left(car2_left_x, dt, 0)

    ######     Ecrã      ######

    # Iniciar as imagens no ecrã

    screen.fill(pygame.Color('blue')) # Os 50px na parte superior do ecrã poderão ser utilizado para um sistema de vidas.
    screen.blit(road_img, (road_x, road_y))
    screen.blit(frog_img, (frog_x, frog_y))

    # Primeira faixa
    for i in range(len(car_right_x)):
        screen.blit(car_right_img, (car_right_x[i], car_right_y))
    
    # Segunda Faixa
    for i in range(len(car2_right_x)):
        screen.blit(car_right_img, (car2_right_x[i], car2_right_y))
    
    # Terceira Faixa
    for i in range(len(car_left_x)):
        screen.blit(car_left_img, (car_left_x[i], car_left_y))
    
    # Quarta Faixa
    for i in range(len(car2_left_x)):
        screen.blit(car_left_img, (car2_left_x[i], car2_left_y))
    
    pygame.display.flip()

    if frog_y == 55:
        running = False
        print("Winner")

pygame.quit()
