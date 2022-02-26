from visual import *

##Bruce Sherwood Fall 2000; major revision Fall 2002.
##March 2004: Change colors for better display with computer projector.

print """
Motion in a potential energy well.
Drag from left to right to create a potential energy well.
Click to specify the energy level.
Click again to choose a different energy level.
Click "New well" in lower right corner to start over.
Moving red indicator represents separation r.
Cyan arrow represents momentum.
Magenta line represents kinetic energy.
"""

class button:
    def __init__(self, pos=[(0,0,0),(1,1,0.1)], text='', visible=0):
        x1 = pos[0][0]
        y1 = pos[0][1]
        x2 = pos[1][0]
        y2 = pos[1][1]
        self.box = box(pos=(0.5*(x1+x2),0.5*(y1+y2),0), size=(x2-x1,y2-y1,0.1),
                       color=color.white, visible=visible)
        self.text = label(pos=self.box.pos, text=text, visible=visible,
                          color=color.black, opacity=0)
        
    def setvisible(self, visible=1):
        self.box.visible = visible
        self.text.visible = visible

def update(deltat):
    global nslope
    oldnslope = nslope
    xleft = slopes[nslope].xleft
    xright = slopes[nslope].xright
    Fx = -slopes[nslope].axis.y/slopes[nslope].axis.x
    oldx = bead.x
    oldv = bead.p.x/bead.m
    # Need to determine dtleft (when would reach left edge of slope, if at all)
    #   and dtright (when would reach right edge of slope, if at all)
    acc = Fx/bead.m
    dts = [deltat]
    if acc == 0:
        if oldv < 0:
            dtleft = (xleft-oldx)/oldv
            if dtleft > 0:
                dts.append(dtleft)
        if oldv > 0:
            dtright = (xright-oldx)/oldv
            if dtright > 0:
                dts.append(dtright)
    else:
        if oldx != xleft: # determine time when would reach left end of this slope
            vleftsq = oldv**2+2.*acc*(xleft-oldx)
            if vleftsq >= 0:
                vleft = sqrt(vleftsq)
                dtleft = (vleft-oldv)/acc
                if dtleft > 0:
                    dts.append(dtleft)
                dtleft = (-vleft-oldv)/acc
                if dtleft > 0:
                    dts.append(dtleft)
        if oldx != xright: # determine time when would reach right end of this slope
            vrightsq = oldv**2+2.*acc*(xright-oldx)
            if vrightsq >= 0:
                vright = sqrt(vrightsq)
                dtright = (vright-oldv)/acc
                if dtright > 0:
                    dts.append(dtright)
                dtright = (-vright-oldv)/acc
                if dtright > 0:
                    dts.append(dtright)
    dt = min(dts)
    
    bead.p = bead.p+vector(Fx,0,0)*dt
    newv = bead.p.x/bead.m
    bead.x = bead.x+0.5*(oldv+newv)*dt
    if dt < deltat:
        if bead.x > slopes[nslope].x:
            bead.x = xright
        else:
            bead.x = xleft
    ypotential = slopes[nslope].y+(slopes[nslope].axis.y/slopes[nslope].axis.x)*(bead.x-slopes[nslope].x)
    kinetic.pos = [bead.pos, (bead.x,ypotential,0)]
    parrow.pos = bead.pos+voffset
    parrow.axis = bead.p
    farrow.pos = bead.pos+foffset
    farrow.axis = vector(Fx,0,0)
    
    if bead.x >= xright and newv > 0:
        nslope = nslope+1
    elif bead.x <= xleft and newv <= 0:
        nslope = nslope-1
    if not 0 <= nslope <= (len(slopes)-1):
        if nslope < 0:
            ypotential = slopes[0].y+slopes[0].axis.y
        else:
            ypotential = slopes[-1].y+slopes[-1].axis.y
        while 1:
            if scene.mouse.clicked:
                return 0
            rate(200)
            bead.pos = bead.pos+(bead.p/bead.m)*dt
            kinetic.pos = [bead.pos, (bead.x,ypotential,0)]
            parrow.pos = bead.pos+voffset
            parrow.axis = bead.p

    if dt < deltat:
        update(deltat-dt)
    return 1
        
def makewell():
    global slopes
    even = 1
    slopes = []
    newwell.setvisible(visible=0)
    zero.visible = 0
    lastpos = None
    while 1: # create the potential well
        rate(100)
        if scene.mouse.events:
            m = scene.mouse.getevent()
            if m.drag:
                lastpos = m.project(normal=(0,0,1), d=0)
            if m.drop:
                if slopes <> []:
                    break
                lastpos = None
        if lastpos:
            newpos = scene.mouse.project(normal=(0,0,1), d=0)
            if newpos.x-lastpos.x > 0.1: # get pathologies if slopes extremely short
                slopes.append(box(pos=0.5*(newpos+lastpos),
                    size=(mag(newpos-lastpos),slopethick,slopedeep),
                    color=color.green))
                slopes[-1].rotate(
                    angle=-asin(dot(cross(norm(newpos-lastpos),vector(1,0,0)),vector(0,0,1))),
                    axis=(0,0,1))
                slopes[-1].xleft = lastpos.x
                slopes[-1].xright = newpos.x
                slopes[-1].yupper = slopes[-1].y+abs(0.5*slopes[-1].axis.y)
                slopes[-1].ylower = slopes[-1].y-abs(0.5*slopes[-1].axis.y)
                lastpos = newpos

    xright = slopes[-1].xright
    yzero = slopes[-1].yupper
    zero.pos = (xright+0.5*Lextra,yzero,0)
    zero.visible = 1
    newwell.setvisible(visible=1)

def setlevel():
    global nslope
    while 1:
        scene.mouse.getclick() # place the bead in the potential well (with initial v = 0)
        pos = scene.mouse.project(normal=(0,0,1), d=0)
        if pos:
            mx, my = pos.x, pos.y
            if scene.mouse.pick == newwell.box:
                return 'new well'
            possibles = [] # list of slopes for which the mouse is within upper, lower
            for s in slopes:
                if s.ylower <= my <= s.yupper and s.ylower <> s.yupper:
                    possibles.append(s)
            if possibles == []: continue # clicked above or below the whole well
            break
    
    minxdist = 1000.
    for p in possibles:
        if abs(mx-p.x) < minxdist:
            minxdist = abs(mx-p.x)
            best = p
    nslope = slopes.index(best)
    if best.axis.y < 0: # falling to the right
        xleft = best.xright-(my-best.ylower)*(best.xright-best.xleft)/(best.yupper-best.ylower)
        if best <> possibles[-1]:
            p2 = possibles[possibles.index(best)+1]
            xright = p2.xleft+(my-p2.ylower)*(p2.xright-p2.xleft)/(p2.yupper-p2.ylower)
        else:
            xright = slopes[-1].xright+Lextra
    else: # rising to the right
        xright = best.xleft+(my-best.ylower)*(best.xright-best.xleft)/(best.yupper-best.ylower)
        if best <> possibles[0]:
            p2 = possibles[possibles.index(best)-1]
            xleft = p2.xright-(my-p2.ylower)*(p2.xright-p2.xleft)/(p2.yupper-p2.ylower)
        else:
            xleft = slopes[0].xleft-Lextra
    level.pos = vector(0.5*(xleft+xright),my,0)
    level.size = (xright-xleft,slopethick,slopedeep)
    if xright > slopes[-1].xright:
        mx = xleft
    if xleft < slopes[0].xleft:
        mx = xright
    if abs(mx-xleft) < abs(mx-xright):
        bead.pos = vector(xleft,my,0)+boffset
    else:
        bead.pos = vector(xright,my,0)+boffset
    bead.m = 1.0
    bead.p = vector(0,0,0)
    kinetic.pos = [bead.pos, bead.pos]
    parrow.pos = bead.pos+voffset
    parrow.axis = bead.p
    for vobj in visualobjects:
        vobj.visible = 1
    return 'done'

scene.width = scene.height = 800
scene.x = scene.y = 0
scene.userzoom = 0
scene.background = color.white
scene.foreground = color.black
slopethick = 0.1 # thickness of each slope
slopedeep = 1. # depth of each slope
Lbox = 0.5 # edge length of sliding bead
Lextra = 5.0 # extend zero level this far to the right of right edge of well
scene.range = 10
scene.center = (10,0,0)
dt = 0.01

zero = box(pos=(0,0,0), size=(Lextra,slopethick,slopedeep), color=color.green, visible=0)
bead = box(size=(2.*slopethick,0.5*slopedeep,slopedeep), color=color.red, visible=0)
boffset = vector(0,0.5*bead.height+0.5*slopethick,0)
voffset = vector(0,bead.height,0)
foffset = vector(0,2*bead.height,0)
level = box(color=color.yellow, visible=0)
kinetic = curve(radius=0.05, color=color.magenta, visible=0)
parrow = arrow(shaftwidth=0.2, color=color.cyan, visible=0)
farrow = arrow(shaftwidth=0.2, color=color.green, visible=0)
newwell = button(pos=[(17,-9,0),(19,-8,0)], text='New Well', visible=0)
visualobjects = [bead, level, kinetic, parrow] # don't show farrow after all; confusing

while 1:
    makewell()

    while 1:
        if setlevel() == 'new well':
            for s in slopes:
                s.visible = 0
            break
        
        while 1: # let the bead slide
            rate(200)
            if scene.mouse.clicked:
                break
            if not update(dt):
                break

        for vobj in visualobjects:
            vobj.visible = 0
    
    


    


