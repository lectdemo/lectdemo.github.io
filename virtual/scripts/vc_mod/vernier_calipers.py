##################
#Vernier Calipers#
#Michael Malahe  #
#2007            #
##################

#INSTRUCTIONS:
#Click and drag the small scale to move it
#Press x to centre on your measurement
#Press z to zoom back out

#Modules
from visual import *
from math import *

#Visual parameters
linethickness = 0.025
fontsize = 30

#Scene alignment
scene.center = (10,0,0)
scene.fullscreen = 1
scene.userspin = 0


def l2s(l):
    string = ""
    for a in l:
        string += a
    return string

#Importer#
################
def blender_import(filename,col):
    #Import file
    f = open(filename, 'r')
    array = eval(f.readline())
    #Convert file
    a = frame()
    for f in array:
        p = []
        for v in f:
            k = vector(v[0], v[1], v[2])
            p.append(k)
        p = [p[2], p[1], p[0]]
        #Normal calculation
        vec1 = p[2] - p[1]
        vec2 = p[0] - p[1]
        n = vec1.cross(vec2)
        n = n/mag(n)
        newface = faces(frame=a,pos=p,normal=n,color=[col,col,col])
    return a

#Visual objects#
################

#Superficial
leftend = blender_import("leftend.gxl",(0.8,0.8,0.8))
rightend = blender_import("rightend.gxl",(0.8,0.8,0.8))
divider = curve(pos=[(0,0),(20,0)])
connection = curve(pos=[(0,0),(0,0)],color=(1,0,0))

#Small scale#
scale_s = frame()
rightend.frame = scale_s
for a in arange(0,10.01,0.2):
    if float(int(a)) == float(a):
        pline = curve(frame=scale_s,pos=[((a/2)*0.98,0.),((a/2)*0.98,-0.5)])
        if a == 10:
            plabel = label(frame=scale_s,pos=((a/2)*0.98,-0.65),text="0",box=0)
        else:
            plable = label(frame=scale_s,pos=((a/2)*0.98,-0.65),text=str(int(a)),box=0)
    else:
        pline = curve(frame=scale_s,pos=[((a/2)*0.98,0.),((a/2)*0.98,-0.15)])
label1 = label(frame=scale_s,pos=(2.5,-2),text=str(round(scale_s.pos.x,2)))
#label2 = label(frame=scale_s,pos=(4.0,-2),text="+/-",box=0)
#label3 = label(frame=scale_s,pos=(5.0,-2),text="?")
label4 = label(frame=scale_s,pos=(4.0,-2),text="cm",box=0)

for a in [label1,label4]:
    a.height = fontsize

#Big scale
scale_b = frame()
for a in arange(0,20.01,0.1):
    if float(int(a)) == float(a):
        pline = curve(frame=scale_b,pos=[(a,1),(a,0.)])
        plabel = label(frame=scale_b,pos=(a,1.25),text=str(int(a)),box=0)
    elif float(int(a*2)) == float(a*2):
        pline = curve(frame=scale_b,pos=[(a,0.75),(a,0)])
    else:
        pline = curve(frame=scale_b,pos=[(a,0.35),(a,0)])

#Grabber
grabber = box(pos=(2.5,-0.35,-0.05), length=5, height=0.7, width=0.05, color=(0,0,0))

#Global Scaling
for obj in scene.objects:
    if obj.__class__ == curve:
        obj.radius = linethickness
standard = vector(scene.scale)

#Interaction#
#############
pick = None
scene.autoscale = 0
while 1:
    if scene.mouse.events:
        m1 = scene.mouse.getevent()
        if m1.drag and m1.pick == grabber:
            drag_pos = m1.pickpos 
            pick = m1.pick 
            scene.cursor.visible = 0 
        elif m1.drop:
            pick = None
            scene.cursor.visible = 1
    if pick:
        new_pos = scene.mouse.project(normal=(0,0,1))
        if new_pos != drag_pos:
            add = new_pos.x - drag_pos.x
            if pick.pos.x+add<2.5:
                pick.pos.x = 2.5
            elif pick.pos.x+add>17.5:
                pick.pos.x = 17.5
            else:
                pick.pos.x += add
            drag_pos = new_pos
    if scene.kb.keys: 
        s = scene.kb.getkey()
        if s == "z":
            scene.center = (10,0,0)
            scene.scale = standard
        if s == "x":
            scene.center = (scale_s.pos.x+2.5,0,0)
            scene.scale = 3*vector(standard)
    scale_s.pos.x = grabber.pos.x-2.5
    mval = str(round(scale_s.pos.x,2))
    dotpos = mval.find(".")
    end = [a for a in mval[dotpos+1:-1].zfill(2)]
    end.reverse()
    label1.text = mval[0:dotpos]+ "." + l2s(end)
    connection.pos = [(0,-5),(scale_s.pos.x,-5)]
