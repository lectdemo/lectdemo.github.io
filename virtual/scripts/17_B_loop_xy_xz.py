from visual import *

#scene.stereo="redcyan"
print """
Ruth Chabay Spring 2001
Magnetic field of a current-carrying loop.
"""

scene.width = scene.height = 600
scene.x = scene.y = 0
scene.background = color.white

def axes(a=10):
    axes=curve(pos=[(-a,0,0),(a,0,0),(0,0,0),(0,-a,0),(0,a,0),(0,0,0),
                    (0,0,-a),(0,0,a)], color=(0.7,0.7,0.7))
    scene.autoscale = 0

I = 1.0
kmag = 1e-7
bscale = 1e5

R = 0.01        ##0.03
loop = ring(pos=(0,0,0), axis=(1,0,0), radius=R, thickness=0.001)
axes(a = 0.1)

locations = []
locations2 = []
obs1 = []
obs2 = []
dtheta = pi/6.
phi = pi/4.
Ro = 6*R
for theta in arange(0, pi+dtheta, dtheta):
    x = Ro*cos(theta)
    y = Ro*sin(theta)
    z = 0
    locations2.append((x,y,z))
    locations2.append((x,-y,z))
    locations.append((x,z,y))
    locations.append((x,z,-y))
    a = vector(x,y,z)
    b = rotate(a,angle=phi, axis=(1,0,0))
##    locations2.append((b.x, b.y, b.z))
##    locations2.append((b.x,-b.y, -b.z))
    c = rotate(a, angle=3*phi, axis=(1,0,0))
##    locations2.append((c.x,c.y,c.z))
##    locations2.append((c.x,-c.y, -c.z))

for point in locations:
    obs1.append(arrow(pos=point, axis=(0,0,0), color=color.cyan,
                      shaftwidth=0.003))
for point in locations2:
    obs2.append(arrow(pos=point, axis=(0,0,0), color=color.cyan,
                shaftwidth=0.01))

dtheta = pi/10.

dlarrow = arrow(pos=(0,0,0), axis=(0,0,0), color=color.red,
                shaftwidth=0.01)
rarrow = arrow(pos=(0,0,0), axis=(0,0,0), color=color.green,
               shaftwidth=0.005)

for barrow in obs1+obs2:
##for barrow in obs1:
    B = vector(0,0,0)
    for theta in arange(0,2*pi,dtheta):
        a = vector(0,R*cos(theta), R*sin(theta))
        b = vector(0,R*cos(theta+dtheta), R*sin(theta+dtheta))
        dl = b-a
##        dlarrow.pos=a
##        dlarrow.axis=dl
        r = barrow.pos - a
##        rarrow.pos=dlarrow.pos
##        rarrow.axis=r
        dB = kmag*I*cross(dl,norm(r))/mag(r)**2
        B = B+dB
##        scene.mouse.getclick()
    barrow.axis = B*bscale
##    print mag(barrow.axis)

while 1:
    scene.mouse.getclick()
    for barrow in obs2:
        barrow.visible = not(barrow.visible)
