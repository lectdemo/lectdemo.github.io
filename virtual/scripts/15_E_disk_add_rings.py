from __future__ import division
from visual import *
scene.background = color.white
scene.width=1024
scene.height=768

print """
Ruth Chabay 2004
Add electric field of concentric rings to get
E of disk on axis.
Click to advance.
"""



def axes(a=10):
    axes=curve(pos=[(-a,0,0),(a,0,0),(0,0,0),(0,-a,0),(0,a,0),(0,0,0),
                    (0,0,-a),(0,0,a)], color=color.black)
    scene.autoscale = 0
axes(4)
####*************
obsloc = vector(0,0,0)
eap = obsloc.x
sf=1
Ea = arrow(pos=obsloc, axis=(0,0,0), shaftwidth=0.3, color=color.orange)
for R in arange(0.2,5,0.2):
    scene.mouse.getclick()
    a = ring(pos=(-3,0,0), radius=R, color=color.red, thickness=0.09)
    Ea.axis = Ea.axis + sf*2*pi*R/(R**2 + (eap+2)**2)**1.5*vector(1,0,0)
