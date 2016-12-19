import numpy as np
from defbar import bar
from defdispl_i import displ_i

""" Difference between Analytical Method and F.E. Method displacements """
def difference(t):

    # Equation of Analytical Method

    FEM_displ = bar(t).transpose()
    list_displ, list_x = displ_i(t)

    list_displa = np.append([0.0],[list_displ])
    list_xs = np.append([0.0],[list_x])

    A = np.vstack([list_xs, np.ones(len(list_xs))]).T
    m, c = np.linalg.lstsq(A, list_displa)[0]

    print "Line Solution is y = {m}x + {c}".format(m=m,c=c)

    # Equation of F.E.M.

    FEM_displ = bar(t).transpose()
    FEM_displa = np.append([0.0],[FEM_displ])

    A, B, C = np.polyfit(list_xs, FEM_displa, 2)
    print A, 'x^2', B, 'x', '+', C

    # 


    #b = (-FEM_displ[0]*(1+2)/((0-1)*(0-2)))
difference(3)
