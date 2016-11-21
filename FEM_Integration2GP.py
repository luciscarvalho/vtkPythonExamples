class Integration2GP:
# Gaussian Quadrature for 2 points
    def __init__(self):
# Number of Gaussian Point
        self.NumberOfGP = 2
    def GetIntegrationPoints(self):
# Gaussian Quadrature ~~~ see more in https://en.wikipedia.org/wiki/Gaussian_quadrature
        return [-np.sqrt(1./3.), np.sqrt(1./3.)]
    def GetIntegrationWeights(self):
# Weight function ~~~ see more in https://en.wikipedia.org/wiki/Gaussian_quadrature
        return [1, 1]
