import numpy as np
import time
import vtk


from FEM_Node1D import Node1D                      # Axis x and u is axis Y (displacement)
from FEM_Integration2GP import Integration2GP      # Gaussian Quadrature for 2 points
from FEM_Integration3GP import Integration3GP      # Gaussian Quadrature for 3 points
from FEM_Element1D import Element1D                # E, A, nodes, Ke, Fe, shape functions
from FEM_defbar import bar                         # Assembly Local to Global Matrix, Displacement (FEM)
from FEM_defdispl_i import displ_i                 # Displacement (Analytical Method)
from FEM_defparaview import paraview               # Paraview for FEM Displacement


print bar(4)
