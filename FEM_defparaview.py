import time
import vtk
from FEM_Node1D import Node1D
from FEM_Integration2GP import Integration2GP
from FEM_Integration3GP import Integration3GP
from FEM_Element1D import Element1D
from FEM_defbar import bar
from FEM_defdispl_i import displ_i

def paraview(num_elems):
    L = 20.0
    points = vtk.vtkPoints()
    myline = vtk.vtkLine()
    num_nodes = num_elems+1
    time = 10
    list_displ = displ_i(num_nodes+1)
    mesh = vtk.vtkCellArray()
    for i in range(num_nodes):
        points.InsertNextPoint((i*L/(num_nodes-1)),0,0)
    for i in range(num_nodes-1):
        myline.GetPointIds().SetId(0,i)
        myline.GetPointIds().SetId(1,i+1)
        mesh.InsertNextCell(myline)
    #print mesh

    array = vtk.vtkDoubleArray()
    array.SetName("Displacement")
    array.SetNumberOfComponents(1)
    for i in range(num_nodes):
        array.InsertNextTuple1(list_displ[i])
    grid = vtk.vtkUnstructuredGrid()
    grid.SetPoints(points)
    grid.SetCells(vtk.VTK_LINE, mesh)
    grid.GetPointData().SetScalars(array)

    #bar(i+1)
    #displ_i(i+1)

    writer = vtk.vtkXMLUnstructuredGridWriter()
    writer.SetFileName("Group_Elements"+`i`+".vtu")
    writer.SetInputData(grid)
    writer.Write()
