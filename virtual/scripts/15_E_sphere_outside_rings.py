from __future__ import division
from visual import *
scene.background = color.white
scene.width=1024
scene.height=768
scene.center = (0,0,0)
R = 1.0
Q = 5e-7
k=9e9

sp = sphere(color=color.yellow, pos=(0,0,0), radius=R)
obsloc = vector(2*R,0,0)
N = 30
A = 4*pi*R**2
dEscale = 1/500
dEa = arrow(color=color.green, pos=obsloc+vector(0,0.2,0), axis=(0,0,0), shaftwidth=0.1, fixedwidth=1)
Ea = arrow(color=color.orange, pos=obsloc, axis=(0,0,0), shaftwidth=0.1, fixedwidth=1)
E = vector(0,0,0)
dtheta = pi/N
theta = dtheta/2
sum_dQ = 0
scene.mouse.getclick()

while theta < pi:
    rate(2)
    x = R*cos(theta)
    ringR = R*sin(theta)
    if ringR == 0:
        pass
    a = ring(pos=(x,0,0), radius=ringR, thickness = R/(2*N), axis=(1,0,0), color=color.red)
    rr = obsloc-a.pos
    dQ = Q*(2*pi*ringR)*(R*dtheta)/A
    print 'dQ=', dQ
    sum_dQ += dQ
    dE = (k*dQ*mag(rr)/((ringR**2+mag(rr)**2)**1.5))*norm(rr)
    print dE
    E += dE
    dEa.axis=dE*dEscale
    Ea.axis = E*dEscale
##    scene.mouse.getclick()
    theta += dtheta
dEa.visible = 0
scene.mouse.getclick()
##Ea = arrow(pos=obsloc, color=color.orange, shaftwidth=0.3, axis=E*dEscale)
print 'Enet=', E
print 'sum_dQ=', sum_dQ

ptoffset = 5
pt = sphere(color=color.red, pos=(0,ptoffset,0), radius=R/10)
ptobsloc = vector(2*R,ptoffset,0)
Ept = k*Q*norm(ptobsloc-pt.pos)/mag(ptobsloc-pt.pos)**2
Epta = arrow(pos=ptobsloc, axis=Ept*dEscale, color=color.orange, shaftwidth=0.1, fixedwidth=1)
print 'Ept=', Ept


    
####constant dx
##dx= 0.05*R
##x = 0.999*R
##while x > -1.1*R:
##    print 'x=',x,'x/R=',x/R
##    if (x/R) < -1.0:
##        theta = pi
##    elif (x/R) == 0:
##        theta = 0.002
##    else:
##        theta = acos(x/R)
##    ringR = R*sin(theta)
##    print 'theta=', theta, 'ringR=',ringR
##    a = ring(pos=(x,0,0), radius=1.1*ringR, axis=(1,0,0),
##             thickness=dx/2, color=color.blue)
##    scene.mouse.getclick()
##    x = x-dx
