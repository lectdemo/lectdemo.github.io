from __future__ import division
from visual import *
from visual.graph import *
from visual.controls import *

## Simplified Franck-Hertz experiment visualization
## Ruth Chabay 2003-03-16

print """Simplified Franck-Hertz experiment.
Electric force does work on single electron (blue),
which gains K and collides with single Hg atom (gray).
Use slider to set electric force on electron (dVacc).
Click "GO" to release electron.
Click "reset" to start over (can set electric force to new value).
Orange arrow represents electric force on electron.
Green arrow represents electron's momentum.
"""

scene.x=scene.y=0
scene.width=800
scene.height=300
scene.title="Franck-Hertz experiment"
scene.background=color.white
scene.foreground=color.black

def set_dV(vs):
    global dVacc, E, L
    dVacc = vs.value
    E = vector(-dVacc/L,0,0)
##    print dVacc, mag(E)

def go():
    global GO
    GO = 1

def reset():
    global hue, Ke
    clr = color.rgb_to_hsv(Ke.color)
    hue = clr[0]
    electron.pos = vector(-L/2,0,0)
    electron.p = vector(0,0,0)
    Far.pos = electron.pos
    Far.axis=(0,0,0)
    par.pos = electron.pos
    par.axis = vector(0,0,0)
    Hg.color=(.6,.6,.6)
    t=0.0
    hue = hue+0.15
    if hue > 1:
        hue = hue-1
    Ke=gcurve(color=color.hsv_to_rgb((hue,1,0.8)))

# parameters
L=0.5
E0 = 4.9*1.6e-19
ltblu=color.cyan
EMAX = 10.

#controls
cw = controls(x=600,y=300, width=200, height=300, title="electric force")
cw.display.background=color.white
cw.display.foreground=color.black
sdV = slider(pos=(0,-80,0), axis=(0,2*80,0), text="deltaVacc",min=0, max=EMAX,
                action=lambda: set_dV(sdV), color=color.orange)
sdV.value = 1.0
set_dV(sdV)
gobtn = button(pos=(40,0,0), size=(20,20), text="GO", action=lambda: go())
reset_button=button(pos=(-40,0,0), size=(20,20), text="reset",
                    action=lambda: reset())
GO=0

# electron and Hg atom
electron=sphere(pos=(-L/2,0,0), radius=0.005, color=ltblu)
electron.q = -1.6e-19
electron.m = 9e-31
electron.p = electron.m*vector(0,0,0)
Far = arrow(pos=electron.pos, shaftwidth=electron.radius, color=color.orange,
            axis=(0,0,0))
Fscale = (L/40)/abs(electron.q*mag(E))
offset = vector(0,electron.radius,0)
par = arrow(pos=electron.pos+offset, color=color.green,
            shaftwidth=electron.radius, axis=(0,0,0))
pscale = (2*L/10)/(1e-24)

Hg = sphere(pos=(L/4,0,0), radius=2*electron.radius, color=color.white)
Hg.v = vector(0,0,0)
# emitter and collector
emitter=box(pos=(-1.1*L/2,0,0), size=(0.001,0.14,0.14), color=color.blue)
collector = box(pos=(1.1*L/2,0,0), size=(0.001,0.14,0.14), color=color.red)
scene.range = 1.6*L/2.
scene.autoscale = 0
dt = 1e-10

# graphs
grafs = gdisplay(x=0,y=300, title="electron kinetic energy", width=600,
                 height=300, xtitle="position", ytitle="K (eV)",
                 xmax=1.1*L, ymax=EMAX,
                 background=color.white, foreground=color.black)
Ke=gcurve(color=(0.8,0,0))
while 1:
    cw.interact()
    if not(GO):
        continue
    collide=0
    t=0.0
    while electron.pos.x < collector.pos.x:
        rate(1000)
        F = electron.q * E
        electron.p = electron.p + F*dt
        electron.pos = electron.pos + (electron.p/electron.m)*dt
        Hg.pos = Hg.pos + Hg.v*dt
        Far.pos = electron.pos
        Far.axis = F*Fscale
        par.pos = electron.pos+offset
        par.axis = pscale*electron.p
        K=mag(electron.p)**2/(2*electron.m)
        K2 = K/1.6e-19
        Ke.plot(pos=(electron.x+L/2.,K2))
        if (mag(Hg.pos - electron.pos) < electron.radius) and (collide is 0):
            if K >= E0:
                collide = 1
                K = K-E0
                pmag = sqrt(2*electron.m*K)
                electron.p = vector(pmag,0,0)
                Hg.color=(1,.4,1)
        t=t+dt
    GO=0
print t

    
    
