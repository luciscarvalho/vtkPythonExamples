from xml.dom import minidom

"""This file creates a PVD file for paraview with TimeSteps and Names for each file"""
doc = minidom.Document()

nd_line = doc.createElement('VTKFile')
nd_line.setAttribute('type', 'Collection')
doc.appendChild(nd_line)

rd_line = doc.createElement('Collection')
nd_line.appendChild(rd_line)

t = num_repeats = 5
for i in range(t):
    th_line =doc.createElement('DataSet')
    th_line.setAttribute('timestep', `i*720`)
    th_line.setAttribute('file', "Group_Elements"+`i`+".vtu")
    rd_line.appendChild(th_line)

nd_line_str = doc.toprettyxml(indent="\t")

save_path_file = "teste1.pvd"

with open(save_path_file, "w") as f:
    f.write(nd_line_str)
