from visual import *

print """
Ruth Chabay 2001-03-23
Program for introducing Gauss's Law qualitatively
See Matter & Interactions II: Electric & Magnetic Interactions, Chapter 21
In options 1-4 clicking on box toggles visibility of source charges.
 (move inside the box for options 1 and 2)
  1: pos inside, 2: neg inside,
  3: pos plate, some inside, 4: capacitor outside
In "nhat" example, clicking on box changes angle of E;
  first 5 times without nhat, next 5 times with nhat
 (this shows that we need an angle in the flux formula)
In "amount" example, clicking on box changes amt. of charge
  inside box (need mag(E) in the flux formula)
In "boxsize" example, clicking on box changes size of box,
  but not amount of charge (need area in the flux formula)
In all cases clicking in small window returns to main menu.
"""

def killobjects():
    for obj in scene.objects:
        obj.visible = 0

def one():
    killobjects()
    scene.autoscale = 1
    L = 3.0
    W = 1.5
    H = 1.5
    b = box(pos=(0,0,0), length=L, height=H, width=W)
    dL = L/3.
    dh = dw = H/2.

    dLq = L/3.
    charges = []
    for x in arange(-L/2.+dL/2., L/2., dLq):
        charges.append(sphere(pos=(x,0,0), radius=0.1, q=+0.3, color=color.red,
                              visible=0))

    obsloc = []
    for x in arange(-L/2.+dL/2., L/2., dL):
        obsloc.append(vector(x,0,W/2.))
        obsloc.append(vector(x,0,-W/2.))
        obsloc.append(vector(x,H/2.,0))
        obsloc.append(vector(x,-H/2.,0))
    for z in arange(-W/2.+dw/2., W/2., dw):
        obsloc.append(vector(L/2.,0,z))
        obsloc.append(vector(-L/2.,0,z))

    escale = 2.

    for pt in obsloc:
        E=vector(0,0,0)
        for q in charges:
            r = pt - q.pos
            E = E+norm(r)*q.q/mag(r)**2
        Ea = arrow(pos=pt, axis=E*escale, color=(1.,.6,0), shaftwidth=0.2)

    rr = 5.
    pt = vector(-0.9*rr,-0.9*rr, 0)
    while 1:
        if w2.mouse.events:
            m2 = w2.mouse.getevent()
            if m2.click == "left":
                return
        if scene.mouse.events:
            m1 = scene.mouse.getevent()
            if m1.click == "left" and scene.mouse.pick != None:
                for obj in charges:
                    obj.visible = not(obj.visible)

  
def two():
    killobjects()
    scene.autoscale = 1
    L = 3.0
    W = 1.5
    H = 1.5
    b = box(pos=(0,0,0), length=L, height=H, width=W)
    dL = L/3.
    dh = dw = H/2.

    dLq = L/3.
    charges = []
    for x in arange(-L/2.+dL/2., L/2., dLq):
        charges.append(sphere(pos=(x,0,0), radius=0.1, q=-0.3, color=color.blue,
                              visible=0))

    obsloc = []
    for x in arange(-L/2.+dL/2., L/2., dL):
        obsloc.append(vector(x,0,W/2.))
        obsloc.append(vector(x,0,-W/2.))
        obsloc.append(vector(x,H/2.,0))
        obsloc.append(vector(x,-H/2.,0))
    for z in arange(-W/2.+dw/2., W/2., dw):
        obsloc.append(vector(L/2.,0,z))
        obsloc.append(vector(-L/2.,0,z))

    escale = 2.

    for pt in obsloc:
        E=vector(0,0,0)
        for q in charges:
            r = pt - q.pos
            E = E+norm(r)*q.q/mag(r)**2
        ppt = pt-E*escale
        Ea = arrow(pos=ppt, axis=E*escale, color=(1.,.6,0), shaftwidth=0.2)

    while 1:
        if w2.mouse.events:
            m2 = w2.mouse.getevent()
            if m2.click == "left":
                return
        if scene.mouse.events:
            m1 = scene.mouse.getevent()
            if m1.click == "left" and scene.mouse.pick != None:
                for obj in charges:
                    obj.visible = not(obj.visible)
                scene.autoscale = 0

def three():
    killobjects()
    scene.autoscale = 1

    L = 3.0
    W = 1.5
    H = 1.5
    b = box(pos=(0,0,0), length=L, height=H, width=W)
    dL = L/3.
    dh = dw = H/2.

    dLq = L/3.
    charges = []

    wf = 10.0
    x = 0
    for z in arange(-W*wf,W*wf+dw,dw):
        for y in arange(-W*wf,W*wf+dw,dw):
            charges.append(sphere(pos=(x,y,z), radius=0.1, q=0.2, color=color.red,
                                  visible=0))

    obsloc = []
    for x in arange(-L/2.+dL/2., L/2., dL):
        if x==0: continue
        obsloc.append(vector(x,0,W/2.))
        obsloc.append(vector(x,0,-W/2.))
        obsloc.append(vector(x,H/2.,0))
        obsloc.append(vector(x,-H/2.,0))
    for z in arange(-W/2.+dw/2., W/2., dw):
        obsloc.append(vector(L/2.,0,z))
        obsloc.append(vector(-L/2.,0,z))

    escale = 3.

    for pt in obsloc:
        # make E ablsolutely parallel to x axis
        if pt.x < 0:
            E = vector(-1,0,0)
        else:
            E = vector(1,0,0)
        # compute E for real charges    
        ##    E=vector(0,0,0)
        ##    for q in charges:
        ##        r = pt - q.pos
        ##        E = E+norm(r)*q.q/mag(r)**2
        Ea = arrow(pos=pt, axis=E*escale, color=(1.,.6,0), shaftwidth=0.2)

    while 1:
        if w2.mouse.events:
            m2 = w2.mouse.getevent()
            if m2.click == "left":
                return
        if scene.mouse.events:
            m1 = scene.mouse.getevent()
            if m1.click == "left" and scene.mouse.pick != None:
                for obj in charges:
                    obj.visible = not(obj.visible)
                scene.autoscale = 0

def four():
    killobjects()
    scene.autoscale = 1
    L = 3.0
    W = 1.5
    H = 1.5
    b = box(pos=(0,0,0), length=L, height=H, width=W)
    dL = L/3.
    dh = dw = H/2.

    dLq = L/3.
    charges = []

    x = -1.5*L
    for z in arange(-W,W+dw,dw):
        for y in arange(-W,W+dw,dw):
            charges.append(sphere(pos=(x,y,z), radius=0.1, q=0.2, color=color.red,
                                  visible=0))
            charges.append(sphere(pos=(-x,y,z), radius=0.1, q=-0.2, color=color.blue,
                                  visible=0))

    obsloc = []
    for x in arange(-L/2.+dL/2., L/2., dL):
        obsloc.append(vector(x,0,W/2.))
        obsloc.append(vector(x,0,-W/2.))
        obsloc.append(vector(x,H/2.,0))
        obsloc.append(vector(x,-H/2.,0))
    for z in arange(-W/2.+dw/2., W/2., dw):
        obsloc.append(vector(L/2.,0,z))
        obsloc.append(vector(-L/2.,0,z))

    escale = 2.

    for pt in obsloc:
        E=vector(0,0,0)
        for q in charges:
            r = pt - q.pos
            E = E+norm(r)*q.q/mag(r)**2
        if pt.x == -L/2.:
            ppt = pt-E*escale
        else:
            ppt = pt
        Ea = arrow(pos=ppt, axis=E*escale, color=(1.,.6,0), shaftwidth=0.2)

    while 1:
        if w2.mouse.events:
            m2 = w2.mouse.getevent()
            if m2.click == "left":
                return
        if scene.mouse.events:
            m1 = scene.mouse.getevent()
            if m1.click == "left" and scene.mouse.pick != None:
                for obj in charges:
                    obj.visible = not(obj.visible)
                scene.autoscale = 0

def returnclick():
    while 1:
        if w2.mouse.events:
            m2 = w2.mouse.getevent()
            if m2.click == "left":
                return 1
        if scene.mouse.events:
            m1 = scene.mouse.getevent()
            if m1.click == "left" and scene.mouse.pick != None:
                return 0

def nhat():       
    killobjects()
    scene.autoscale = 1
    L = 0.2
    lth = 3
    W = 1.5/2.
    H = 1.5/2.
    b = box(pos=(0,0,0), length=L, height=2*H, width=2*W)
    aa = [(0,H,H), (-3,H,H),(-3,-H,H),(0,-H,H)]
    bb = [(0,H,-H), (-3,H,-H),(-3,-H,-H),(0,-H,-H)]
    cc =[(-3,H,-H), (-3,H,H)]
    dd = [(-3,-H,-H), (-3,-H,H)]

    curve(pos=aa)
    curve(pos=bb)
    curve(pos=cc)
    curve(pos=dd)

    Ea = arrow(pos=(L/2.,0,0), shaftwidth=0.2, axis = (3,0,0), color=(1,.6,0))
    scene.autoscale = 0
    nhat = arrow(pos=(L/2.,0,.2), shaftwidth=0.2, axis=(1,0,0),
                 color=color.green, visible = 0)
    while 1:
        nhat.visible = 0
        Ea.axis = (3,0,0)
        if returnclick(): return
        Ea.axis = 3*norm(vector(1,1,0))
        if returnclick(): return
        Ea.axis = 3*vector(0,1,0)
        if returnclick(): return
        Ea.axis = 3*norm(vector(-1,1,0))
        if returnclick(): return
        Ea.axis = vector(-3,0,0)

        if returnclick(): return        
        Ea.visible = 0
        nhat.visible = 1
        if returnclick(): return
        Ea.visible = 1
        Ea.axis = vector(3,0,0)
        if returnclick(): return
        Ea.axis = 3*norm(vector(1,1,0))
        if returnclick(): return
        Ea.axis = 3*vector(0,1,0)
        if returnclick(): return
        Ea.axis = 3*norm(vector(-1,1,0))
        if returnclick(): return
        Ea.axis = vector(-3,0,0)
        if returnclick(): return

def amount():
    killobjects()
    scene.autoscale = 1
    escale = 4.
    LL = 3.0
    dLq = LL/3.
    charges = []
    for x in arange(-LL/2.+dLq/2., LL/2., dLq):
        charges.append(sphere(pos=(x,0,0), radius=0.1, q=+0.2, color=color.red,
                              visible=0))
    boxfactor = 1.0
    L = 3.0*boxfactor
    W = 1.5*boxfactor
    H = 1.5*boxfactor
    dL = L/3.
    dh = dw = H/2.
    b = box(pos=(0,0,0), length=L, height=H, width=W, color=(.8,.8,1))
    scene.autoscale = 0
    scene.range = 10.

    obsloc = []
    for x in arange(-L/2.+dL/2., L/2., dL):
        obsloc.append(vector(x,0,W/2.))
        obsloc.append(vector(x,0,-W/2.))
        obsloc.append(vector(x,H/2.,0))
        obsloc.append(vector(x,-H/2.,0))
    for z in arange(-W/2.+dw/2., W/2., dw):
        obsloc.append(vector(L/2.,0,z))
        obsloc.append(vector(-L/2.,0,z))

    amount = 0
    Earr = []
    while 1:
        if returnclick(): return
        for obj in Earr:
            obj.visible = 0
            
        if amount:
            for qq in charges:
                qq.q = 0.2
        else:
            for qq in charges:
                qq.q = 0.6
        amount = not(amount)
        
        Earr = []
        for pt in obsloc:
            E=vector(0,0,0)
            for q in charges:
                r = pt - q.pos
                E = E+norm(r)*q.q/mag(r)**2
            Ea = arrow(pos=pt, axis=E*escale, color=(1.,.6,0), shaftwidth=0.2)
            Earr.append(Ea)

def boxsize():
    killobjects()
    scene.autoscale = 1
   
    escale = 6.
    size = 1
    LL = 3.0
    dLq = LL/3.
    charges = []
    for x in arange(-LL/2.+dLq/2., LL/2., dLq):
        charges.append(sphere(pos=(x,0,0), radius=0.1, q=+0.3, color=color.red,
                              visible=0))

    while 1:
        for obj in scene.objects:
            obj.visible = 0           
        if size:
            boxfactor = 1.0
            boxcolor = (1,.8,1)
        else:
            boxfactor = 2.0
            boxcolor = (.8,1.,.8)
        size = not(size)
        
        L = 3.0*boxfactor
        W = 1.5*boxfactor
        H = 1.5*boxfactor
        dL = L/3.
        dh = dw = H/2.
        b = box(pos=(0,0,0), length=L, height=H, width=W, color=boxcolor)

        obsloc = []
        for x in arange(-L/2.+dL/2., L/2., dL):
            obsloc.append(vector(x,0,W/2.))
            obsloc.append(vector(x,0,-W/2.))
            obsloc.append(vector(x,H/2.,0))
            obsloc.append(vector(x,-H/2.,0))
        for z in arange(-W/2.+dw/2., W/2., dw):
            obsloc.append(vector(L/2.,0,z))
            obsloc.append(vector(-L/2.,0,z))

        for pt in obsloc:
            E=vector(0,0,0)
            for q in charges:
                r = pt - q.pos
                E = E+norm(r)*q.q/mag(r)**2
            Ea = arrow(pos=pt, axis=E*escale, color=(1.,.6,0), shaftwidth=0.2)

        scene.autoscale = 0
        if returnclick(): return
        
###################################################
w2 = display(x=950, y=0, height=50, width=20)
scene = display(x=0,y=0,width=950,height=768)
scene.background = (0.7,0.7,0.7)

labeltexts = ['one','two','three','four',
              'nhat','amount','boxsize']
space = 4

while 1:
    killobjects()
    menu = []
    for i in arange(0,len(labeltexts)):
        y = space*len(labeltexts)/2.-space*i
        a = sphere(pos=(-4,y,0), radius=1.5, color=color.green)
        menu.append(a)
        a.lbl = label(pos=a.pos, xoffset = 20, text=labeltexts[i],
                      box=0, opacity=0)

    bw = 20    
    title = label(pos=(0,bw-1.5,0), text="Gauss's Law", box=1)
    y=y-space
    dir2 = label(pos=(0,y,0),
                 text ='Click in small window to return to menu')
    fr = curve(pos = [(-bw,-bw,0), (-bw,bw,0), (bw,bw,0), (bw,-bw,0),
                      (-bw,-bw,0)])
    scene.mouse.getclick()
    if scene.mouse.pick == None:
        continue
    else:
        selected = scene.mouse.pick
        bb = menu.index(selected)
        option_name = selected.lbl.text
        option = globals().get(option_name)
        if option:
            option()
            scene.autoscale = 1
            scene.forward = (0,0,-1)




    
