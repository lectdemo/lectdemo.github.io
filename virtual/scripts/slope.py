#################
#Ball on a slope#
#Michael Malahe #
#2006           #
#################

#ANIMATION PARAMETERS
tickrate=50
ballsize=0.2
speed = 10
slopeangle=45

#Modules
from visual import *
from math import *

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

#Scene alignment
scene.fullscreen = 1

#Cleanup
slopeangle = radians(slopeangle)
removal = []
init = 0

#Timeline control
while 1:
    if init == 0:
        #Initialisation
        slope = box(pos=(0,0,0),axis=(cos(slopeangle),sin(slopeangle),0),length=6,width=0.4,height=0.1)
        ball = sphere(pos=(0.5*slope.length*cos(slopeangle)-ballsize*sin(slopeangle),
                           0.5*slope.length*sin(slopeangle)+ballsize*cos(slopeangle),0),radius=ballsize)
        ball.p = 0
        scene.autoscale = 0
        scene.scale = (0.22,0.22,0.22)
        init = 1
    if scene.mouse.clicked == 1:
        c = scene.mouse.getclick()
        init = 0
        removal.append(slope)
        removal.append(ball)
        #Main Loop
        dt = 0.01
        dp = -0.0010*speed
        stopper = framestop(tickrate)
        while 1:
            if ball.pos.y<-0.5*slope.length*sin(slopeangle)+ballsize*cos(slopeangle):
                ball.visible = 0
                break
            rate(60)
            if stopper.tick():
                removal.append(copy.copy(ball))
            ball.p += dp*sin(slopeangle)
            ball.x += ball.p*dt*(cos(slopeangle))
            ball.y += ball.p*dt*(sin(slopeangle))
            ball.rotate(angle=-(ball.p*dt/(ball.radius*pi)),axis=(0,0,1),origin=ball.pos)
        while 1:
            if scene.mouse.clicked:
                c = scene.mouse.getclick()
                break
        for e in removal:
            e.visible = 0

    
