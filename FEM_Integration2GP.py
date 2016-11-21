import numpy as np
import matplotlib.pyplot as plt
import time

class Integration2GP:
    def __init__(self):
        self.NumberOfGP = 2
    def GetIntegrationPoints(self):
        return [-np.sqrt(1./3.), np.sqrt(1./3.)]
    def GetIntegrationWeights(self):
        return [1, 1]
