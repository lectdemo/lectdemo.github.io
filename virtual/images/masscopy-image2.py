################
#Mass copying  #
#Copyright 2007#
#Michael Malahe#
################

from __future__ import division
from os import *
from os.path import *
import Image as I

#Parameters
trydrives = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
specific = 'C:\Documents and Settings\Michael.MIKL\My Documents\Current Projects\Physics Department\Website\\virtual\images\\backup'
ending = ".JPG"
mode = 'path'
display = 'yes'
maxres = 700

#Initial values
drives = []
origin = getcwd()
found = []

def isDirectory(string):
    if string.find(".") == -1:
        return 1
    else:
        pass

def search(directory, suffix):
    files = listdir(directory)
    print files
    winners = []
    for element in files:
        if element.endswith(suffix):
            #check resolution
            chdir(directory)
            im = I.open(element)
            res = im.size
            ratio = res[1]/res[0]
            print "..."
            if res[0]>maxres or res[1]>maxres:
                if res[1]>=res[0]:
                    xres = int(maxres/ratio)
                    im = im.resize((xres,maxres))
                if res[0]>res[1]:
                    yres = int(maxres*ratio)
                    im = im.resize((maxres,yres))
            #write
            chdir(origin)
            im.save(element)
            #add to winners
            winners.append(element)
    if winners is []:
        pass
    else:
        return winners

def hunt(main, suffix):
    files = listdir(main)
    print main
    directories = []
    for element in files:
        directories.append(element)
    for directory in directories:
        path = main + "\\" + directory
        try:
            hunt(path, suffix)
        except:
            pass
    print "..."
    if search(main, suffix) is not []:
        found.append(search(main, suffix))

for drive in trydrives:
    drivename = drive + ":\\"
    try:
        chdir(drivename)
        drives.append(drive)
    except:
        pass

if mode is 'path':
    hunt(specific, ending)
if mode is 'drive':
    for drive in drives:
        drivename = drive + ":\\"
        hunt(drivename, ending)

if display is 'yes': 
    mock = []
    final = []
    for element in found:
        if len(element) == 0:
            pass
        else:
            mock.append(element)
    for element in mock:
        for a in element:
            final.append(a)
    print final
