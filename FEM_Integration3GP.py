import numpy as np
import matplotlib.pyplot as plt
import time

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
