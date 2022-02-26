from __future__ import division
from visual import *
scene.background = color.white
scene.width=1024
scene.height=768

print """
Ruth Chabay 2003
Calculate E of ring by superposition of E of
point charges.
Magenta arrow is deltaE from this segment;
orange arrow is net field so far.

Click to advance. Zoom out when E gets large.
"""

def axes(a=10):
    axes=curve(pos=[(-a,0,0),(a,0,0),(0,0,0),(0,-a,0),(0,a,0),(0,0,0),
                    (0,0,-a),(0,0,a)], color=color.black)
    scene.autoscale = 0
axes(4)
cc=color.black
##zl=label(pos=(4,0,0), text="z", color=cc, opacity=0, linecolor=cc)
##yl=label(pos=(0,4,0), text="y", color=cc, opacity=0, linecolor=cc)
##xl=label(pos=(0,0,-4),text="x", color=cc, opacity=0, linecolor=cc)
####*************
a = ring(pos=(-3,0,0), radius=3, color=color.red, thickness=0.2)
obsloc = vector(4,0,0)
Ea = arrow(pos=obsloc, axis=(0,0,0), shaftwidth=0.3, color=color.magenta)
Eb = arrow(pos=obsloc, axis=(0,0,0), shaftwidth=0.3, color=(1,.7,0))
dtheta=pi/10
angles = arange(0,2*pi,dtheta)
b=50
scene.mouse.getclick()
pt = sphere(pos=(-3,a.radius,0), color=color.cyan, radius=a.thickness*1.2)
ra = arrow(pos=pt.pos, axis=(0,0,0),color=color.green, shaftwidth=0.1)
for theta in angles:
    pt.pos = (-3,a.radius*cos(theta),a.radius*sin(theta))
    ra.pos=pt.pos
    r = Ea.pos - ra.pos
    ra.axis = r
    Ea.axis = (b/mag(r)**2)*norm(r)
    Eb.axis = Eb.axis+Ea.axis
##    print Ea.axis
    scene.mouse.getclick()
ra.visible = 0
Ea.visible = 0
pt.visible = 0

