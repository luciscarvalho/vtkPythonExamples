class Integration3GP:
    """ Gaussian Quadrature for 3 points """
    def __init___(self):
        """Number of Gauss Points and Weight Function"""
        self.NumberOfGP = 3
        self.NumberOfGPWeight = 5/9
    def GetIntegrationPoints(self):
        """ Gaussian Quadrature ~~~ see more in https://en.wikipedia.org/wiki/Gaussian_quadrature"""
        if self.NumberOfGPWeight == 5/9:
            return [-np.sqrt(3./5.), np.sqrt(3./5.)]
        if self.NumberOfGPWeight == 8/9:
            return [0]
    def GetIntegrationWeights(self):
        """ Weight function ~~~ see more in https://en.wikipedia.org/wiki/Gaussian_quadrature"""
        return [self.NumberOfGPWeight]
