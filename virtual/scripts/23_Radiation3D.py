from visual import *
scene.background = color.white

#
# This program visualizes the radiative E and B fields of a charged particle
# receiving a brief acceleration. Before the acceleration, the particle was
# stationary. After the acceleration, the particle moves with constant
# momentum although this motion is not shown. For obvious reasons, the
# outgoing pulse will have already propagated a finite distance from the
# particle when the simulation starts.
#
# Joe Heafner, April 2003
#
# Future modifications:
#  1) show Poynting vector
#  2) click the mouse to stop and start propagation
#  3) show the radial field inside and/or outside the spherical wavefront
#  4) allow the particle to oscillate
#

print "The spherical wavefront propagates outward at speed c."

# Set up the scene
##scene.width = scene.height = 550
scene.width = 1024
scene.height=768
scene.x = scene.y = 0
scene.forward = (-1, -1, -5)

# Create an array of field points (observer locations). This is a spherical
# distribution of points, but you could also use a rectangular distribution
# of points.

# Coordinate transformation for the grid of field points.
# Note that this is not the standard textbook transformaton!
# <x, y, z> = <r sin(theta) cos(phi), r cos(theta), r sin(theta) sin(phi)>
# phi wraps around the y-axis
# theta is relative to +y-axis
#
# This mapping of spherical coords to rectangular coords matches VPython's
# coordinate axis orientation, with y pointing "up". This is merely a matter
# of taste though. Most textbooks use the convention that z points up.

rmin = 0.3e-11  # Minimum radius
dr = 0.5e-11    # Increment in radius
dtheta = pi/6.  # Increment in theta
dphi = pi/6.    # Increment in phi

obsloc = []     # Empty array
# We need the extra dr if we want r to assume the last possible value.
# This is also apparently necessary for theta and phi.
for r in arange(rmin, 2.*rmin, dr):
    for phi in arange(0., 2.*pi+dphi, dphi):
        # Start theta at something other than zero in order to avoid a
        # singularity on the y-axis.
        for theta in arange(dtheta, pi+dtheta, dtheta):
            a = vector(r*sin(theta)*cos(phi), r*cos(theta), r*sin(theta)*sin(phi))
            obsloc.append(a)
            # Put a tiny dot at each point if desired
            # sphere(pos=a, radius=1e-13, color=color.green)

# Speed of light
c = 3e8
c2 = c**2

# Define a charged particle
particle = sphere(pos=(0,0,0), radius=3e-13, color=color.red)


# Make the charge negative if you want an electron (also make it blue!)
particle.charge = 1.6e-19
if particle.charge < 0:
    particle.color=color.blue

#####################################
scene.range = 1e-011
scene.mouse.getclick()
if particle.charge > 0:
    particle.color = (1,.7,.7)
else:
    particle.color = (.7,.7,1)
####################################
    
# Define particle's acceleration
acc = vector(0,-2e17,0)

# Scale factor for pretty acc arrow
ascale = 0.04*2e-11/1e17   ##0.05*2e-11/1e17

accarr = arrow(pos=particle.pos, axis=ascale*acc, shaftwidth=0.2e-12, color=color.yellow)

# Coulomb constant
kel = 9e9

# Scale factor for pretty E arrows
escale = 0.1*2e-11/500.

# Scale factor for pretty B arrows
bscale = 0.3*2e-11/1e-5

# Create an array of E and B and a_perp arrows
Earr = []     # Empty array
Barr = []     # Empty array
# aarr = []     # Empty array
for pt in obsloc:

    # Position of field point relative to particle
    r = pt - particle.pos
    rhat = norm(r)

    # The component of acceleration perpendicular to r is just vector r
    # minus the parallel component of acceleration. The parallel component
    # of acceleration has a magnitude equal to the dot product of acceleration
    # and rhat, and is directed parallel to rhat.
    aperp = acc - dot(acc,rhat)* rhat

    # Visualize a_perp at each point if desired
    # Not recommended if you're visualizing the fields
    # a = arrow(pos=pt, axis=ascale*aperp, shaftwidth=0.2e-12, color=color.green)
    # aarr.append(aa)

    # Calculate radiative E field
    Erad = -kel * particle.charge * aperp / (c**2 * mag(r))
    
    b = arrow(pos=pt, axis=escale*Erad, shaftwidth=0.2e-12, color=color.orange)
    Earr.append(b)

    # Calculate radiative B field
    # The B field has magnitude E/c and is in the direction of rhat cross Erad.
    rhatcrossE = cross(rhat,Erad)
    Brad =  (mag(Erad)/c) * norm(rhatcrossE)
    
    cc = arrow(pos=pt, axis=bscale*Brad, shaftwidth=0.2e-12, color=color.cyan)
    Barr.append(cc)

scene.autoscale = 0
##print scene.range
##scene.mouse.getclick()

# Propagate the pulse
dt = 1e-22
t = 0.0
while t < 1:
    rate(30)
    if scene.mouse.clicked:
        scene.mouse.getclick()
        scene.mouse.getclick()
    i = 0
    for pt in obsloc:
        
        # Get a new field point by increasing the magnitude of the current
        # vector from the field point to the origin. The components will
        # automatically be updated.
        pt.mag = pt.mag + c * dt
        r = pt - particle.pos
        rhat = norm(r)

        # Update perpendicular component of acceleration
        aperp = acc - dot(acc,rhat) * rhat
        
        # aarr[i].pos = pt
        # aarr[i].axis = ascale*aperp

        # Update the E field and B field
        Erad = -kel * particle.charge * aperp / (c**2 * mag(r))
        Earr[i].pos = pt
        Earr[i].axis = escale*Erad
        rhatcrossE = cross(rhat,Erad)
        Brad = (mag(Erad)/c) * norm(rhatcrossE)
        Barr[i].pos = pt
        Barr[i].axis = bscale*Brad
        i = i + 1
    t = t + dt
