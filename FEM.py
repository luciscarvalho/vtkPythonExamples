import numpy as np
import time
import vtk

from defbar import bar
from defdispl_i import displ_i
from defparaview import paraview

t = num_repeats = 6
for i in range(t):
    displacement = bar(i+1)
    #displacement = displ_i(i+1)
    paraview(displacement,i+1)
