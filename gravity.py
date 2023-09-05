import math
# Implementation of the Body class

class Body:
    def __init__(self, xpos, ypos, mass, radius, xspeed, yspeed, xaccel, yaccel):
        self.xpos = xpos
        self.ypos = ypos
        self.mass = mass
        self.radius = radius
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.xaccel = xaccel
        self.yaccel = yaccel

    # TODO fix gravitation calculation
    def calc_accel(self, body):
        xdistance = self.xpos - body.xpos
        ydistance = self.ypos - body.ypos
        distance = (xdistance**2 + ydistance**2)**0.5
        accel = 6.67*10**(-11) * (body.mass/distance**2)
        xangle = math.atan(ydistance/xdistance)
        yangle = math.atan(xdistance/ydistance)
        self.xaccel = math.cos(xangle)*accel
        self.yaccel = math.cos(yangle)*accel

    def calc_speed(self):
        self.xspeed += self.xaccel
        self.yspeed += self.yaccel

    def move(self):
        self.xpos += self.xspeed
        self.ypos += self.yspeed