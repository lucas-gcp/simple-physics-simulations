import pygame
from gravity import Body

pygame.init()


def calculate_acceleration(body, bodies_list):
    for b in bodies_list:
        body.calc_accel(b)


def update_body(bodies_list):
    for b in bodies_list:
        calculate_acceleration(b, filter(lambda x: x != b, bodies_list))
        b.calc_speed()
    for b in bodies_list:
        b.move()
        b.clear_accel()


# Function to draw object from Body class
def draw_body(surface, color, body):
    pygame.draw.circle(surface, color, (body.xpos, body.ypos), body.radius)


screenWidth, screenHeight = 1000, 1000
screen = pygame.display.set_mode([screenWidth, screenHeight])
clock = pygame.time.Clock()

earth = pygame.image.load(R".\resources\earth.png")
earth = pygame.transform.scale(earth, (15, 15))

bodies = []
# Test bodies
body_1 = Body(300, 200, 5.9722*10**12, 3, 1.4, 0.15, 0, 0)
bodies.append(body_1)
body_2 = Body(280, 300, 1.98*10**12, 5, 0, 0, 0, 0)
bodies.append(body_2)
body_3 = Body(450, 340, 7.34767309*10**12, 2, 0.9, -1, 0, 0)
bodies.append(body_3)
body_4 = Body(600, 270, 7.34767309*10**12, 4, -0.9, 1.9, 0, 0)
bodies.append(body_4)

running = True
tickrate = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    update_body(bodies)

    screen.fill('black')
    # Test the draw_body function
    screen.blit(earth, (body_1.xpos-5, body_1.ypos-5))
    draw_body(screen, 'blue', body_1)
    draw_body(screen, 'yellow', body_2)
    draw_body(screen, 'white', body_3)
    draw_body(screen, 'green', body_4)
    pygame.display.update()
    clock.tick(tickrate)

pygame.quit()
