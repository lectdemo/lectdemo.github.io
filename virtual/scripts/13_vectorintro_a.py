from visual import *
scene.width = 1024
scene.height = 768
scene.background = color.white

print """
Change axis of arrow to display a different vector
"""

of = 5
d = 5
r = 0.06
sw = 0.2
scene.range = 1.2*d
scene.forward = (-0.1,-0.2,-1)  ## position camera
## draw and label axes
xaxis=cylinder(pos=(0,0,0), axis=(d,0,0), radius=r, color=color.red)
label(pos=xaxis.pos+xaxis.axis, text='x', color=xaxis.color, opacity=0,
      linecolor=xaxis.color, xoffset= of, height=24)
yaxis=cylinder(pos=(0,0,0), axis=(0,d,0), radius=r, color=(0,1,.3))
label(pos=yaxis.pos+yaxis.axis, text='y', color=yaxis.color, opacity=0,
      linecolor=yaxis.color, xoffset= of, height=24)
zaxis=cylinder(pos=(0,0,0), axis=(0,0,d), radius=r, color=(.4,.4,1))
label(pos=zaxis.pos+zaxis.axis, text='z', color=zaxis.color, opacity=0,
      linecolor=zaxis.color, xoffset= of, height=24)


# sample visualizations of vectors in 3D (could create on the fly):
arrow(pos=(0,0,0), axis=(-2,1.5,3), color=color.cyan, shaftwidth = sw)
##arrow(pos=(0,0,0), axis=(2,1.5,3), color=color.yellow, shaftwidth = sw)
arrow (pos=(0,0,0), axis=vector(3,-6,2), color=color.yellow, shaftwidth = sw)





