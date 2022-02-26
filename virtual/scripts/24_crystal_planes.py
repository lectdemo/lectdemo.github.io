from visual import *

print """
Ruth Chabay Spring 2001
Click to see planes containing many atoms.
"""

scene.x = scene.y = 0
scene.width = scene.height = 800
scene.forward = (1,-0.8,-2)

def wirebox (s=5., boxcolor=(0,1,1)):
    pts = [(-s, -s, -s), (-s, -s, s), (-s, s, s),
           (-s, s, -s), (-s, -s, -s), (s, -s, -s),
           (s, s, -s), (-s, s, -s), (s, s, -s),
           (s, s, s), (-s, s, s), (s, s, s),
           (s, -s, s), (-s, -s, s), (s, -s, s),(s, -s, -s)]
    c=curve (color=boxcolor, radius=0.05, pos=pts)
    return c

for x in arange(-2, 3, 2):
    for z in arange (-2, 3, 2):
        for y in arange (-2, 3, 2):
            a=sphere(pos=(x,y,z), radius = 0.3, color=(1,0,1))

for x in arange (-1, 3, 2):
    for z in arange (-1, 3, 2):
        for y in arange (-1, 3, 2):
            a=sphere(pos=(x,y,z), radius = 0.3, color=(0,1,1))

scene.autoscale=0

unit = wirebox(s=1, boxcolor=(.8,.8,.8))
unit.pos=unit.pos+vector(-1,-1,-1)

plane1=box (pos=(0,0,0), size = (6,0.01,6),color = (.8,.8,.8), visible=0)

plane2 = box(pos = (0, 0, 0), size = (6,0.01,6), color = (.8,.8,.8), visible=0)
plane2.rotate(axis = (0,0,1), angle=pi/4.)

scene.mouse.getclick()
unit.visible = 0
plane1.visible = 1
pv=1
planes=[plane1, plane2]

while 1:
    scene.mouse.getclick()
    pv = pv+1
    if pv > 2: pv=1
    plane1.visible = (pv==1)
    plane2.visible = (pv==2)
