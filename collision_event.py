import pygame
import os
from collision_calculations import Block

def calculate_velocity(block1, block2):
    block1_speed_after = abs((((block1.mass - block2.mass) / (block1.mass + block2.mass)) * block1.speed) + (
        ((2 * block2.mass) / (block1.mass + block2.mass)) * block2.speed))
    block2_speed_after = abs(
        ((block1.mass * block1.speed + block2.mass * block2.speed) - block1.mass * block1_speed_after) / block2.mass)
    block1.speed = -(block1_speed_after)
    block2.speed = -(block2_speed_after)

def collision_run():
    # Screen settings
    pygame.init()
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Collisions simulator')
    FPS = 60

    # Images settings
    background = pygame.transform.scale(pygame.image.load(os.path.join('resources', 'collision_background.jpg')), (WIDTH, HEIGHT))

    # Block1 configs
    block1 = Block(WIDTH/4, HEIGHT / 2 - 55, 50, 50, 2, 2)
    block1_surface = pygame.Surface((block1.xsize, block1.ysize))
    pygame.Surface.fill(block1_surface, 'red')
    block1_rect = block1_surface.get_rect(topright = (block1.xpos, block1.ypos))

    momentum_block1 = block1.mass * block1.speed

    # Block2 configs
    block2 = Block(WIDTH - WIDTH/4, HEIGHT/2 - 55, 50, 50, 4, 1)
    block2_surface = pygame.Surface((block2.xsize, block2.ysize))
    pygame.Surface.fill(block2_surface, 'black')
    block2_rect = block2_surface.get_rect(topright = (block2.xpos, block2.ypos))

    momentum_block2 = block2.mass * block2.speed


    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(background, (0, 0))



        #Blit block 1
        block1_rect.x += block1.speed
        WIN.blit(block1_surface, block1_rect)

        #Blit block 2
        block2_rect.x += -(block2.speed)
        WIN.blit(block2_surface, block2_rect)

        trial = 0
        if block1_rect.colliderect(block2_rect) and trial == 0:
            trial = 1
            print('Block 1 Speed: ', block1.speed)
            print('Block 2 Speed: ', block2.speed)
            calculate_velocity(block1, block2)
            print('Block 1 Speed after: ', block1.speed)
            print('Block 2 Speed after: ', block2.speed)



        pygame.display.update()

pygame.quit()


