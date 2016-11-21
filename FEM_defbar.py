import numpy as np
import matplotlib.pyplot as plt
import time

def bar(num_elems):
    L = 20.0
    YoungsModulus = 20
    Area = 25
    list_nodes = []
    list_elements = []
    K = np.zeros((num_elems+1,num_elems+1))
    F = np.zeros((num_elems+1,1))
    for i in range(num_elems+1):
        node = Node1D(i*L/num_elems)
        list_nodes.append(node)
    for i in range(num_elems):
        element = Element1D(YoungsModulus, Area, [list_nodes[i], list_nodes[i+1]])
        list_elements.append(element)
    for i in range(num_elems):
        K[i:i+2, i:i+2] += list_elements[i].GetKe()
        F[i:i+2] += list_elements[i].GetFe(4.0)
        restrained_DOF = [0]
    for dof in restrained_DOF:
        F = np.delete(F, dof, axis=0)
        for i in [0,1]:
            K = np.delete(K, dof, axis=i)
    displacement = np.linalg.solve(K, F)

    return displacement
#bar(4)
