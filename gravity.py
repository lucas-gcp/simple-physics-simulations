# Implementation of the Body class

class Body:
    def __init__(self, xpos, ypos, radius, xspeed, yspeed, xaccel, yaccel):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.xaccel = xaccel
        self.yaccel = yaccel
    
    def calc_speed(self):
        self.xspeed += self.xaccel
        self.yspeed += self.yaccel

    def move(self):
        self.xpos += self.xspeed
        self.ypos += self.yspeed