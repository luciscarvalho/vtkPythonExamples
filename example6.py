#!/usr/bin/env python
#------------------------------------------------------------------------------#
#                                   Imports                                    #
#------------------------------------------------------------------------------#
import vtk
VTK_MAJOR_VERSION = vtk.VTK_VERSION[0]

LEVEL = 6

#------------------------------------------------------------------------------#
#                                   Main Code                                  #
#------------------------------------------------------------------------------#
def main():
    points = vtk.vtkPoints()
    points.InsertNextPoint(0.0, 0.0, 0.0)
    points.InsertNextPoint(1.0, 0.0, 0.0)
    points.InsertNextPoint(2.0, 0.0, 0.0)
    points.InsertNextPoint(3.0, 0.0, 0.0)
    points.InsertNextPoint(4.0, 0.0, 0.0)

    lines = vtk.vtkCellArray()
    line = vtk.vtkLine()
    line.GetPointIds().SetId(0, 0)
    line.GetPointIds().SetId(1, 1)
    lines.InsertNextCell(line)
    line.GetPointIds().SetId(0, 1)
    line.GetPointIds().SetId(1, 2)
    lines.InsertNextCell(line)
    line.GetPointIds().SetId(0, 2)
    line.GetPointIds().SetId(1, 3)
    lines.InsertNextCell(line)
    line.GetPointIds().SetId(0, 3)
    line.GetPointIds().SetId(1, 4)
    lines.InsertNextCell(line)

    warpData = vtk.vtkDoubleArray()
    warpData.SetNumberOfComponents(3)
    warpData.SetName("warpData")
    warp = [0.0, 0.0, 0.0]
    warp[1] = 0.0
    warpData.InsertNextTuple(warp)
    warp[1] = 0.1
    warpData.InsertNextTuple(warp)
    warp[1] = 0.3
    warpData.InsertNextTuple(warp)
    warp[1] = 0.0
    warpData.InsertNextTuple(warp)
    warp[1] = 0.1
    warpData.InsertNextTuple(warp)

    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)
    polydata.SetLines(lines)
    polydata.GetPointData().AddArray(warpData)
    polydata.GetPointData().SetActiveVectors(warpData.GetName())
