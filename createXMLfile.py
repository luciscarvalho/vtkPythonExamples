from xml.dom import minidom
#import os


doc = minidom.Document()

nd_line = doc.createElement('VTKFile')
nd_line.setAttribute('type', 'Collection')
doc.appendChild(nd_line)

rd_line = doc.createElement('Collection')
nd_line.appendChild(rd_line)

t = num_repeats = 10
for i in range(t):
    th_line =doc.createElement('DataSet')
    th_line.setAttribute('timestep', `i*720`)
    th_line.setAttribute('file', "Group_Elements"+`i`+".vtu")
    rd_line.appendChild(th_line)

nd_line_str = doc.toprettyxml(indent="\t")

save_path_file = "teste1.pvd"

with open(save_path_file, "w") as f:
    f.write(nd_line_str)







































"""
PRIMEIRA TENTATIVA

import numpy as np
import time
import vtk
import xml.etree.ElementTree as xml

from defbar import bar
from defdispl_i import displ_i
from defparaview import paraview


t = num_repeats = 10
for i in range(t):
    displacement = bar(i)
    #displacement = displ_i(i+1)
    paraview(displacement,i)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Create PVD File
    root = xml.Element("VTKFile")
    appt = xml.Element("Collection")
    root.append(appt)

    xml.SubElement(appt,"DataSet",file="Group_Elements"+`t`+".vtu", timestep= "`t`*720").text = ""

tree = xml.ElementTree(root)
tree.write("teste1.pvd")
"""
