import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

sun_x = 320
sun_y = 10
sun_radius = 25

cloud1_x = 36
cloud1_y = 121
cloud_radius = 20

cloud2_x = 357
cloud2_y = 179

cloud3_x = 528
cloud3_y = 60

wave1_x = 0
wave2_x = -720
wave_y = 360
wave_radius = 100
wave_y_speed = 0.5

fish1_x = 103
fish1_y = 391
fish1_tail = 18
fish2_x = 508
fish2_y = 290
fish_length = 75
fish_y_speed = 1

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    sun_x += 0.25
    if sun_x - sun_radius > WIDTH:
        sun_x = -sun_radius
        
    cloud1_x += 2
    cloud2_x += 2
    cloud3_x += 2
    if cloud1_x - cloud_radius > WIDTH:
        cloud1_x = -41 - cloud_radius
    if cloud2_x - cloud_radius > WIDTH:
        cloud2_x = -53 - cloud_radius
    if cloud3_x - cloud_radius > WIDTH:
        cloud3_x = -50 - cloud_radius
        
    wave1_x += 4
    wave2_x += 4
    if wave1_x - wave_radius > WIDTH:
        wave1_x = -600 - wave_radius
    if wave2_x - wave_radius > WIDTH:
        wave2_x = -600 - wave_radius
    wave_y -= wave_y_speed
    if wave_y == 350:
        wave_y_speed = -0.5
    elif wave_y == 360:
        wave_y_speed = 0.5

    fish1_x += 9
    if fish1_x - fish1_tail > WIDTH:
        fish1_x = -fish_length
    fish1_y -= fish_y_speed
    if fish1_y == 360:
        fish_y_speed = -1
    elif fish1_y == 391:
        fish_y_speed = 1

    fish2_x -= 1
    if fish2_x + fish_length < 0:
        fish2_x = WIDTH
    
    # DRAWING
    screen.fill((101, 147, 245))  # always the first drawing command

    #Sky
    pygame.draw.circle(screen, (255, 216, 1), (sun_x, sun_y), sun_radius)

    cloud_colour = (240, 240, 240)
    #                                            36        121
    pygame.draw.circle(screen, cloud_colour, (cloud1_x, cloud1_y), cloud_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud1_x + 15, cloud1_y - 15), cloud_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud1_x + 25, cloud1_y + 8), cloud_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud1_x + 41, cloud1_y - 13), cloud_radius)
    #                                           357        179
    pygame.draw.circle(screen, cloud_colour, (cloud2_x, cloud2_y), cloud_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud2_x + 30, cloud2_y + 14), cloud_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud2_x + 26, cloud2_y - 13), cloud_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud2_x + 53, cloud2_y -1), cloud_radius)
    #                                           528        60
    pygame.draw.circle(screen, cloud_colour, (cloud3_x, cloud3_y), cloud_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud3_x + 23, cloud3_y - 23), cloud_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud3_x + 25, cloud3_y + 10), cloud_radius)
    pygame.draw.circle(screen, cloud_colour, (cloud3_x + 50, cloud3_y - 5), cloud_radius)
    
    #Sailboat
    pygame.draw.polygon(screen, (106, 78, 66), [(189,215), (237, 303), (395, 303), (443, 215)])
    pygame.draw.rect(screen, (57, 30, 23), (315, 76, 10, 140))
    pygame.draw.polygon(screen, (178, 34, 34), [(315, 76), (315, 175), (220, 175)])
    pygame.draw.rect(screen, (178, 34, 34), (315, 92, 11, 5))
    pygame.draw.rect(screen, (178, 34, 34), (315, 160, 11, 5))

    #Water
    pygame.draw.rect(screen, (0, 0, 128), (0, 288, 640, 283))
    #                                          0       360
    pygame.draw.circle(screen, (0, 0, 128), (wave1_x, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave1_x + 80, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave1_x + 160, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave1_x + 240, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave1_x + 320, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave1_x + 400, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave1_x + 480, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave1_x + 560, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave1_x + 640, wave_y), wave_radius)
    #                                         -720     360
    pygame.draw.circle(screen, (0, 0, 128), (wave2_x, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave2_x + 80, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave2_x + 160, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave2_x + 240, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave2_x + 320, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave2_x + 400, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave2_x + 480, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave2_x + 560, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave2_x + 640, wave_y), wave_radius)
    pygame.draw.circle(screen, (0, 0, 128), (wave2_x + 720, wave_y), wave_radius)

    #Fish
    fish1_colour = (152, 191, 100)
    #                                          103      391
    pygame.draw.ellipse(screen, fish1_colour, (fish1_x, fish1_y, 60, 30))
    pygame.draw.polygon(screen, fish1_colour, [(fish1_x + 17, fish1_y + 15), (fish1_x - 18, fish1_y - 5), (fish1_x - 18, fish1_y + 35)])
    pygame.draw.polygon(screen, fish1_colour, [(fish1_x + 37, fish1_y + 3), (fish1_x + 18, fish1_y - 12), (fish1_x + 18, fish1_y + 3)])
    pygame.draw.circle(screen, (240, 240, 240), (fish1_x + 47, fish1_y + 9), 8)
    pygame.draw.circle(screen, (35, 79, 30), (fish1_x + 47, fish1_y + 9), 5)
    pygame.draw.ellipse(screen, (65, 3, 0), (fish1_x + 47, fish1_y + 19, 14, 4))

    fish2_colour = (240, 131, 58)
    #                                            508      290
    pygame.draw.ellipse(screen, fish2_colour, (fish2_x, fish2_y, 60, 30))
    pygame.draw.polygon(screen, fish2_colour, [(fish2_x + 47, fish2_y + 15), (fish2_x + 73, fish2_y - 5), (fish2_x + 73, fish2_y + 35)])
    pygame.draw.polygon(screen, fish2_colour, [(fish2_x + 31, fish2_y + 3), (fish2_x + 46, fish2_y - 12), (fish2_x + 46, fish2_y + 3)])
    pygame.draw.circle(screen, (240, 250, 240), (fish2_x + 8, fish2_y + 9), 10)
    pygame.draw.circle(screen, (135, 60, 10), (fish2_x + 8, fish2_y + 9), 5)
    pygame.draw.ellipse(screen, (65, 3, 0), (fish2_x, fish2_y + 21, 14, 5))

    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
