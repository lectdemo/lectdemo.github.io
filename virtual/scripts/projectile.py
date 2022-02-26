#################
#Projectile     #
#Michael Malahe #
#2006           #
#################

#ANIMATION PARAMETERS
tickrate = 10
ballsize = 0.5
speed = 1

#Modules
from visual import *

#PHYSICS PARAMETERS
g = 9.8
fang = radians(45)
fspeed = 15
dt = 0.025

#Scene alignment
scene.center=(12,1,0)
scene.fullscreen = 1

#Framestop class
class framestop:
    def __init__(self,frames):
        self.frames = frames
        self.frame = 0
    def tick(self):
        self.frame += 1
        if self.frame == self.frames:
            self.frame = 0
            return 1
        return 0
#Cleanup
removal = []
init = 0

#Timeline control
while 1:
    if init == 0:
        #Visual elements
        floor = box(pos=(12,0,0),axis=(1,0,0),length=24,width=10,height=0.1)
        ball = sphere(pos=(0,ballsize,0), radius=ballsize)
        ball.vel = vector(fspeed*cos(fang),fspeed*sin(fang),0)
        init = 1
    if scene.mouse.clicked == 1:
        c = scene.mouse.getclick()
        init = 0
        removal.append(floor)
        removal.append(ball)
        #Main loop
        stopper = framestop(tickrate)
        stopper.frame = tickrate-1
        while ball.pos.y>0:
            rate(60)
            if stopper.tick():
                removal.append(copy.copy(ball))
            rate(1/dt)
            ball.vel += vector(0,-g,0)*dt*speed
            ball.pos += ball.vel*dt*speed
        ball.visible = 0
        while 1:
            if scene.mouse.clicked:
                c = scene.mouse.getclick()
                break
        for e in removal:
            e.visible = 0





    
