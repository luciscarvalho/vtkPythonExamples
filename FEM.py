import numpy as np
import time
import vtk

from xml.dom import minidom
import os

from defbar import bar
from defdispl_i import displ_i
from defparaview import paraview


t = num_repeats = 10
for i in range(t):
    displacement = bar(i)
    #displacement = displ_i(i+1)
    paraview(displacement,i)
