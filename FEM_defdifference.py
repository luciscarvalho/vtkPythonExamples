def difference():
# Difference between Analytical Method and F.E. Method displacements

    FEM_displ = bar(6).transpose()
    Anal_displ = displ_i(6)

    u = (FEM_displ - Anal_displ)**2
    #u = sp.integrate(FEM_displ - Anal_displ)**2

    print FEM_displ
    print Anal_displ
    print u


difference()
