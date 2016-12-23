import numpy as np
import sympy as sp
from defbar import bar
from defdispl_i import displ_i
from analytic_solution import analytic_solution
from Elements import Element1D
from IntegrationGP import Integration2GP

""" Difference between Analytical Method and F.E. Method displacements """
def difference(t):

# Equation of Analytical Method
    L = 20.0
    E = 20.0
    A = 25.0
    P = 8.0*t**0.5

    list_u_anal = []
    num_elems = 9
    list_x1 = []
    list_x2 = []
    nodes = []

    for i in range(num_elems+1):
        x_1 = i*L/num_elems
        x_2 = ((i+1)*L/num_elems)+1
        nodes.append(x_1)
        lists = [x_1,x_2]
        gp = Integration2GP().GetIntegrationPoints()
        for xi in gp:
            N = 0.5*np.matrix([1-xi,xi+1])
            x = N*[[x_1], [x_2]]
            u = analytic_solution(x, L, E, A, P)
            list_u_anal.append(u)

    anal = np.array(list_u_anal)
    print anal

# Equation of F.E.M.
    list_u_fem = []
    list_u_fe = bar(t, num_elems)
    for elem in range(num_elems-1):
        u_1 = list_u_fe[elem]
        u_2 = list_u_fe[elem+1]
        gp = Integration2GP().GetIntegrationPoints()
        for xi in gp:
            N = 0.5*np.matrix([1-xi,xi+1])
            u_1_2 = np.array([u_1, u_2])
            u = N*u_1_2
            list_u_fem.append(u)
    fem = np.array(list_u_fem)

    print fem

# Difference
    wi = Integration2GP().GetIntegrationWeights()
    list_diff = []
    for i in range(num_elems-1):
        diff = np.sum((((list_u_anal[i])-(list_u_fem[i]))**2)*wi)
        list_diff.append(diff)

    print list_diff

# Plot points in a graphic
    print list_diff


difference(4)
