import vtk
import numpy as np

def paraview(displacement,t):
    """ Paraview for FEM Displacement, clock and create files vtu """

    L = 20.0
    points = vtk.vtkPoints()
    myline = vtk.vtkLine()
    num_elems = len(displacement)
    num_nodes = num_elems+1
    displ_zero = [[0.0]]
    displ_list = np.vstack([displ_zero,displacement])
    mesh = vtk.vtkCellArray()


    for i in range(num_nodes):
        points.InsertNextPoint((i*L/(num_nodes-1)),0,0)
    for i in range(num_elems):
        myline.GetPointIds().SetId(0,i)
        myline.GetPointIds().SetId(1,i+1)
        mesh.InsertNextCell(myline)


    array = vtk.vtkDoubleArray()
    array.SetName("Displacement")
    array.SetNumberOfComponents(1)
    for i in range(num_nodes):
        array.InsertNextTuple1(displ_list[i])
    grid = vtk.vtkUnstructuredGrid()
    grid.SetPoints(points)
    grid.SetCells(vtk.VTK_LINE, mesh)
    grid.GetPointData().SetScalars(array)


    writer = vtk.vtkXMLUnstructuredGridWriter()
    writer.SetFileName("Group_Elements"+`t`+".vtu")
    writer.SetInputData(grid)
    writer.SetTimeStep(t*7200)
    writer.Write()

    return displ_list
