import pygame
from gravity import Body

pygame.init()


# Function to draw object from Body class
def draw_body(surface, color, body):
    pygame.draw.circle(surface, color, (body.xpos, body.ypos), body.radius)


def calculate_acceleration(body, bodies_list):
    for b in bodies_list:
        body.calc_accel(b)


def update_body(bodies_list):
    for b in bodies_list:
        calculate_acceleration(b, filter(lambda x: x != b, bodies_list))
        b.calc_speed()
        b.move()
        b.clear_accel()


screenWidth = 1000
screenHeight = 1000
screen = pygame.display.set_mode([screenWidth, screenHeight])
clock = pygame.time.Clock()

earth = pygame.image.load(R"D:\DOWNLOADS\terra.png")
earth = pygame.transform.scale(earth, (15, 15))

bodies = []
# Test bodies
body_1 = Body(500, 649.6, 5.9722*10**24, 3, 2.978, 0, 0, 0)
bodies.append(body_1)
body_2 = Body(500, 500, 1.98*10**31, 5, 0, 0, 0, 0)
bodies.append(body_2)
body_3 = Body(500, 650, 7.34767309*10**22, 2, 2.97, 0, 0, 0)
bodies.append(body_3)

running = True
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
    pygame.display.update()
    clock.tick(60)

pygame.quit()
