import math
# Implementation of the Body class


class Body:
    def __init__(self, xpos, ypos, mass, xspeed, yspeed, xaccel_in, yaccel_in, density, visualizaton_scale,
                 simulation_scale):
        self.visualization_scale = visualizaton_scale
        self.simulation_scale = simulation_scale
        self.xpos_calc = xpos
        self.ypos_calc = ypos
        self.mass = mass
        self.radius = (((3*self.mass)/(4*math.pi*density))**(1/12))/10
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.xaccel = self.xaccel_in = xaccel_in
        self.yaccel = self.yaccel_in = yaccel_in
        self.xdistance = (xpos - 500)*self.visualization_scale
        self.ydistance = (ypos - 500)*self.visualization_scale
        self.xpos = self.xdistance + 500
        self.ypos = self.ydistance + 500

    def calc_accel(self, body):
        xdistance = abs(self.xpos_calc - body.xpos_calc)*self.simulation_scale
        ydistance = abs(self.ypos_calc - body.ypos_calc)*self.simulation_scale
        distance = (xdistance**2 + ydistance**2)**0.5
        accel = 6.67*10**(-11) * (body.mass/distance**2)

        angle = math.atan2(ydistance, xdistance)
        xdir = math.copysign(1, (body.xpos_calc - self.xpos_calc))
        ydir = math.copysign(1, (body.ypos_calc - self.ypos_calc))

        self.xaccel += math.cos(angle)*accel*xdir
        self.yaccel += math.sin(angle)*accel*ydir

    def clear_accel(self):
        self.xaccel = self.xaccel_in
        self.yaccel = self.yaccel_in

    def calc_speed(self):
        self.xspeed += self.xaccel
        self.yspeed += self.yaccel

    def move(self):
        self.xpos_calc += self.xspeed
        self.xpos += self.xspeed*self.visualization_scale
        self.ypos_calc += self.yspeed
        self.ypos += self.yspeed*self.visualization_scale
