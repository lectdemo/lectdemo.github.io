#####################
#Ball in a half-pipe#
#Michael Malahe     #
#2006               #
#####################

#ANIMATION PARAMETERS
tickrate = 20
ballsize = 1
speed = 1

#Modules
from visual import *
import visual as v
from math import *

#PHYSICS PARAMETERS
g = 9.8
dt = 0.001
curveres = 0.01
t = 0
offset = vector(0,1,0)
rad = 1
a = 0.01
side = 0
ki = 0

#Scene alignment
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

#Motion function
def xyz(off,r,t):
    return vector(-r*cos(t),-r*sin(t),0)+off

#Cleanup
removal = []
init = 0

#Timeline control
while 1:
    if init == 0:
        #Visual elements
        ball = sphere(pos=xyz(offset,rad,0),radius=0.05)
        c = curve(pos=[vector(x,-rad*sqrt(1-x**2),0)+offset for x in arange(-1,1+curveres,curveres)])
        t = 0
        init = 1
    if scene.mouse.clicked:
        init = 0
        c = scene.mouse.getclick()
        removal.append(ball)
        #Main loop
        stopper = framestop(tickrate)
        while 1:
            if ball.pos.y>=rad and side == 0:
                side = 1
                ball.pos.y = rad
                for e in removal:
                    e.visible = 0
                ball = sphere(pos=xyz(offset,rad,t),radius=0.05)
            elif ball.pos.y>=rad and side == 1:
                side = 0
                ball.pos.y = rad
                for e in removal:
                    e.visible = 0
                ball = sphere(pos=xyz(offset,rad,t),radius=0.05)
            #Acceleration
            if ball.pos.x<0 and side == 0:
                dt = (1+a*abs(cos(t)))*dt
            elif side == 0:
                dt = dt/(1+a*abs(cos(t)))
            if ball.pos.x>0 and side == 1:
                dt = (1+a*abs(cos(t)))*dt
            elif side == 1:
                dt = dt/(1+a*abs(cos(t)))
            rate(60)
            if side == 0:
                t += dt
            if side == 1:
                t -= dt
            ball.pos = xyz(offset,rad,t)
            ki = 1
            if stopper.tick():
                removal.append(copy.copy(ball))
        while 1:
            if scene.mouse.clicked:
                c = scene.mouse.getclick()
                break
        for e in removal:
            e.visible = 0



    
