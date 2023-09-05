import pygame
from gravity import Body

pygame.init()

# Function to draw object from Body class
def draw_body(surface, color, body):
    pygame.draw.circle(screen, 'white', (body.xpos, body.ypos), body.radius)

screenWidth = 400
screenHeight = 400
screen = pygame.display.set_mode([screenWidth, screenHeight])
clock = pygame.time.Clock()

# Test bodies
body_1 = Body(100,100, 5, 0, 0, 0.1, 0.1)
body_2 = Body(200, 200, 3, 1, 1, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    body_1.calc_speed()
    body_1.move()

    screen.fill ('black')
    # Test the draw_body function
    draw_body(screen, 'white', body_1)
    draw_body(screen, 'red', body_2)
    pygame.display.update()
    clock.tick(60)

pygame.quit()