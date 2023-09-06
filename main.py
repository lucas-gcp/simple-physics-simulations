import pygame
from gravity import Body

pygame.init()


# Function to draw object from Body class
def draw_body(surface, color, body):
    pygame.draw.circle(surface, color, (body.xpos, body.ypos), body.radius)


screenWidth, screenHeight = 1000, 1000
screen = pygame.display.set_mode([screenWidth, screenHeight])
clock = pygame.time.Clock()

# Test bodies
body_1 = Body(500, 649.6, 5.9722*10**24, 3, 2.978, 0, 0, 0)
body_2 = Body(500, 500, 1.98*10**31, 5, 0, 0, 0, 0)

running = True
tickrate = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    body_1.calc_accel(body_2)
    body_1.calc_speed()
    body_1.move()
    body_2.calc_accel(body_1)
    body_2.calc_speed()
    body_2.move()

    screen.fill('black')
    # Test the draw_body function
    draw_body(screen, 'blue', body_1)
    draw_body(screen, 'yellow', body_2)
    pygame.display.update()
    clock.tick(tickrate)

pygame.quit()
