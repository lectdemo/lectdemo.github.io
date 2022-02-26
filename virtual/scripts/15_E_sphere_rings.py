from __future__ import division
from visual import *
scene.background = color.white
scene.width=1024
scene.height=768
R = 1.0
Q = 5e-7
sp = sphere(color=color.yellow, pos=(0,0,0), radius=R)
N = 30    ##60
A = 4*pi*R**2
k=9e9
obsloc = vector(2*R/3,0,0)
##obsloc = vector(0,0,0)
dEa = arrow(color=color.green, pos=obsloc+vector(0,0.1,0), axis=(0,0,0), shaftwidth=0.03, fixedwidth=1)
Ea = arrow(color=color.orange, pos=obsloc, axis=(0,0,0), shaftwidth=0.05, fixedwidth=1)
dEscale = 1/600
E = vector(0,0,0)
dtheta = pi/N
theta = dtheta/2
scene.autoscale = 0
scene.mouse.getclick()
##sp.visible = 0
sum_dQ = 0
sumN = 0
flag = 0
while theta < pi+dtheta:
##    rate(2)
    x = R*cos(theta)
    ringR = R*sin(theta)
    dQ = Q*(2*pi*ringR)*(R*dtheta)/A
    print 'dQ=', dQ
    sum_dQ += dQ
    if ringR == 0:
        pass
    a = ring(pos=(x,0,0), radius=ringR, thickness = R/(2*N), axis=(1,0,0), color=color.red)
    rr = obsloc-a.pos
    dE = (k*dQ*mag(rr)/((ringR**2+mag(rr)**2)**1.5))*norm(rr)
    E += dE
    print 'z=',mag(rr),'dE=', dE, 'E=', E
    Ea.axis = E*dEscale
    dEa.axis=dE*dEscale
    if not(flag):
        scene.mouse.getclick()
        sp.visible=0
        flag=1
    scene.mouse.getclick()
    theta += dtheta
    sumN += 1
dEa.visible = 0
##Ea = arrow(pos=obsloc, color=color.orange, axis=E*dEscale)
print 'E=', E
print 'sum_dQ=', sum_dQ, 'sumN=', sumN
