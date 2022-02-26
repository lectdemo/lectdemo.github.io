#Creates left-hand navigation and index pages

from os import *
from os.path import *

#Parameters
specific = "C:\Documents and Settings\~Michael\My Documents\Current Projects\Physics Department\Website\pracs"
navname = 'leftnav.txt'
tocname = 'toc.txt'
ending = ".html"
mode = 'path'
display = 'yes'
section = 'ad'

#Initialise files
nav = file(navname,'w+')
nav.write("")
nav.close()
toc = file(tocname, 'w+')
toc.write('<table width="0%"  border="0" cellpadding=" " cellspacing=" ">\n'+
          '<tr bgcolor="#CCCCCC">\n'+
          '<th scope="col"><div align="left" style="font-size: small">Name</div></th>\n'+
          '<th scope="col"><div align="left">Purpose</div></th>\n'+
          '</tr>\n')
toc.close()

#Initial values
drives = []
origin = getcwd()
found = []

def clean(string):
    try:
        if string[0] == " ":
            string = string[1:len(string)]
        if string[-1] == " ":
            string = string[0:len(string)-1]
    except:
        pass
    return string

def isDirectory(string):
    if string.find(".") == -1:
        return 1
    else:
        pass

def search(directory, suffix):
    files = listdir(directory)
    winners = []
    tochead = 1
    for element in files:
        if element.endswith(suffix):
            length = len(element)
            iTitle = length
            for i in range(length):
                try:
                    int(element[i])
                    iTitle = i
                    break
                except:
                    pass
            secPref = element[0:iTitle]
            if secPref == section:
                print element
                #read
                chdir(directory)
                infile = file(element, 'r')
                #write
                chdir(origin)
                nav = file(navname,'a')
                toc = file(tocname,'a')
                #MODIFICATIONS GO HERE
                #Find name and purpose
                string1 = ""
                string2 = ""
                for line in infile.readlines():
                    i = -1
                    k = -1
                    l = -1
                    start1 = 'name="purpose" -->'
                    stop1 = '<!-- InstanceE'
                    i = line.find(start1)
                    if  i != -1:
                        j = line.find(stop1)
                        string1 = clean(line[i+len(start1):j])
                    start2 = 'name="title" -->'
                    stop2 = '<!-- InstanceE'
                    k = line.find(start2)
                    if  k != -1:
                        l = line.find(stop2)
                        string2 = clean(line[k+len(start2):l])
                    start3 = 'name="ref" -->'
                    stop3 = '<!-- InstanceE'
                    l = line.find(start3)
                    if  l != -1:
                        m = line.find(stop3)
                        string3 = clean(line[l+len(start3):m])
                #Write lefnav
                string0 = '<a href="'+'../pracs/'+element+'" title="'
                nav.write(string0+string1+'">'+string3+":"+string2+'</a>')
                nav.write("\n<br>\n")
                #Write toc
                if tochead == 1:
                    tochead = 0
                    toc.write('<tr>\n')
                    toc.write('<td width="213" scope="col"><h2 align="left" style="font-size: small"><a href="')
                    toc.write(element)
                    toc.write('">'+string2+'</a></h2></td>\n')
                    toc.write('<td width="643" scope="col"><div align="left">'+string1+'</div></td>\n')
                    toc.write('</tr>\n')
                elif tochead == 0:
                    toc.write('<tr>\n')
                    toc.write('<td><h2 align="left" style="font-size: small"><a href="')
                    toc.write(element)
                    toc.write('">'+string3+":"+string2+'</a></h2></td>\n')
                    toc.write('<td><div align="left">'+string1+'</div></td>\n')
                    toc.write('</tr>\n')
                #Close file
                infile.close()
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
    if search(main, suffix) is not []:
        found.append(search(main, suffix))

search(specific, ending)
toc = file(tocname,'a')
toc.write('</table>')
toc.close()

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
