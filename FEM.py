import numpy as np
import matplotlib.pyplot as plt
import time

class Node1D:
    def __init__(self, x):
        self.x = x
        self.u = 0
class Integration2GP:
    def __init__(self):
        self.NumberOfGP = 2
    def GetIntegrationPoints(self):
        return [-np.sqrt(1./3.), np.sqrt(1./3.)]
    def GetIntegrationWeights(self):
        return [1, 1]
class Integration3GP:
    def __init___(self):
        self.NumberOfGP = 3
        self.NumberOfGPWeight = 5/9
    def GetIntegrationPoints(self):
        if self.NumberOfGPWeight == 5/9:
            return [-np.sqrt(3./5.), np.sqrt(3./5.)]
        if self.NumberOfGPWeight == 8/9:
            return [0]
    def GetIntegrationWeights(self):
        return [self.NumberOfGPWeight]
class Element1D:
    def __init__(self, E, A, nodes):
        self.E = E
        self.A = A
        self.nodes = nodes
        self.integrationType = Integration2GP()
    def GetB2Node(self, xi):
      return np.matrix([-0.5, 0.5])
    def GetN2Node(self, xi):
        return 0.5*np.matrix([1-xi, xi+1])
    def GetKe(self):
        Ke = [[0,0],[0,0]]
        Le = self.nodes[1].x - self.nodes[0].x
        for i in range(self.integrationType.NumberOfGP):
            xi = self.integrationType.GetIntegrationPoints()[i]
            wi = self.integrationType.GetIntegrationWeights()[i]
            B = self.GetB2Node(xi)
            Ke += self.E* self.A * B.T*B*wi*2/Le
        return Ke
    def GetFe(self, P):
        Fe = np.array([[0.0],[0.0]])
        Le = self.nodes[1].x-self.nodes[0].x
        for i in range(self.integrationType.NumberOfGP):
            xi = self.integrationType.GetIntegrationPoints()[i]
            wi = self.integrationType.GetIntegrationWeights()[i]
            N =  self.GetN2Node(xi)
            Fe += wi*N.T*P*Le/2
        return Fe

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
def displ_analy(x):
    L = 20.0
    E = 20.0
    A = 25.0
    P = 4.0
    u = (P/(E*A))*(L*x- 0.5*x**2)
    return u
#displ_analy(i*L/num_elems)
num_nodes = 5
L = 20.0


"""def main():
    L = 20.0
    num_elems = 4


    # Grafico Axis=X.Process_time
    list_clock = []
    list_x = []

#    for i in range(1,11):
#        process_time, error, displacement = bar(i)
#        list_displ = displ_i(i)
#        list_x.append(i)
#        list_clock.append(process_time)

#    plt.plot(list_x,list_clock)
#    plt.show()

    # Grafico displ_i.displacement_erro
    list_displ_error = []
    for i in range(1,3):
        displacement = bar(i)
        list_displ = displ_i(i)
        error = np.abs(displacement.T - list_displ.T)
        list_x.append(i)
        list_displ_error.append(error.sum()/error.size)
    print list_displ_error
    plt.plot(list_x, list_displ_error)
    plt.show()

main()"""
