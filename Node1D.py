class Node1D:
    """A Node for one dimensional finite element code"""
    def __init__(self, x):
        # Axis x and u is axis Y (displacement)
        self.x = x
        self.u = 0
