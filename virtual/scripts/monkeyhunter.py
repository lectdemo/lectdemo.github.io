#################
#Monkey & Hunter#
#Michael Malahe #
#2006           #
#################

#ANIMATION PARAMETERS
tickrate = 10
ballsize = 0.5
speed = 1
mpos = (15.,10.,0)

#Modules
from visual import *
from math import *

#PHYSICS PARAMETERS
g = 3
fspeed = 7
dt = 0.025

#Scene alignment
scene.center=(10,2,0)
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
        fang = atan(mpos[1]/mpos[0])
        cannon = cylinder(axis=(cos(fang),sin(fang),0), radius=ballsize)
        ball = sphere(pos=cannon.pos+cannon.axis, radius=ballsize)
        ball.vel = vector(fspeed*cos(fang),fspeed*sin(fang),0)
        ball2 = sphere(pos=mpos, radius=ballsize)
        ball2.vel = vector(0,0,0)
        ref = curve(pos=[cannon.pos,ball2.pos])
        init = 1
    if scene.mouse.clicked == 1:
        c = scene.mouse.getclick()
        init = 0
        removal.append(cannon)
        removal.append(ball)
        removal.append(ball2)
        removal.append(ref)
        #Main Loop
        stopper = framestop(tickrate)
        while ball.pos.y>-20:
            if ball.x > mpos[0]:
                break
            rate(60)
            if stopper.tick():
                removal.append(copy.copy(ball))
                removal.append(copy.copy(ball2))
            rate(1/dt)
            ball.vel += vector(0,-g,0)*dt*speed
            ball.pos += ball.vel*dt*speed
            ball2.vel += vector(0,-g,0)*dt*speed
            ball2.pos += ball2.vel*dt*speed
        removal.append(copy.copy(ball))
        removal.append(copy.copy(ball2))
        ball2.visible = 0
        ball.visible = 0
        while 1:
            if scene.mouse.clicked:
                c = scene.mouse.getclick()
                break
        for e in removal:
            e.visible = 0




    
