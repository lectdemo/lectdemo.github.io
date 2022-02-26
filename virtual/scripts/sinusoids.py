##############################
#Summing sinusoidal functions#
#Michael Malahe              #
#2006                        #
##############################

#Instructions:
#The buttons next to each graph control its parameters
#The outer lateral buttons change the phaseshift
#The inner lateral buttons change the frequency
#The vertical buttons change the amplitude

#Modules
from visual import *
from visual.graph import *
from visual.controls import *
from math import *

#Parameters
g1a = 1.
g1f = pi
g1phi = 0
g2a = 1.
g2f = pi
g2phi = 0
extent = 4*pi
da = 0.1
df = 0.1
dphi = 0.1
dt = 0.05

#Graph scenes
graph1 = gdisplay(x=0, y=0, width=874, height=200,
          xmax=extent, xmin=0., ymax=1, ymin=-1,
          foreground=color.white, background=color.black)
g1 = gcurve(gdisplay=graph1,color=color.white)
graph2 = gdisplay(x=0, y=200, width=874, height=200,
          xmax=extent, xmin=0., ymax=1, ymin=-1,
          foreground=color.white, background=color.black)
g2 = gcurve(gdisplay=graph2,color=color.white)
graph3 = gdisplay(x=0, y=400, width=874, height=400,
          xmax=extent, xmin=0., ymax=2, ymin=-2,
          foreground=color.white, background=color.black)
g3 = gcurve(gdisplay=graph3,color=color.white)

#Control function
def change(button,diff):
    exec(button+".diff="+str(diff))

#Control scene 1
c1 = controls(title='',
     x=874, y=0, width=150, height=200, range=50)

#Graph1 controls
subf1 = button(pos=(-10,0), width=10, height=10,
              text='', action=lambda:change("subf1",df))
subf1.diff = 0
addf1 = button(pos=(10,0), width=10, height=10,
              text='', action=lambda:change("addf1",-df))
addf1.diff = 0
suba1 = button(pos=(0,-20), width=10, height=10,
              text='', action=lambda:change("suba1",-da))
suba1.diff = 0
adda1 = button(pos=(0,20), width=10, height=10,
              text='', action=lambda:change("adda1",da))
adda1.diff = 0
addphi1 = button(pos=(20,0), width=10, height=10,
              text='', action=lambda:change("addphi1",-dphi))
addphi1.diff = 0
subphi1 = button(pos=(-20,0), width=10, height=10,
              text='', action=lambda:change("subphi1",dphi))
subphi1.diff = 0

#Control scene 2
c2 = controls(title='',
     x=874, y=200, width=150, height=200, range=50)

#Graph2 controls
subf2 = button(pos=(-10,0), width=10, height=10,
              text='', action=lambda:change("subf2",df))
subf2.diff = 0
addf2 = button(pos=(10,0), width=10, height=10,
              text='', action=lambda:change("addf2",-df))
addf2.diff = 0
suba2 = button(pos=(0,-20), width=10, height=10,
              text='', action=lambda:change("suba2",-da))
suba2.diff = 0
adda2 = button(pos=(0,20), width=10, height=10,
              text='', action=lambda:change("adda2",da))
adda2.diff = 0
addphi2 = button(pos=(20,0), width=10, height=10,
              text='', action=lambda:change("addphi2",-dphi))
addphi2.diff = 0
subphi2 = button(pos=(-20,0), width=10, height=10,
              text='', action=lambda:change("subphi2",dphi))
subphi2.diff = 0

#First Draw
for t in arange(0.,extent,dt):
            g1.plot(pos=(t,g1a*cos(g1f*t+g1phi)))
for t in arange(0.,extent,dt):
            g2.plot(pos=(t,g2a*cos(g2f*t+g2phi)))
for t in arange(0.,extent,dt):
            g3.plot(pos=(t,g1a*cos(g1f*t+g1phi)+g2a*cos(g2f*t+g2phi)))
 
#Main Loop
while 1:
    c1.interact()
    c2.interact()
    n=0
    for e in [adda1,suba1,addf1,subf1,adda2,suba2,addf2,subf2,addphi1,addphi2,subphi1,subphi2]:
        n+=e.diff
    if n != 0:
        #Change1
        if adda1.diff != 0:
            g1a += adda1.diff
            adda1.diff = 0
        if suba1.diff != 0:
            g1a += suba1.diff
            suba1.diff = 0
        if addf1.diff != 0:
            if g1f>df:
                g1f += addf1.diff
            addf1.diff = 0
        if subf1.diff != 0:
            g1f += subf1.diff
            subf1.diff = 0
        if subphi1.diff != 0:
            g1phi += subphi1.diff
            subphi1.diff = 0
        if addphi1.diff != 0:
            g1phi += addphi1.diff
            addphi1.diff = 0
        #Change2
        if adda2.diff != 0:
            g2a += adda2.diff
            adda2.diff = 0
        if suba2.diff != 0:
            g2a += suba2.diff
            suba2.diff = 0
        if addf2.diff != 0:
            if g2f>df:
                g2f += addf2.diff
            addf2.diff = 0
        if subf2.diff != 0:
            g2f += subf2.diff
            subf2.diff = 0
        if subphi2.diff != 0:
            g2phi += subphi2.diff
            subphi2.diff = 0
        if addphi2.diff != 0:
            g2phi += addphi2.diff
            addphi2.diff = 0
        print g1f
        #Graph 1
        g1.gcurve.visible=0
        g1 = gcurve(gdisplay=graph1,color=color.white)
        for t in arange(0.,extent,dt):
            g1.plot(pos=(t,g1a*cos(g1f*t+g1phi)))
        #Graph 2
        g2.gcurve.visible=0
        g2 = gcurve(gdisplay=graph2,color=color.white)
        for t in arange(0.,extent,dt):
            g2.plot(pos=(t,g2a*cos(g2f*t+g2phi)))
        #Graph 3
        g3.gcurve.visible=0
        g3 = gcurve(gdisplay=graph3,color=color.white)
        for t in arange(0.,extent,dt):
            g3.plot(pos=(t,g1a*cos(g1f*t+g1phi)+g2a*cos(g2f*t+g2phi)))


    
