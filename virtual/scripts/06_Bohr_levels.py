from __future__ import division
from visual import *
from visual.graph import *

## energy levels of Bohr atom; graphs of K, U, K+U
## Ruth Chabay 2003-03-16

print """Click in display to cycle through levels.
Click on blue square in lower l.h. corner to pause.
Click on blue square again to resume.
"""

scene.x = scene.y = 0
scene.height = 400
scene.width = 400
scene.title = "Bohr model of the atom"
background = color.white
flash = color.black
scene.background = background

def circle(radius, thickness, tint):
    dtheta = 2*pi/50
    angles=arange(0,2*pi+dtheta, dtheta)
    c = curve(x=radius*cos(angles), y=radius*sin(angles), z=0,
              color=tint, radius=thickness)
    return c

# atom
nucleus=sphere(radius=1e-11, color=color.red)
hbar = 1.05e-34
oofpez = 9e9
e = 1.6e-19
m = 9e-31
levels=[]
for N in arange(1,6,1):
    r = (N**2)*(hbar**2)/(oofpez*(e**2)*m)
    levels.append(circle(radius=r, thickness=0, tint=(0,0.5,0)))
scene.autoscale = 0

up = 1  ## increase energy
gbackground = (1,1,1)#(0.5,0.5,0.5)
# energy graphs
Eg = gdisplay(x=0, y=400, title="energy", height=200,
              xtitle = "time", background=gbackground, foreground=color.black)
Kg = gcurve(color=(0,0,0.8))
Ug = gcurve(color=(0,0.8,0))
KUg = gcurve(color=(0.8,0,0.8))

# well and levels
Wg = gdisplay(x=400,y=0,width=400, ymax=0, ymin=-14.0, xmax=36*0.53e-10,
              background=gbackground, foreground=color.black)
rr = arange(0.53e-10, 36*0.53e-10, 0.53e-10)
U = gcurve()
for r in rr:
    Uel = -oofpez*e/r
    U.plot(pos=(r,Uel))
states=[]
for N in arange(1,6,1):
    r = N**2*0.53e-10
    E = -13.6/N**2
    lvl = gcurve(pos=([(0,E), (2*r,E)]))
    states.append(lvl)
states[0].gcurve.color=color.magenta

# orbits
N=1
r=(N**2)*0.53e-10
omega = N*hbar/(m*r**2)
electron=sphere(radius=4e-11, color=color.blue, pos=(r,0,0))
dt = (2*pi/omega)/100
t = 0.0

rs = 1.2*(5**2)*(hbar**2)/(oofpez*(e**2)*m)
Stop = box(pos=(-1.1*rs, -rs,0), color=(0,0,0.5),
              size=(12e-11,12e-11,1e-12))
stopped = 0
##
##stopped = 1
##
while 1:
    rate(400)
    if scene.mouse.clicked:
        scene.mouse.getclick()
        if scene.mouse.pick is Stop:
            stopped = not(stopped)
            continue
        scene.background = flash
        rate(2)
        scene.background = background
        rate(400)
        if up:
            states[N-1].gcurve.color=states[N-1].gcurve.display.foreground
            N = N + 1
            states[N-1].gcurve.color=color.magenta
            if N is 5:
                up = 0
        else:
            states[N-1].gcurve.color=states[N-1].gcurve.display.foreground
            N = N -1
            states[N-1].gcurve.color=color.magenta
            if N is 1:
                up = 1
        r=(N**2)*0.53e-10
        omega = N*hbar/(m*r**2)
    if stopped:
        continue
    else:
        electron.pos = vector(r*cos(omega*t), r*sin(omega*t), 0)
        t = t+dt
        K = 0.5*oofpez*(e**2)/r
        U = -oofpez*(e**2)/r
        Kg.plot(pos=(t,K))
        Ug.plot(pos=(t,U))
        KUg.plot(pos=(t,(K+U)))
        
        
    
    
    
