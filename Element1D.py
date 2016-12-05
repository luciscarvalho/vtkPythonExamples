import numpy as np
from Integration2GP import Integration2GP


class Element1D:
    """# E, A, nodes, Ke, Fe, shape functions"""
    def __init__(self, E, A, nodes):
        """Axis x and u is axis Y, displacement"""
        self.E = E
        self.A = A
        self.nodes = nodes
        self.integrationType = Integration2GP()
    def GetB2Node(self, xi):
        """ Limits of shape functions"""
        return np.matrix([-0.5, 0.5])
    def GetN2Node(self, xi):
        """ Shape Function """
        return 0.5*np.matrix([1-xi, xi+1])
    def GetKe(self):
        """Local Young's Modulus """
        Ke = [[0,0],[0,0]]
        Le = self.nodes[1].x - self.nodes[0].x
        for i in range(self.integrationType.NumberOfGP):
            xi = self.integrationType.GetIntegrationPoints()[i]
            wi = self.integrationType.GetIntegrationWeights()[i]
            B = self.GetB2Node(xi)
            Ke += self.E* self.A * B.T*B*wi*2/Le
        return Ke

    def GetFe(self, P):
        """Local Force """
        Fe = np.array([[0.0],[0.0]])
        Le = self.nodes[1].x-self.nodes[0].x
        for i in range(self.integrationType.NumberOfGP):
            xi = self.integrationType.GetIntegrationPoints()[i]
            wi = self.integrationType.GetIntegrationWeights()[i]
            N =  self.GetN2Node(xi)
            Fe += wi*N.T*P*Le/2
        return Fe
