from __future__ import division
from visual import *
print """
Ruth Chabay Spring 2001
Click to start waves moving.
"""

scene.x = scene.y = 0
scene.width = 1000
scene.height = 1000
scene.forward = (-0.3,-1.5,-2)
scene.background = color.white

ihat=vector(1,0,0)
lamb = 1e-1     ##1e-10
c = 3e8
omega = 2*pi*c/lamb
d = 2*lamb      ## slit spacing

Evec1 = []
Evec2 = []
Evec3 = []
Evec4 = []

dist_to_screen = 4.0*lamb    ## dist to screen
scene.center = (dist_to_screen*.65,-d/2.,0)
ds = lamb/20.
dt = lamb/c/100.
E0 = lamb/3.0

screen = curve(pos = [(dist_to_screen,0,0),(dist_to_screen,0,1.5*d)],
               color=(0.6,0.6,0.6))
slit1 = vector(0, 0, -d/2.) ## coord of slit 1
slit2 = vector(0, 0, d/2.)  ## coord of slit 2

## found by search: see interf02_loc.py
max1 = vector(dist_to_screen,0,0)
max2 = vector(dist_to_screen,0,0.24)
min1 = vector(dist_to_screen,0,0.108) ## or z=0.11

#### vectors from slits to max2:
r1mx = max2 - slit1
r2mx = max2 - slit2
## vectors from slits to min1:
r1mn = min1 - slit1
r2mn = min1 - slit2

# vectors from slits to loc. on screen
dr1mx = ds*norm(r1mx)
dr2mx = ds*norm(r2mx)
dr1mn = ds*norm(r1mn)
dr2mn = ds*norm(r2mn)

rr1mx = slit1 + vector(0,0,0) ## current loc along wave 1
rr2mx = slit2 + vector(0,0,0) ## current loc along wave 2
rr1mn = slit1 + vector(0,0,0) ## current loc along wave 3
rr2mn = slit2 + vector(0,0,0) ## current loc along wave 4

i1 = None
i2 = None
i3 = None
i4 = None

## create first wave (max1)
ct = 0
while ct < 120:
    ea = arrow(pos=rr1mx, axis=(0,E0*cos(2*pi*mag(rr1mx-slit1)/lamb),0), color=color.red,
               shaftwidth=lamb/40.)
    if abs(ea.x - dist_to_screen) < 0.002 and i1==None:
        i1 = ea
##        i1.visible = 0
    else:
        Evec1.append(ea)
    rr1mx = rr1mx + dr1mx
    ct = ct + 1
    
## create second wave (max2)
ct = 0
while ct < 100:
    ea = arrow(pos=rr2mx, axis=(0,E0*cos(2*pi*mag(rr2mx-slit2)/lamb),0), color=(1.,.6,0),
               shaftwidth=lamb/40.)
    if abs(ea.x - dist_to_screen) < 0.002 and i2==None:
        i2 = ea
    else:
        Evec2.append(ea)
    rr2mx = rr2mx + dr2mx
    ct = ct + 1

## create third wave (min1)
ct = 0
while ct < 120:
    ea = arrow(pos=rr1mn, axis=(0,E0*cos(2*pi*mag(rr1mn-slit1)/lamb),0), color=color.red,
               shaftwidth=lamb/40.)
    if abs(ea.x - dist_to_screen) < 0.002 and i3==None:
        i3 = ea
##        i3.visible = 0
    else:
        Evec3.append(ea)
    rr1mn = rr1mn + dr1mn
    ct = ct + 1
    
#### create fourth wave (min2)
ct = 0
while ct < 100:
    ea = arrow(pos=rr2mn, axis=(0,E0*cos(2*pi*mag(rr2mn-slit2)/lamb),0), color=(1.,.6,0),
               shaftwidth=lamb/40.)
    if abs(ea.x - dist_to_screen) < 0.002 and i4==None:
        i4 = ea
    else:
        Evec4.append(ea)
    rr2mn = rr2mn + dr2mn
    ct = ct + 1

scene.autoscale = 0
scene.mouse.getclick()
i1.visible=0
i3.visible=0
i2.axis = vector(0,0,0)
i2.color=color.green
i4.axis=vector(0,0,0)
i4.color = color.green
t=0.0
while 1:
    rate(50)
    t = t+dt
    for ea in Evec1:
       ea.axis = (0,E0*cos(omega*t - 2*pi*mag(ea.pos-slit1)/lamb),0)
    for ea in Evec2:
       ea.axis = (0,E0*cos(omega*t - 2*pi*mag(ea.pos-slit2)/lamb),0)
# superposition
    summx = E0*cos(omega*t - 2*pi*mag(i1.pos-slit1)/lamb)+E0*cos(omega*t - 2*pi*mag(i2.pos-slit2)/lamb)
    i2.axis = vector(0,summx,0)
    
    for ea in Evec3:
       ea.axis = (0,E0*cos(omega*t - 2*pi*mag(ea.pos-slit1)/lamb),0)
    for ea in Evec4:
       ea.axis = (0,E0*cos(omega*t - 2*pi*mag(ea.pos-slit2)/lamb),0)
# superposition
    summn = E0*cos(omega*t - 2*pi*mag(i3.pos-slit1)/lamb)+E0*cos(omega*t - 2*pi*mag(i4.pos-slit2)/lamb)
    i4.axis = vector(0,summn,0)
