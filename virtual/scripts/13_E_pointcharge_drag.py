from visual import *
scene.background = color.white
# white background better for projection in most rooms
print """
Ruth Chabay Spring 2001
Electric field of a point charge.
Drag the charge and observe the changes
in the electric field. Rotate (right
button) to give greater sense of 3D.

"""

scene.height = scene.width = 1000
scene.x = scene.y = 0
scene.forward = (-0.2,-0.2,-1)

obsloc = []
arrows = []

xx = arange(-12.0, 13.0, 3.0)
K=15.
q = sphere(pos=(0,0,0), color=color.red, radius=0.4, charge=1.0)

for x in xx:
    for y in xx:
        for z in xx:
            obsloc.append((x,y,z))
            a=arrow(pos=(x,y,z), axis=(0, 0.1, 0), color=(1.0, .5, 0),
                    shaftwidth= 0.2)
            r = a.pos-q.pos
            if mag(r) == 0:
                a.axis=vector(0,0,0)
            else:
                E = K*q.charge*r/(mag(r)**3)
                a.axis=E
            arrows.append(a)

scene.autoscale = 0
obs = array(obsloc)
drag = None

while 1:
    if scene.mouse.events:
        m = scene.mouse.getevent()
        if m.drag and m.pick is q:
            drag = m.pick
            drag_pos = m.pickpos
            scene.cursor.visible = 0
        elif m.drop:
            drag = None
            scene.cursor.visible = 1
    if drag:
        qp = scene.mouse.project(normal=(0,0,1), d=0)
        if qp and qp != drag_pos:
            q.pos += qp - drag_pos
            drag_pos = qp
            r=obs-q.pos
            rmag=mag(r)
            rmag3=reshape(rmag*rmag*rmag, (len(rmag),1))
            E=K*q.charge*r/rmag3
        for i in arange(len(obs)):
            if rmag[i]==0:
                E[i]=vector(0,0,0)
            arrows[i].axis = E[i]

