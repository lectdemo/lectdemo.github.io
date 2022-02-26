from visual import *

print """
Ruth Chabay Spring 2001
Magnetic field around a moving proton.
Change v in the program.
"""
scene.background = color.white
scene.stereo="redcyan"
scene.width=scene.height=1000
scene.x = scene.y = 0
scene.forward = (-1,0,-5)

## proton at rest in lab frame
## moving frame has speed <v,0,0>

c = 3e8
c2 = c**2

v = 0.9*c       ## speed of moving frame


v2=v**2
kel = 9e9
kmag = 1e-7
gamma = 1/sqrt(1-(v2/c2))
print 'gamma = ', gamma
proton = sphere(radius=1e-12, color=color.red)
proton.v = vector(-v,0,0)
proton.q = 1.6e-19

R = 1e-11
##escale = R/3e13
bscale = R/99000

    
obsloc = []
dtheta = pi/4.
dx = 2*R
for x in arange(-dx,2*dx, dx):
##for x in arange(0,R,R):
    for theta in arange (0,2*pi, dtheta):
        a=vector(x, R*sin(theta), R*cos(theta))
        obsloc.append(a)
        
arr0 = []
for pt in obsloc:
    r = pt - proton.pos
    E = norm(r)*kel*proton.q/(mag(r)**2)
    Bprime = vector(0, gamma*(v/c2)*E.z, -gamma*(v/c2)*E.y)
##    print mag(Bprime)
    aa=arrow(pos=pt, axis=bscale*Bprime, color= color.cyan, shaftwidth=.8e-12)
    arr0.append(aa)
    
scene.autoscale = 0

