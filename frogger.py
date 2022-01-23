import pygame

pygame.init()

frog_icon = pygame.image.load('images/frog_icon.png')

pygame.display.set_caption("Frogger")
pygame.display.set_icon(frog_icon)

screen = pygame.display.set_mode((1000, 500))

clock = pygame.time.Clock()

font = pygame.font.Font("font/EBGaramond.ttf", 68)
font_small = pygame.font.Font("font/EBGaramond.ttf", 34)
font_smaller = pygame.font.Font("font/EBGaramond.ttf", 20)

# Load Images

road_img = pygame.image.load('images/road.png').convert()
car_left_img = pygame.image.load('images/car_left.png').convert()
car_left_img.set_colorkey((255, 0, 255))
car_right_img = pygame.image.load('images/car_right.png').convert()
car_right_img.set_colorkey((255, 0, 255))
frog_src = pygame.image.load('images/frog.png').convert()
frog_src.set_colorkey((255, 0, 255))

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

def collision(frog, cars):
    for car in cars:
        if frog[0] < car[0] + car[2] and frog[0] + frog[2] > car[0]:
            return True
    return False

running = True
restart = True # Starts True to initialize the game
lives = 3
while running:
    dt = clock.tick(30)
    lives_str = f"x {lives}"
    alive = lives > 0

    ######    Restart    ######

    while restart:
        frog_img = frog_src

        win, lose = False, False

        # Coordinates

        road_x, road_y = 0, 50
        car_right_x, car_right_y = [200, 600, 1000], 135
        car_left_x, car_left_y = [250, 550, 880, 1150], 210
        car2_right_x, car2_right_y = [10, 380, 760], 285
        car2_left_x, car2_left_y = [350, 650, 950, 1250], 360
        frog_x, frog_y = 500, 455

        # Velocity (upper lane to lower lane)

        car_speed = [0.22, 0.16, 0.125, 0.1]
        
        restart = False

    ######    Events    ######

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and alive and not win:
                if frog_y - 80 > 0:
                    frog_y -= 80
                    frog_img = pygame.transform.rotate(frog_src, 0)
            elif event.key == pygame.K_DOWN and alive and not win:
                if frog_y + 80 < 500:
                    frog_y += 80
                    frog_img = pygame.transform.rotate(frog_src, 180)
            elif event.key == pygame.K_LEFT and alive and not win:
                if frog_x - 60 > 0:
                    frog_x -= 60
                    frog_img = pygame.transform.rotate(frog_src, 90)
            elif event.key == pygame.K_RIGHT and alive and not win:
                if frog_x + 60 < 980:
                    frog_x += 60
                    frog_img = pygame.transform.rotate(frog_src, 270)
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                restart = True
                lives = 3

    ######    Logic     ######

    # Car movement

    car_mov_right(car_right_x, dt, 0)
    car_mov_left(car_left_x, dt, 1)
    car_mov_right(car2_right_x, dt, 2)
    car_mov_left(car2_left_x, dt, 3)

    # Hitbox Update

    frog_hitbox = (frog_x, frog_y, 50, 35)

    car_right_hitbox = []
    car2_right_hitbox = []
    for i in range(len(car_right_x)):
        car_right_hitbox.append((car_right_x[i], car_right_y, 107, 55))
        car2_right_hitbox.append((car2_right_x[i], car2_right_y, 107, 55))
    
    car_left_hitbox = []
    car2_left_hitbox = []
    for i in range(len(car2_left_x)):
        car_left_hitbox.append((car_left_x[i], car_left_y, 107, 55))
        car2_left_hitbox.append((car2_left_x[i], car2_left_y, 107, 55))

    # Winning and losing conditions

    if frog_y == 135:
        lose = collision(frog_hitbox, car_right_hitbox)
    elif frog_y == 215:
        lose = collision(frog_hitbox, car_left_hitbox)
    elif frog_y == 295:
        lose = collision(frog_hitbox, car2_right_hitbox)
    elif frog_y == 375:
        lose = collision(frog_hitbox, car2_left_hitbox)
    elif frog_y == 55:
        win = True

    if alive and lose:
        lives -= 1
        restart = True

    ######     Screen      ######

    # Screen, background and frog

    screen.fill(pygame.Color('black'))
    screen.blit(road_img, (road_x, road_y))
    screen.blit(frog_img, (frog_x, frog_y))

    # Topbar

    screen.blit(frog_icon, (10, 5))
    text = font_small.render(lives_str, True, (255, 255, 255))
    screen.blit(text, (70, 2))
    text = font_smaller.render("R to restart", True, (255, 255, 255))
    screen.blit(text, (900, 15))
    text = font_smaller.render("ESC to exit", True, (255, 255, 255))
    screen.blit(text, (700, 15))

    # First and third lane
    for i in range(len(car_right_x)):
        screen.blit(car_right_img, (car_right_x[i], car_right_y))
        screen.blit(car_right_img, (car2_right_x[i], car2_right_y))
    
    # Second and forth lane
    for i in range(len(car_left_x)):
        screen.blit(car_left_img, (car_left_x[i], car_left_y))
        screen.blit(car_left_img, (car2_left_x[i], car2_left_y))

    # Hitbox debugging
    '''
    pygame.draw.rect(screen, (255, 0, 0), frog_hitbox, 2)
    
    for i in range(len(car_right_x)):
        pygame.draw.rect(screen, (255, 0, 0), car_right_hitbox[i], 2)
        pygame.draw.rect(screen, (255, 0, 0), car2_right_hitbox[i], 2)
    
    for i in range(len(car_left_x)):
        pygame.draw.rect(screen, (255, 0, 0), car_left_hitbox[i], 2)
        pygame.draw.rect(screen, (255, 0, 0), car2_left_hitbox[i], 2)
    '''
    # Winning and losing

    if win:
        screen.fill((0, 0, 0))
        text = font.render(f"YOU WON WITH {lives} LIVES", True, (255, 255, 255))
        screen.blit(text, (150, 125))
        text = font.render("Press ESC to leave or R to restart", True, (255, 255, 255))
        screen.blit(text, (75, 250))

    if not alive:
        screen.fill((0, 0, 0))
        text = font.render("YOU LOSE", True, (255, 255, 255))
        screen.blit(text, (325, 125))
        text = font.render("Press ESC to leave or R to restart", True, (255, 255, 255))
        screen.blit(text, (75, 250))

    pygame.display.flip()

pygame.quit()
