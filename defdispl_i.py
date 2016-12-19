import numpy as np

def displ_i(t):
    """Displacement (Analytical Method)"""

    L = 20.0
    E = 20.0
    A = 25.0
    P = 8.0*t**0.5
    list_disp = []
    lis_x = []
    num_elems = 9
    for i in range(1, num_elems+1):
        u = (P/(E*A))*(L*(i*L/num_elems)-(0.5)*(i*L/num_elems)**2)
        list_disp.append(u)
        lis_x.append(i*20)
    list_displ = np.array(list_disp)
    list_x = np.array(lis_x)
    print list_displ
    return list_displ, list_x

displ_i(1)
