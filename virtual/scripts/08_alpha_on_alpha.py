from visual import *

print """
Bruce Sherwood Fall 2000
Alpha particle incident on stationary alpha particle.
Change "b" (impact parameter) to see what happens.
Note 90 degrees between outgoing momenta.
Comment in two lines below to change to center of momentum frame,
where the collision looks much simpler.
"""

b = 15e-15  # start with 15e-15, then do 80e-15
projectileproperties = (2,4) # alpha particle
targetproperties = (8,16) # oxygen nucleus
##targetproperties = (2,4) # alpha particle

scene.width = 800
scene.height = 600
scene.x = scene.y = 0
scene.background = color.white
scene.fov = 0.01
scene.range = 200e-15
xstart = scene.range.x

kcoul = 9e9
qe = 1.6e-19
mproton = 1.7e-27
rproton = 1.3e-15
alpha = sphere(pos=(-xstart,b,0), color=color.red)
target = sphere(pos=(0,0,0), color=color.blue)
alpha.mass = projectileproperties[1]*mproton
alpha.radius = (alpha.mass/mproton)**(1./3.)*rproton
alpha.q = projectileproperties[0]*qe
ke = 1e6*qe
alpha.p = vector(sqrt(2.*alpha.mass*ke),0,0)
alpha.trail = curve(color=alpha.color)
target.mass = targetproperties[1]*mproton
target.radius = (target.mass/mproton)**(1./3.)*rproton
target.q = targetproperties[0]*qe
target.p = vector(0,0,0)
target.trail = curve(color=target.color)
dt = 5.*xstart/(mag(alpha.p)/alpha.mass)/1e5
ptot = alpha.p+target.p
vcm = ptot/(alpha.mass+target.mass)

##alpha.p = alpha.p-alpha.mass*vcm
##target.p = target.p-target.mass*vcm

##scene.autoscale = 0

while 1:
    r12 = alpha.pos-target.pos
    F = (kcoul*alpha.q*target.q/mag(r12)**2)*norm(r12)
    alpha.p = alpha.p + F*dt
    target.p = target.p - F*dt
    alpha.pos = alpha.pos + (alpha.p/alpha.mass)*dt
    target.pos = target.pos + (target.p/target.mass)*dt
    alpha.trail.append(pos=alpha.pos)
    target.trail.append(pos=target.pos)

    



