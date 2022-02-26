from __future__ import division
from visual import *
print """
Ruth Chabay Spring 2001
Click to start waves moving.
"""

scene.x = scene.y = 0
scene.width = 1024
scene.height = 768
scene.background = color.white

SHOWDECREASE = 1

ihat=vector(1,0,0)
lamb = 2.     ##1e-10
c = 3e8
omega = 2*pi*c/lamb
d=2*lamb
L=2*lamb
antenna = cylinder(pos=(0,-L/2,0), axis=(0,L,0), color=(.7,.7,.7), radius=0.5)

Evec1 = []
Evec2 = []

dist_to_screen = 4.0*lamb    ## dist to screen
dts = dist_to_screen
##scene.center = (dist_to_screen*.65,-d/2.,0)
ds = lamb/20.
dt = lamb/c/100.
##E0 = lamb/3.0
E0=lamb*5

##slit1 = vector(0, 0, -d/2.) ## coord of slit 1
slit1 = vector(0,0,0)
rvectors=[]
dtheta = pi/3
for theta in arange(0,2*pi,dtheta):
    r1 = vector(dts*cos(theta),0,dts*sin(theta))
    rvectors.append(r1)
    
## create waves
for r1 in rvectors:
    dr1 = ds*norm(r1)
    rr1 = slit1 + 10*dr1     ##vector(0,0,0) ## current loc along wave 1
    i1 = None
    ct = 0
    while ct < 120:
        ea = arrow(pos=rr1, axis=(0,(E0*cos(2*pi*mag(rr1-slit1))/lamb),0), color=color.orange,
                   shaftwidth=lamb/40.)
        ba = arrow(pos=rr1, axis=(0,0,0), color=color.cyan,
                   shaftwidth=lamb/40., visible=0)
        ea.B = ba
        Evec1.append(ea)
        rr1 = rr1 + dr1
        ct = ct + 1
            
scene.autoscale = 0

t=0.0
while 1:
    rate(50)
    if scene.mouse.clicked:     ## toggle vis of mag field vectors
        scene.mouse.getclick()
        for a in Evec1:
            a.B.visible = not(a.B.visible)
    t = t+dt
    for ea in Evec1:
        if SHOWDECREASE:
            decrease = 1/(mag(ea.pos)+lamb/20)
        else:
            decrease = 1.0
        ea.axis = (0,decrease*E0*cos(omega*t - 2*pi*mag(ea.pos-slit1)/lamb),0)
        ea.B.axis = -cross(ea.axis,ihat)*.7

 
