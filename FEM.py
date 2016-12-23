from defbar import bar
from defdispl_i import displ_i
from defparaview import paraview


t = num_repeats = 5
num_elems = 9
for i in range(t):
    displacement = bar(i, num_elems)
    #displacement = displ_i(i)
    paraview(displacement,i)
