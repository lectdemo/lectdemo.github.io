from visual import *

print """
Ruth Chabay Spring 2001
Electric field around a moving proton.
Click start the motion.
"""

scene.width=scene.height=1000
scene.x = scene.y = 0
scene.forward = (-1,-1,-5)

## proton at rest in lab frame
## moving frame has speed <v,0,0>

c = 3e8
c2 = c**2

v = 0.99*c       ## speed of moving frame

v2=v**2
kel = 9e9
kmag = 1e-7
gamma = 1/sqrt(1-(v2/c2))
print 'gamma = ', gamma
proton = sphere(radius=1e-12, color=color.red)
proton.v = vector(-v,0,0)
proton.q = 1.6e-19

R = 1e-11
escale = R/3e13

    
obsloc = []
dtheta = pi/8.
for theta in arange (0,2*pi, dtheta):
    a=vector(R*cos(theta), R*sin(theta), 0)
    obsloc.append(a)
obsloc2 = []
for theta in arange (dtheta, pi, dtheta):
    a = vector(R*cos(theta), 0, -R*sin(theta))
    obsloc2.append(a)
    b = vector(-R*cos(theta), 0, R*sin(theta))
    obsloc2.append(b)

arr0 = []
arr2 = []
for pt in obsloc:
    r = pt - proton.pos
    E = norm(r)*kel*proton.q/(mag(r)**2)
    Eprime = vector(E.x, gamma*E.y, gamma*E.z)
    aa=arrow(pos=pt, axis=escale*Eprime, color=(1,.5,0), shaftwidth=.8e-12)
    arr0.append(aa)
for pt in obsloc2:
    r = pt - proton.pos
    E = norm(r)*kel*proton.q/(mag(r)**2)
    Eprime = vector(E.x, gamma*E.y, gamma*E.z)
    aa=arrow(pos=pt, axis=escale*Eprime, color=(1,.5,0), shaftwidth=.8e-12)
    arr2.append(aa)
    
scene.autoscale = 0

while 1:
    scene.mouse.getclick()
    for ee in arr2:
        ee.visible = not(ee.visible)
        
