from visual.graph import *

print """
Ruth Chabay Spring 2001
Numerical integration of an RC circuit.
"""

charge = gdisplay(title = 'Charge on capacitor vs. time', x=0, y=0,
                  xtitle = 't, s', ytitle = 'Q, coulombs', ymax=3.0, height=300)
Qgraph = gcurve(color = color.cyan)
Qgraph.plot(pos=(0,0))
current = gdisplay(title = 'Current vs. time', x=0, y=300,
                   xtitle = 't, s', ytitle = 'I, amperes')
Igraph = gcurve(color = color.yellow)

emf = 3.0
C = 1.0
R = 15.0
Q = 0
dt = 0.01
t = 0.0
deltaV = 0.0
I = 0.0

while t < 150.:
    dQ = dt*(emf-Q/C)/R
    Q = Q+dQ
    t = t+dt
    Qgraph.plot(pos=(t,Q))
    I = dQ/dt
    Igraph.plot(pos=(t,I))






    
    
