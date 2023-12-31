import pygame
from gravitycalculations import Body

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
def draw_body(surface, color, bodies_list):
    for i,b in enumerate(bodies_list):
        pygame.draw.circle(surface, color[i], (b.xpos, b.ypos), b.radius)

def gravity_run():
    pygame.init()

    screenWidth, screenHeight = 1000, 1000
    displayname = pygame.display.set_caption("Gravity test")
    screen = pygame.display.set_mode([screenWidth, screenHeight], pygame.RESIZABLE)
    clock = pygame.time.Clock()

    colorlist = ['blue', 'cyan', 'gold', 'gray', 'green', 'orange', 'purple', 'red', 'violet', 'yellow', 'white']

    earth = pygame.image.load(R".\resources\earth.png")
    earth = pygame.transform.scale(earth, (15, 15))

    visualization_scale = 1
    simulation_scale = 10**9

    bodies = []
    # Test bodies
    body_1 = Body(500, 649.6, 5.9722*10**24, 2.978, 0, 0, 0, 5515, visualization_scale, simulation_scale)
    bodies.append(body_1)
    body_2 = Body(500, 500, 1.98*10**31, 0, 0, 0, 0, 1408, visualization_scale, simulation_scale)
    bodies.append(body_2)
    body_3 = Body(500, 650, 7.34767309*10**22, 2.95, 0, 0, 0, 3344, visualization_scale, simulation_scale)
    bodies.append(body_3)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode([event.w, event.h], pygame.RESIZABLE)

        update_body(bodies)

        screen.fill('black')
        # Test the draw_body function
        #screen.blit(earth, (body_1.xpos-5, body_1.ypos-5))
        draw_body(screen, colorlist, bodies)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
