from visual import *
# demonstration of vector cross product

print """
Vector cross product. Magnitude represented by grey parallelogram.
Direction represented by (optional) yellow vector whose direction
is given by a right-hand rule: Red cross Green = Yellow.
Drag to change green vector.
Click to show the yellow vector perpendicular to grey area.
Click to toggle fixed angle or fixed length.
"""

scene.background = color.white
scene.title="Vector Cross Product"
scene.width=600
scene.height=600
scene.ambient = .5
scene.forward = (-1,-.2,-.1)

R = 0.15*4
plane = curve(pos=[(0, -10, -10), (0, -10, 10), (0, 10,10), (0, 10, -10),
              (0, -10, -10), (0,-6,-10), (0,-6,10), (0, -2, 10), (0, -2, -10),
              (0,2,-10), (0,2,10), (0,6,10), (0,6,-10),(0,10, -10),              
              (0,10,-6), (0,-10,-6), (0,-10,-2), (0,10,-2), (0,10,2),
              (0,-10,2), (0,-10,6), (0,10,6)], color=color.black)

s_theta=sphere(pos=(0,-12,-10), radius=0.6, color=(0.6, 1.0, 0.6))
s_theta_label=label(pos=s_theta.pos, text="Fix Angle", yoffset=-5,
                    opacity=0, box=0, line=0, color=color.black)
s_length=sphere(pos=(0,-12,10), radius=0.6, color=(0.6, 0.6, 1.0))
s_length_label=label(pos=s_length.pos, text="Fix Length", yoffset=-5,
                    opacity=0, box=0, line=0, color=color.black)
s_showvector=sphere(pos=(0,-12,0), radius=0.6, color=(0.6, 1.0, 0.6))
s_showvector_label=label(pos=s_showvector.pos, text="Show Vector", yoffset=-5,
                    opacity=0, box=0, line=0, color=color.black)

s_text=label(pos=(0,12,0), text="Yellow = Red x Green",
                    opacity=0, box=0, line=0, color=color.black)
               
fixlength = 0
fixtheta = 0

avector = vector (0,0,-3.5)
bvector = vector (0,5,-3)

a = arrow(pos=(0,0,0), axis=avector, shaftwidth=R, color=color.red)
b = arrow(pos=a.pos+a.axis, axis=bvector, shaftwidth=R, color=color.green)

cvector = cross(avector,bvector)
c = arrow(pos=(0,0,0), axis=cvector, shaftwidth=R, color=color.yellow, visible=0)

org = vector(0,0,0)
zaxis = vector(0,0,1)

area = faces(pos=[org,org,org,org,org,org,org,org,org,org,org,org],
             normal=[zaxis,zaxis,zaxis,zaxis,zaxis,zaxis,
                     -zaxis,-zaxis,-zaxis,-zaxis,-zaxis,-zaxis], color=(0.5,0.5,0.5))

def setarea():
    area.pos = [(0,0,0), avector, bvector, avector, avector+bvector, bvector,
                      (0,0,0), bvector, avector, bvector, avector+bvector, avector]

setarea()
scene.autoscale = 0

drag = 0

while 1:
    if scene.mouse.events:
        m = scene.mouse.getevent()
        if m.drag:
            drag = 1
            obs = None
        elif m.drop:
            drag = 0
        elif m.click:
            if m.pick is s_length:
                if fixtheta:
                    fixtheta = not(fixtheta)
                    s_theta.color = (0.6, 1.0, 0.6)
                fixlength=not(fixlength)
                if fixlength:
                    s_length.color=(0.0, 0.0, 1.0)
                else:
                    s_length.color=(0.6, 0.6, 1.0)
            elif m.pick is s_theta:
                if fixlength:
                    fixlength = not(fixlength)
                    s_length.color=(0.6, 0.6, 1.0)
                fixtheta = not(fixtheta)
                if fixtheta:
                    s_theta.color=(0.0, 1.0, 0.0)
                else:
                    s_theta.color = (0.6, 1.0, 0.6)
            elif m.pick is s_showvector:
                c.visible = not(c.visible)
                if c.visible:
                    s_showvector.color=(0.0, 1.0, 0.0)
                    s_showvector_label='Hide Vector'
                else:
                    s_showvector.color = (0.6, 1.0, 0.6)
                    s_showvector_label='Show Vector'
    if drag:
        newobs=scene.mouse.project(normal=(1,0,0), d=0)
        if newobs and (newobs != obs):
            obs = newobs
            if not fixlength and not fixtheta:
                bvector = obs-(a.pos+a.axis)
                if bvector.mag > 20: bvector=bvector*(20/bvector.mag)
                b.axis=bvector
            elif fixlength:
                length=6
                bvector = length*norm(obs-(a.pos+a.axis))
                b.axis=bvector
            elif fixtheta:
                length=mag(obs-(a.pos+a.axis))
                bvector=length*norm(vector(0, 3, 1))
                b.axis=bvector

            cvector=cross(avector,b.axis)
            c.axis=cvector
            setarea()

