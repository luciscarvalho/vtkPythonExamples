import numpy as np
import matplotlib.pyplot as plt
import time

def displ_i(num_elems):
    L = 20.0
    E = 20.0
    A = 25.0
    P = 4.0
    list_displ = []
    for i in range(1, num_elems+1):
        u = (P/(E*A))*(L*(i*L/num_elems)-(0.5)*(i*L/num_elems)**2)
        list_displ.append(u)
    #print list_displ
    return np.array(list_displ)
#displ_i(4)
