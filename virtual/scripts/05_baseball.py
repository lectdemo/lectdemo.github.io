from visual import *

print """
Bruce Sherwood, Fall 2000
First display is a baseball moving in a vacuum.
Click to see the baseball move through air at sea level.
"""

scene.width=800
scene.height=600
scene.x=scene.y=0
g = 9.8
L = 250.
R = 0.035 # radius of a baseball
C = 0.35 # drag coefficient for a sphere
thick = 1.
density = 1.3 # density of air in kg/m**3
ball = sphere(pos=(10,0,0), radius=20.*R, color=color.white)
ballnoair = sphere(pos=(10,0,0), radius=20.*R, color=color.red)
field = box(pos=(L/2.,-thick/2.,0), size=(L,thick,L/4.), color=color.green)
scene.center = vector(0.45*L,0,0)
scene.forward = -vector(-L/4.,L/4.,L)
ball.m = ballnoair.m = 0.155 # mass of a baseball
v0 = 100.*1600./3600. # 100 mph
theta0 = 45.*2.*pi/360. # 45 degrees
ball.p = ballnoair.p = ball.m*vector(v0*cos(theta0),v0*sin(theta0),0)
ball.trail = curve(color=ball.color, radius=ball.radius)
ballnoair.trail = curve(color=ballnoair.color, radius=ballnoair.radius)
Fgrav = vector(0,-ball.m*g,0)
dt = 0.01

for b in [ballnoair, ball]:
    t = 0.
    while b.y >= 0:
        rate(300)
        if b == ball:
            F = Fgrav-0.5*C*density*pi*R**2*mag(b.p/b.m)*(b.p/b.m)
        else:
            F = Fgrav
        b.p = b.p+F*dt
        b.pos = b.pos+(b.p/b.m)*dt
        b.trail.append(pos=b.pos)
    t = t+dt
    scene.mouse.getclick()
