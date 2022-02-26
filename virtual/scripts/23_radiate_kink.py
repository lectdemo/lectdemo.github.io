from __future__ import division
from visual import *
scene.width = scene.height = 1000
max = 15*0.5
scene.range = max
scene.autoscale = 0
scene.background = color.white

print """
Click to start animation. While running, click to pause, click to resume.
After completed, click to restart.
"""

start = sphere(pos=(0,0,0), radius=0.1, color=(1,.5,.5))
proton = sphere(pos=(0,0,0),radius=0.1, color=color.red)
rad = 0.5
lines = []
for theta in arange(0,2*pi,pi/8):
    a=curve(pos=[(0,0,0),(.5*max*cos(theta),.5*max*sin(theta),0),(1*max*cos(theta),1*max*sin(theta),0),
                 (2*max*cos(theta),2*max*sin(theta),0)],
                 color=(1,.5,0),radius=0.03)
    lines.append(a)
dt = 0.01
vmag = 0.01
v = vector(0,-vmag,0)
c = 10*vmag
a = rad/2   ## mag of acceleration (arbitrary, to get visible kinks)
ahat = vector(0,-1,0)
while 1:
    scene.mouse.getclick()
    t=0
    proton.pos = vector(0,0,0)
    while c*t < max:
        proton.pos = proton.pos + v*dt
        for fl in lines:
            fl.pos[0]=proton.pos     ## beginning of line tracks proton
            r = fl.pos[3]-vector(0,0,0)  ## from origin to end of line
            rhat = norm(r)
            fl.pos[2]=rhat*c*t    ## end of the kink
            zvector = -cross(rhat, ahat) # +z if rhs, -z if lhs
            rhatperp = norm(cross(rhat,zvector)) ## vector perp to r and zhat           
            magaperp = mag(cross(rhat,norm(proton.pos))) ## sin theta
            b = rhatperp*magaperp*a
            fl.pos[1] = fl.pos[2]+b        
        t = t+dt
        if scene.mouse.clicked:
            scene.mouse.getclick()
            while not(scene.mouse.clicked):
                rate(20)
                pass
            scene.mouse.getclick()
    
