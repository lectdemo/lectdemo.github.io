from visual import *

print """
Bruce Sherwood Fall 2000
An alpha particle scatters a free electron.
This shows that as the alpha particle enters an atom,
the electrons are scattered away, and the alpha particle
essentially interacts with a bare nucleus.
Note that this is a case of a large mass colliding with
a stationary small mass, and the small mass acquires about
twice the speed of the large mass.
After a very long time, you see that with these initial
conditions the two particles are orbiting each other!
"""

scene.width = 800
scene.height = 600
scene.x = scene.y = 0
scene.background = color.white

kcoul = 9e9
qe = 1.6e-19
xstart = 2e-14
alpha = sphere(pos=(-xstart,0,0), radius=1e-15, color=color.red)
target = sphere(pos=(+xstart,-15e-15,0), radius=0.4e-15, color=color.blue)
scene.autoscale = 0
alpha.mass = 4.*1.7e-27
alpha.q = 2.*qe
ke = 1e8*qe
alpha.p = vector(sqrt(2.*alpha.mass*ke),0,0)
alpha.trail = curve(color=alpha.color)
target.mass = 9e-31
target.q = -qe
target.p = vector(0,0,0)
target.trail = curve(color=target.color)
dt = xstart/(mag(alpha.p)/alpha.mass)/1e3

while 1:
    rate(200)
    r12 = alpha.pos-target.pos
    F = (kcoul*alpha.q*target.q/mag(r12)**2)*norm(r12)
    alpha.p = alpha.p + F*dt
    target.p = target.p - F*dt
    alpha.pos = alpha.pos + (alpha.p/alpha.mass)*dt
    target.pos = target.pos + (target.p/target.mass)*dt
    alpha.trail.append(pos=alpha.pos)
    target.trail.append(pos=target.pos)
    



