from visual import *
scene.background = color.white

print """
Ruth Chabay Spring 2001
Electric field of a uniformly charged disk.
"""

scene.height = 1000
scene.width = 1000
scene.x = scene.y = 0

w = 0.2
R = w*50.
d = cylinder(pos=(0,0,-w/2), radius=R, axis=(0,0,w), color=color.red)
Q = 1e-7
kel = 9e9
Escale = .1
r = 0.9*R
N = 60.
dtheta = 2.*pi/N
arc = r*dtheta
dr = arc    ##0.15*R
sources = []
for r in arange(1.*R, 0.01*R, -dr):
    N = 2.*pi*r/arc
    dtheta = 2*pi/N
##    print 'r=',r, 'N=',N, 'arc=', arc, 'circumf = ', 2*pi*r
    for theta in arange(0,2*pi-dtheta/2.,dtheta):
        p = sphere(pos=(r*cos(theta), r*sin(theta), w/2), radius=0.2,
                   color=color.blue)
        sources.append(p)
nq = len(sources)
for q in sources:
    q.charge = Q/float(nq)

dx = R/10.
for x in arange(-1.1*R, 1.1*R+dr, dx):
    obsloc = vector(x,0,5.*w)
    E = vector(0,0,0)
    for q in sources:
        r = obsloc - q.pos
        E = E + kel*norm(r)*q.charge/mag(r)**2
    arrow(pos=obsloc, color=(1,.5,0), axis=Escale*E, shaftwidth=0.4)
        
