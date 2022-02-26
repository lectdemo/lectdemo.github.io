from visual import *

print """
Bruce Sherwood Fall 2000
Click to cycle through different angular momentum cases:
   rotation == 0: barbell orientation doesn't change;
      (mounted on frictionless axle, no torque acts on it)
   1: barbell rotates at same rate as rod
   2: barbell rotates a lot
"""

scene.background = color.white
scene.width=scene.height=800
scene.x = scene.y = 0
rmass = 0.2
L = 2.
rod=cylinder(pos=(0,0,0), axis=(4,0,0), radius=0.03, color=(1,.9,0))
barbell = frame()
offset = vector(0,0,1.5*rmass)
rod2=cylinder(frame=barbell, pos=(0,0,0), axis=-offset,
              radius=rod.radius, color=rod.color)
s1=sphere(frame=barbell, pos=(0,L/2.,0), radius=rmass, color=(1,0,0))
s1.mass=0.01
s2=sphere(frame=barbell, pos=(0,-L/2.,0), radius=rmass, color=(0,0,1))
s2.mass=0.01
rd=cylinder(frame=barbell, pos=s1.pos, axis=(s2.pos-s1.pos),
            color=(1,1,1), radius=0.04)
barbell.trail=curve(color=(.6,.6,.6))

barbell.Icm = 2*s1.mass*(L/2.0)**2
barbell.pos = rod.pos+rod.axis+offset
barbell.Iorig = 2*s1.mass*(mag(rod.axis)**2)

omegaCM = vector(0,0,pi)
omega = vector(0,0,pi/5.)
dt = 0.05
t = 0.0
scene.range=5
Lscale = 2.0/0.1

LT=arrow(pos=rod.pos, axis=(0,0,0), color=color.cyan,
         shaftwidth = 0.2)
LR=arrow(pos=barbell.pos, axis=(0,0,0), color=color.green,
         shaftwidth = 0.2)

rotation = 0
direction = 1
while 1:
    while 1:
        if scene.mouse.clicked:
            scene.mouse.getclick()
            break
        rate(30)
        dtheta = mag(omegaCM)*dt
        dphi = mag(omega)*dt
        rod.rotate(angle=dphi, axis=omega, origin=(0,0,0))
        barbell.pos = rod.pos+rod.axis+offset
        Ltrans = barbell.Iorig*omega
        Lrot = vector(0,0,0)
        if rotation == 1:
            barbell.rotate(angle=dphi, axis=omegaCM, origin=(barbell.pos))
            Lrot = barbell.Icm*omega 
        if rotation == 2:
            barbell.rotate(angle=direction*dtheta, axis=omegaCM, origin=(barbell.pos))
            Lrot = direction*barbell.Icm*omegaCM
        LT.axis = Ltrans*Lscale
        LR.pos = barbell.pos
        LR.axis = Lrot*Lscale
        t = t+dt
    rotation = rotation+1
    if rotation > 2:
        rotation = 0
        direction = -direction
