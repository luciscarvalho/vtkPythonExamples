import numpy as np

def displ_i(num_elems):
    # Analytical Method - Displacement

    L = 20.0
    E = 20.0
    A = 25.0
    P = 4.0
    list_disp = []
    for i in range(1, num_elems+1):
        u = (P/(E*A))*(L*(i*L/num_elems)-(0.5)*(i*L/num_elems)**2)
        list_disp.append(u)
    list_displ = np.array(list_disp)
    return list_displ
#displ_i(i+1)


"""def difference():
# Difference between Analytical Method and F.E. Method displacements

    FEM_displ = bar(6).transpose()
    Anal_displ = displ_i(6)

    u = (FEM_displ - Anal_displ)**2
    #u = sp.integrate(FEM_displ - Anal_displ)**2

    print FEM_displ
    print Anal_displ
    print u


difference()"""
