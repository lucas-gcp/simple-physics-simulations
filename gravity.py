import math
# Implementation of the Body class


class Body:
    def __init__(self, xpos, ypos, mass, radius, xspeed, yspeed, xaccel_in, yaccel_in):
        self.xpos = xpos
        self.ypos = ypos
        self.mass = mass
        self.radius = radius
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.xaccel = self.xaccel_in = xaccel_in
        self.yaccel = self.yaccel_in = yaccel_in

    def calc_accel(self, body):
        xdistance = abs(self.xpos - body.xpos)*10**9
        ydistance = abs(self.ypos - body.ypos)*10**9
        distance = (xdistance**2 + ydistance**2)**0.5
        accel = 6.67*10**(-11) * (body.mass/distance**2)

        angle = math.atan2(ydistance, xdistance)
        xdir = math.copysign(1, (body.xpos - self.xpos))
        ydir = math.copysign(1, (body.ypos - self.ypos))

        self.xaccel += math.cos(angle)*accel*xdir
        self.yaccel += math.sin(angle)*accel*ydir

    def clear_accel(self):
        self.xaccel = self.xaccel_in
        self.yaccel = self.yaccel_in

    def calc_speed(self):
        self.xspeed += self.xaccel
        self.yspeed += self.yaccel

    def move(self):
        self.xpos += self.xspeed
        self.ypos += self.yspeed
