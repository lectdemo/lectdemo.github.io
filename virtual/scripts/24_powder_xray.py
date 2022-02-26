from visual import *

print """
Ruth Chabay Spring 2001
Click to see formation of x-ray powder rings.
"""

scene.x = scene.y = 0
scene.height = scene.width = 700

ihat=vector(1,0,0)
jhat=vector(0,1,0)
khat=vector(0,0,1)

a1 = arange(0,2*pi,pi/4.)

R1 = 2.0
l1 = []
for theta in a1:
    b = box(pos=(0,0,0), size=(.5,0.02,.5), color=(.5,.5,1))
    b.rotate(axis=khat, angle=-2*pi/5.)
    b.rotate(axis=jhat, angle=theta)
    b.pos=(R1*cos(theta),0,-R1*sin(theta))
    l1.append(b)
    
R2=1.5
l2=[]
phi=pi/6.
for theta in a1:
    b = box(pos=(0,0,0), size=(.5,0.02,.5), color=(.5,1,.5))
    b.rotate(axis=khat, angle=-pi/3.)
    b.rotate(axis=jhat, angle=theta+phi)
    b.pos=(R2*cos(theta+phi),0,-R2*sin(theta+phi))
    l2.append(b)
R3=1.0
l3=[]
phi=pi/3.
for theta in a1:
    b = box(pos=(0,0,0), size=(.5,0.02,.5), color=(1,.5,.5))
    b.rotate(axis=khat, angle=-3*pi/7.)
    b.rotate(axis=jhat, angle=theta+phi)
    b.pos=(R3*cos(theta+phi),0,-R3*sin(theta+phi))
    l3.append(b)
scene.mouse.getclick()

rl1 = []
for bb in l1:
    d = dot(jhat,bb.up)
    dang = (pi/2. - acos(d))
    ee = -cross(jhat,bb.up)
##    ea = arrow(pos=bb.pos, axis=ee)
    vv = rotate(jhat, angle=2*dang, axis=ee)
##    va = arrow(pos=bb.pos, axis=-vv, color=color.red)
    ray1 = arrow(pos=(bb.pos-jhat), axis=jhat, shaftwidth=0.02, color=bb.color)
    rl1.append(ray1)
    ray2 = arrow(pos=bb.pos, axis=vv, shaftwidth=0.02, color=bb.color)
    rl1.append(ray2)
yv = ray2.pos+ray2.axis
yy = yv.y
rad = mag(vector(0,yy,0)-yv)
r1 = ring(pos=(0,yy,0), axis=jhat, radius=rad, thickness=0.05, color=l1[0].color)
rl1.append(r1)
scene.mouse.getclick()

for obj in rl1:
    obj.visible = 0
scene.mouse.getclick()

rl2=[]
for bb in l2:
    d = dot(jhat,bb.up)
    dang = (pi/2. - acos(d))
    ee = -cross(jhat,bb.up)
##    ea = arrow(pos=bb.pos, axis=ee)
    vv = rotate(jhat, angle=2*dang, axis=ee)
##    va = arrow(pos=bb.pos, axis=-vv, color=color.red)
    ray1 = arrow(pos=(bb.pos-jhat), axis=jhat, shaftwidth=0.02, color=bb.color)
    rl2.append(ray1)
    ray2 = arrow(pos=bb.pos, axis=vv*1.5, shaftwidth=0.02, color=bb.color)
    rl2.append(ray2)
yv = ray2.pos+ray2.axis
yy = yv.y
rad = mag(vector(0,yy,0)-yv)
r1 = ring(pos=(0,yy,0), axis=jhat, radius=rad, thickness=0.05, color=l2[0].color)
rl2.append(r1)
scene.mouse.getclick()

for obj in rl2:
    obj.visible = 0
scene.mouse.getclick()

rl3=[]
for bb in l3:
    d = dot(jhat,bb.up)
    dang = (pi/2. - acos(d))
    ee = -cross(jhat,bb.up)
##    ea = arrow(pos=bb.pos, axis=ee)
    vv = rotate(jhat, angle=2*dang, axis=ee)
##    va = arrow(pos=bb.pos, axis=-vv, color=color.red)
    ray1 = arrow(pos=(bb.pos-jhat), axis=jhat, shaftwidth=0.02, color=bb.color)
    rl3.append(ray1)
    ray2 = arrow(pos=bb.pos, axis=vv*0.8, shaftwidth=0.02, color=bb.color)
    rl3.append(ray2)
yv = ray2.pos+ray2.axis
yy = yv.y
rad = mag(vector(0,yy,0)-yv)
r1 = ring(pos=(0,yy,0), axis=jhat, radius=rad, thickness=0.05, color=l3[0].color)
rl3.append(r1)
scene.mouse.getclick()

for obj in rl3:
    obj.visible = 0
scene.mouse.getclick()

for obj in rl1+rl2+rl3:
    obj.visible = 1


