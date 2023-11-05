import pygame
import os
from collision_calculations import Block


def config_block(block):
    pygame.Surface.fill(block.surface, block.color)
    block.rect = block.surface.get_rect(topright=(block.xpos, block.ypos))


def update_block(WIN, block):
    block.rect.x += -block.speed
    WIN.blit(block.surface, block.rect)


def calculate_velocity(block1, block2):
    block1_speed_after = abs((((block1.mass - block2.mass) / (block1.mass + block2.mass)) * block1.speed) + (
        ((2 * block2.mass) / (block1.mass + block2.mass)) * block2.speed))
    block2_speed_after = abs(
        ((block1.mass * block1.speed + block2.mass * block2.speed) - block1.mass * block1_speed_after) / block2.mass)
    block1.speed = -block1_speed_after
    block2.speed = -block2_speed_after


def collision_run():
    # Screen settings
    pygame.init()
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Collisions simulator')
    FPS = 60

    # Images settings
    background = pygame.transform.scale(pygame.image.load(os.path.join('resources', 'collision_background.jpg')),
                                        (WIDTH, HEIGHT))

    # Block1 configs
    block1 = Block(WIDTH/4, HEIGHT / 2 - 55, 50, 50, 2, 2, 'red')
    config_block(block1)

    momentum_block1 = block1.mass * block1.speed

    # Block2 configs
    block2 = Block(WIDTH - WIDTH/4, HEIGHT/2 - 55, 50, 50, 2, 2, 'black')
    config_block(block2)

    momentum_block2 = block2.mass * block2.speed

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(background, (0, 0))

        # Blit block 1
        block1.rect.x += block1.speed
        WIN.blit(block1.surface, block1.rect)

        # Blit block 2
        block2.rect.x += -block2.speed
        WIN.blit(block2.surface, block2.rect)

        trial = 0
        if block1.rect.colliderect(block2.rect) and trial == 0:
            trial = 1
            print('Block 1 Speed: ', block1.speed)
            print('Block 2 Speed: ', block2.speed)
            calculate_velocity(block1, block2)
            print('Block 1 Speed after: ', block1.speed)
            print('Block 2 Speed after: ', block2.speed)

        pygame.display.update()

pygame.quit()

