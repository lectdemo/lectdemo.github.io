from visual import *

print """
Ruth Chabay Spring 2001/F 2004
Magnetic field of a current-carrying loop.
Step-by-step; shows dB for each segment.
Click to advance.
First location: click for each segment.
After this: click for each obs. location.
"""

scene.width = 1024
scene.height=768
scene.x = scene.y = 0
scene.background = color.white

def axes(a=10, as=0):
    axes=curve(pos=[(-a,0,0),(a,0,0),(0,0,0),(0,-a,0),(0,a,0),(0,0,0),
                    (0,0,-a),(0,0,a)], color=color.black)
##    scene.autoscale = as
##    xlabel=label(pos=(a,0,0), xoffset=10, text="x", box=0,
##                 opacity=0,color=color.black)
##    ylabel=label(pos=(0,a,0), yoffset=10, text="y", box=0,
##                 opacity=0,color=color.black)
##    zlabel=label(pos=(0,0,a), xoffset=10, text="z", box=0,
##                 opacity=0,color=color.black)
axes(0.1)

I = 1.0
kmag = 1e-7
bscale = 2e5

R = 0.02        ##0.03
loop = ring(pos=(0,0,0), axis=(1,0,0), radius=R, thickness=0.002)

locations = []
locations2 = []
obs1 = []
obs2 = []
dtheta = pi/6.
phi = pi/4.
Ro = 5*R
for theta in arange(0, pi+dtheta, dtheta):
    x = Ro*cos(theta)
    y = Ro*sin(theta)
    z = 0
    aa = (x,y,z)
    if aa not in locations:
        locations.append(aa)
    aa = (x,-y,z)
    if aa not in locations and theta != pi:
        locations.append(aa)
##    aa = (x,z,y)
##    if aa not in locations:
##        locations.append(aa)
##    aa = (x,z,-y)
##    if aa not in locations:
##        locations.append(aa)
##    a = vector(x,y,z)
##    b = rotate(a,angle=phi, axis=(1,0,0))
##    locations2.append((b.x, b.y, b.z))
##    locations2.append((b.x,-b.y, -b.z))
##    c = rotate(a, angle=3*phi, axis=(1,0,0))
##    locations2.append((c.x,c.y,c.z))
##    locations2.append((c.x,-c.y, -c.z))
##
for point in locations:
    obs1.append(arrow(pos=point, axis=(0,0,0), color=color.cyan,
                      shaftwidth=0.004))
for point in locations2:
    obs2.append(arrow(pos=point, axis=(0,0,0), color=color.cyan,
                    shaftwidth=0.004))

dtheta = pi/10.

dlarrow = arrow(pos=(0,0,0), axis=(0,0,0), color=color.magenta,
                shaftwidth=0.01)
rarrow = arrow(pos=(0,0,0), axis=(0,0,0), color=color.red,
               shaftwidth=0.002,fixedwidth=1)

dbarrow=arrow(pos=(0,0,0), axis=(0,0,0), color=color.cyan,
               shaftwidth=0.002,fixedwidth=1)

a = sphere(pos=(obs1[0].pos), radius=.0001)
##scene.autoscale = 0
##for barrow in obs1+obs2:
count = 0
ratevar = 10
for barrow in obs1:
    dBlist =[]
    barrow.visible=0
    B = vector(0,0,0)
    count1=0
    for theta in arange(0,2*pi,dtheta):
        rate(ratevar)
        a = vector(0,R*cos(theta), R*sin(theta))
        b = vector(0,R*cos(theta+dtheta), R*sin(theta+dtheta))
        dl = b-a
        dlarrow.pos=a*1.2
        dlarrow.axis=dl
        r = barrow.pos - dlarrow.pos
        rarrow.pos=dlarrow.pos
        rarrow.axis=r
##
        if count1 < 1:
            scene.mouse.getclick()
            count1 = 1
##        
        dB = kmag*I*cross(dl,norm(r))/mag(r)**2
        dBarrow = arrow(pos=barrow.pos, axis=dB*bscale, shaftwidth=0.001, fixedwidth=1, color=color.cyan)
        dBlist.append(dBarrow)
        B = B+dB
        barrow.axis = B*bscale
        if count > 0:
            scene.autoscale = 0
        if count < 1:
            scene.mouse.getclick()
    count = count + 1
    if count > 3:
        ratevar = 30
    scene.mouse.getclick()
    for bb in dBlist:
        bb.visible=0
    dBlist=[]
    barrow.visible=1
    scene.mouse.getclick()
dlarrow.visible = 0
rarrow.visible = 0

##    print mag(barrow.axis)

##while 1:
##    scene.mouse.getclick()
##    for barrow in obs2:
##        barrow.visible = not(barrow.visible)

