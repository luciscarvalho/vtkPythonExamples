from defbar import bar
from defdispl_i import displ_i
from defparaview import paraview


t = num_repeats = 10
for i in range(t):
    displacement = bar(i)
    #displacement = displ_i(i)
    paraview(displacement,i)
