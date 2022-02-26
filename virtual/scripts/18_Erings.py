from __future__ import division
from visual import *
scene.width = 1024
scene.height = 768
scene.background = color.white

oof = 9e9
sf = 2e-11
L = 6e-3
dL = 1e-3
##color.orange = (1,.7,0)

redcolor = color.rgb_to_hsv((1,0,0))
print redcolor

def qring(rradius=10, nptcharges=20, totalq=1e-9, xx=0):
    thisring = []
    dtheta = 2*pi/nptcharges
    for theta in arange(0,2*pi,dtheta):
        aa =sphere(pos=(xx,rradius*sin(theta),rradius*cos(theta)), radius=rradius/15)
        aa.q = totalq/nptcharges
##        sat = 1.5*abs(totalq)/(4.5e-9)
        sat = 1.5*abs(totalq)/(1e-8)
        if totalq > 1e-15:
            hue = 0.0
        elif totalq < 0:
            hue = (240/360)
        elif totalq == 0:
            sat = 0
        aa.color = color.hsv_to_rgb((hue,sat,1.0))
        thisring.append(aa)
        ring(pos=(xx,0,0), axis=(1,0,0), radius=rradius, thickness=rradius/75., color=aa.color)
    return thisring
rings =[]
ring_radius = 2e-3
dQ = 5e-10
##print 'dQ=',dQ
Q = -3*dQ       ## charge of leftmost ring
count = 0
vis = 1
##for x in arange (-L,1.1*L,dL):
for x in arange(-2*L,2.5*L,dL):
    rings.append(qring(rradius=ring_radius,nptcharges=20,totalq=Q,xx=x))
    print 'charge of ring #',count,"=",Q
    Q = Q +dQ
    count += 1
print 'len(rings)=',len(rings)
print "Click to see electric field"
scene.mouse.getclick()
for rr in rings:
    for pt in rr:
        pt.visible = not(pt.visible)
for x in arange((-L+dL),L-dL,dL/2):
##    print 'x=',x
    for y in arange(-(2/3)*ring_radius,ring_radius,ring_radius/3.):
        loc = vector(x,y,0)
        E = vector(0,0,0)
        for rng in rings:
##            print rings.index(rng)
            for ptq in rng:
                r = loc - ptq.pos
                E = E + (oof*ptq.q/mag(r)**2)*norm(r)
##                print E, mag(E)
        arrow(pos= loc, axis=E*sf, color=color.orange, shaftwidth=ring_radius/20) 

while 1:
    scene.mouse.getclick()
    for rr in rings:
        for pt in rr:
            pt.visible = not(pt.visible)
            
        
