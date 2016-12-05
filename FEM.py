import numpy as np
import time
import vtk

from defbar import bar                            # Assembly Local to Global Matrix, Displacement (FEM)
from defdispl_i import displ_i                    # Displacement (Analytical Method)
from defparaview import paraview                  # Paraview for FEM Displacement, clock and files vtu

t = num_repeats = 6
for i in range(t):
    displacement = bar(i+1)
    #displacement = displ_i(i+1)
    paraview(displacement,i)
