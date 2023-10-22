
import pygame
import os

def collision_run():
    #Screen settings
    pygame.init()
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Collisions simulator')
    FPS = 60

    #Images settings
    background = pygame.transform.scale(pygame.image.load(os.path.join('resources', 'collision_background.jpg')), (WIDTH, HEIGHT))

    #Block1 configs
    block1 = pygame.Surface((50, 50))
    pygame.Surface.fill(block1, 'red')
    block1_rect = block1.get_rect(topright = ((WIDTH/4), (HEIGHT / 2 - 55)))

    block1_speed = 2
    block1_mass = 2
    momentum_block1 = block1_mass * block1_speed

    #Block2 configs
    block2 = pygame.Surface((50, 50))
    pygame.Surface.fill(block2, 'black')
    block2_rect = block2.get_rect(topright = ((WIDTH - WIDTH/4), (HEIGHT / 2 - 55)))

    block2_speed = 4
    block2_mass = 1
    momentum_block2 = block2_mass * block2_speed


    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(background, (0, 0))



        #Blit block 1
        block1_rect.x += block1_speed
        WIN.blit(block1, block1_rect)

        #Blit block 2
        block2_rect.x += -(block2_speed)
        WIN.blit(block2, block2_rect)

        trial = 0
        if block1_rect.colliderect(block2_rect) and trial == 0:
            trial = 1
            print('Block 1 Speed: ', block1_speed)
            print('Block 2 Speed: ', block2_speed)
            block1_speed_after = abs((((block1_mass - block2_mass) / (block1_mass + block2_mass)) * block1_speed) + (((2*block2_mass) / (block1_mass + block2_mass)) * block2_speed))
            print('Block 1 Speed after: ', block1_speed_after)
            block2_speed_after = abs(((block1_mass * block1_speed + block2_mass * block2_speed) - block1_mass * block1_speed_after) / block2_mass)
            print('Block 2 Speed after: ', block2_speed_after)
            block1_speed = -(block1_speed_after)
            block2_speed = -(block2_speed_after)



        pygame.display.update()

pygame.quit()


