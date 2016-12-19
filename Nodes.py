"""A module for finite element nodes in various dimensions."""

class Node1D(object):
    """A Node for one dimensional finite element code"""
    def __init__(self, x):
        """Axis x and u is axis Y (displacement)"""
        self.x = x
        self.u = 0
class Node2D(object):
    """A node for two dimensional finite element code"""
    def __init__(self,coordinate):
        """Axis x and y and values of the displacement"""
        self.coordinate = coordinate
