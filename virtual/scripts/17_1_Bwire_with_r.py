from visual import *

print """
Ruth Chabay Spring 2001
Magnetic field of a long straight current-carrying wire.
Click to advance dl. After first ring it will run continuously.
magenta arrow: dl, red arrow: r,  cyan arrow: B.
"""

d = display(x=0,y=0,height=800,width=1024,title='magnetic field')
d.background = color.white

I = 5.0
kmag = 1e-7
L = 1.0
dx = L/20.
dl = vector(dx,0,0)
r1 = .05
r2 = .10
Bscale = 3e3
wire = []
for x in arange(-L/2.,L/2.,dx):
    c = cylinder(pos=(x,0,0), axis=dl*0.9, radius=0.005, color=(.7,.7,.7))
    wire.append(c)
    
arr = []
da = L/8.
##for x in arange(-L/2., L/2.+da, da):
for x in arange(-L/2.+2*da, L/2.-da, da):
    for theta in arange(0, 2*pi, pi/4.0):
        b = arrow(pos=(x,r1*cos(theta), r1*sin(theta)), color=(0,1,1),
                       shaftwidth = 0.008, axis=(0,0,0))
        arr.append(b)
## second concentric ring - slows it down
##        b = arrow(pos=(x,r2*cos(theta), r2*sin(theta)), color=(0,1,1),
##                       shaftwidth = 0.004, axis=(0,0,0))
##        arr.append(b)
ra = arrow(pos=(0,0,0), axis=(0,0,0), color=color.red, shaftwidth=0.002)
dla = arrow(pos=(0,0,0), axis=(0,0,0), color=color.magenta, shaftwidth=0.02)
dl_label = label(pos=dla.pos, text="dl", yoffset = 5, xoffset = 3,
                 color=dla.color, opacity=0, box=0)
r_label = label(pos = ra.pos + ra.axis/2., color=ra.color, text = "r",
                yoffset = 5, xoffset = 5, opacity=0, box=0)

count = 0
ratevar = 5
for a in arr:
    for s in wire:
        rate(ratevar)
        r = a.pos - (s.pos+dl/2.)
        ra.pos = (s.pos+dl/2.)
        ra.axis = r
        r_label.pos = ra.pos + ra.axis/2.
        dla.pos = s.pos+vector(0,0.011,0)
        dla.axis = dl
        dl_label.pos = dla.pos
        a.axis = a.axis +Bscale*kmag*I*cross(dl, norm(r))/mag(r)**2
        if count < 2:
            d.mouse.getclick()
    count = count+1
    if count > 8:
        ratevar = 50

##Iv = arrow(pos=(L/2.,0,0), axis=dl, color=(1,0,0))
ra.visible = 0
dla.visible=0
r_label.visible = 0
dl_label.visible = 0
