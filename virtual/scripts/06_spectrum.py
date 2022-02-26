from __future__ import division
from visual import *


# Spectrum, by Bruce Sherwood, NCSU, March 2004

print """
Click to sequence through various spectrum situations.
"""

scene.x = scene.y = 0
scene.width = 1000
scene.height = 768
scene.range = .5
scene.center = (0,-0.2,0)
scene.forward = (.1,-.5,-1)
scene.background = (0.7,0.7,0.7)
scene.lights = [(0,0,0.5), (0.5,0,0), (-0.5,0,0), (0,1,0)]
grayness = 0.5
gray = (grayness,grayness,grayness)
d = 0.05
L = 0.6
N = 50 # max number of lines shown
zblue = 0.6*d
zlong = 1.8*d
wslit = zlong/N
wslitadjust = 1*wslit
hslit = 0.8*d
dy = 0.1*d
ray = norm(vector(1,0,2))
apparatus = frame(pos=(-.3,0,-.2), axis=ray)
container = box(frame=apparatus, size=(8*d,d,d), color=gray)
slit = box(frame=apparatus, pos=(4*d,0,0), size=(0.3*d,hslit,wslit), color=gray)
box(frame=apparatus, pos=container.pos+container.axis/2+vector(L,hslit/2+dy/2,0),
           size=(0.01*d,dy,2*zblue+2*(N-1)*wslit+wslit+2*dy), color=gray)
box(frame=apparatus, pos=container.pos+container.axis/2+vector(L,-hslit/2-dy/2,0),
           size=(0.01*d,dy,2*zblue+2*(N-1)*wslit+wslit+2*dy), color=gray)
box(frame=apparatus, pos=container.pos+container.axis/2+vector(L,0,zblue+(N-1)*wslit+wslit/2+dy/2),
           size=(0.01*d,hslit,dy), color=gray)
box(frame=apparatus, pos=container.pos+container.axis/2+vector(L,0,-zblue-(N-1)*wslit-wslit/2-dy/2),
           size=(0.01*d,hslit,dy), color=gray)
box(frame=apparatus, pos=container.pos+container.axis/2+vector(L,0,(zblue+wslit/2)/2),
           size=(0.01*d,hslit,(zblue-wslit/2)), color=gray)
box(frame=apparatus, pos=container.pos+container.axis/2+vector(L,0,(-zblue-wslit/2)/2),
           size=(0.01*d,hslit,(zblue-wslit/2)), color=gray)
center = box(frame=apparatus, pos=slit.pos+vector(L,0,0),
           size=(0.015*d,hslit,wslit), color=gray)

grating = frame(frame=apparatus, pos=slit.pos+vector(L/2,0,0))
gobjects = []
w = 0.05*d
gobjects.append(box(frame=grating, pos=(0,0,-d), size=(0.01*d,2.1*d,0.1*d),
              color=gray, visible=0))
gobjects.append(box(frame=grating, pos=(0,0,d), size=(0.01*d,2.1*d,0.1*d),
           color=gray, visible=0))
gobjects.append(box(frame=grating, pos=(0,d,0), size=(0.01*d,0.1*d,2*d,),
             color=gray, visible=0))
gobjects.append(box(frame=grating, pos=(0,-d,0), size=(0.01*d,0.1*d,2*d),
            color=gray, visible=0))
for z in arange(-d+0.05*d+w, d-0.05*d, w):
    gobjects.append(cylinder(frame=grating, pos=(0,-d,z), axis=(0,2*d,0),
                     radius=0.01*d, color=gray, visible=0))
gobjects.append(label(frame=grating, pos=(0,1.2*d,-1.8*d), text='Diffraction Grating',
               visible=0))

sourcetitle = label(frame=apparatus, pos=container.pos+vector(-container.length/2,container.height,0),
      text='White Light Source')
leftspectrum = label(frame=apparatus, pos=center.pos+vector(0,-1.1*hslit,1.5*d),
                     text='Spectrum', visible=0)
rightspectrum = label(frame=apparatus, pos=center.pos+vector(0,-1.1*hslit,-1.5*d),
                     text='Spectrum', visible=0)

left = []
right = []
leftray = []
rightray = []
white = []
for nn in range(N):
    left.append(box(frame=apparatus, pos=center.pos+vector(0,0,zblue+nn*wslit),
                    size=(0.01*d,hslit,wslitadjust), color=gray))
    leftray.append(box(frame=apparatus, pos=(grating.pos+left[-1].pos)/2,
                    size=(mag(left[-1].pos-grating.pos),hslit,wslit), color=gray, visible=0))
    leftray[-1].axis = left[-1].pos-grating.pos
    right.append(box(frame=apparatus, pos=center.pos+vector(0,0,-zblue-nn*wslit),
                    size=(0.01*d,hslit,wslitadjust), color=gray))
    rightray.append(box(frame=apparatus, pos=(grating.pos+right[-1].pos)/2,
                    size=(mag(right[-1].pos-grating.pos),hslit,wslit), color=gray, visible=0))
    rightray[-1].axis = right[-1].pos-grating.pos
    white.append(color.hsv_to_rgb(((nn/N)*(5/6),1,1)))

beam1 = box(frame=apparatus, pos=(slit.pos+center.pos)/2,
            size=(center.x-slit.x,hslit,wslit), color=color.white, visible=0)

absorber = box(frame=apparatus, pos=container.pos+container.axis/2+vector(L/5,0,0),
               size=(0.2*d,1.4*hslit,1.4*hslit), color=(0.4,0.4,0.4), visible=0)
absorbertitle = label(frame=apparatus, pos=absorber.pos+vector(0,-0.9*hslit,1.1*hslit),
                      text='Absorber', visible=0)

def gratingvisible(visible):
    for obj in gobjects:
        obj.visible = visible

def showspectrum(colorlist, absorb=0):
    raycolor = vector(0,0,0)
    nlines = 0
    if absorb:
        showspectrum(white, absorb=0)
    else:
        for nn in range(N):
            left[nn].color = gray
            right[nn].color = gray
            leftray[nn].visible = 0
            rightray[nn].visible = 0
    if colorlist is off:
        slit.color = center.color = gray
        beam1.visible = 0
        return
    beam1.visible = 1
    for col in colorlist:
        hsv = color.rgb_to_hsv(col)
        hue = hsv[0]
        nindex = int(N*(1-1.2*hue)+0.5)
        if nindex >= N:
            nindex = N-1
        setcol = col
        if absorb:
            setcol = color.hsv_to_rgb((hue,hsv[1],0.5*hsv[2]))
        left[nindex].color = setcol
        right[nindex].color = setcol
        leftray[nindex].color = setcol
        leftray[nindex].visible = 1
        rightray[nindex].color = setcol
        rightray[nindex].visible = 1
        nindex += 1
        if col != (0,0,0):
            raycolor += vector(col)
            nlines += 1
    raycolor /= nlines
    hsv = color.rgb_to_hsv(raycolor)
    if nlines > 1:
        hsv = (hsv[0], hsv[1], 1)
    if colorlist is white or absorb:
        hsv = (0,0,1)
    beam1.color = slit.color = center.color = color.hsv_to_rgb(hsv)

off = [gray]
gas1 = [color.green, (1,0.3,0)]
gas2 = [color.yellow, color.cyan]

while 1:
    gratingvisible(0)
    leftspectrum.visible = rightspectrum.visible = 0
    sourcetitle.text = 'Light Source Off'
    showspectrum(off)
    scene.mouse.getclick()
    sourcetitle.text = 'White Light Source'
    beam1.color = slit.color = center.color = color.white
    beam1.visible = 1
    scene.mouse.getclick()
    gratingvisible(1)
    leftspectrum.visible = rightspectrum.visible = 1
    showspectrum(white)
    scene.mouse.getclick()
    sourcetitle.text = 'Electron-excited Gas'
    showspectrum(gas1)
    scene.mouse.getclick()
    sourcetitle.text = 'White Light Source'
    showspectrum(white)
    scene.mouse.getclick()
    absorber.visible = absorbertitle.visible = 1
    showspectrum(gas2, absorb=1)
    scene.mouse.getclick()
    absorber.visible = absorbertitle.visible = 0
