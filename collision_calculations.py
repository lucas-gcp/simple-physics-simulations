import pygame

class Block:
    def __init__(self, xpos, ypos, xsize, ysize, speed, mass, color):
        self.xpos = xpos
        self.ypos = ypos
        self.xsize = xsize
        self.ysize = ysize
        self.speed = speed
        self.mass = mass
        self.surface = pygame.Surface((self.xsize, self.ysize))
        self.rect = self.surface.get_rect(topright=(self.xpos, self.ypos))
        self.color = color
