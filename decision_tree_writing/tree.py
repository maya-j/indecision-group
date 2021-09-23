#implementation of a tree for the decision trees

#data for each node
class Data:
    def __init__(self, days, attributes):
        self.days = days
        self.attributes = attributes

#one node of the decision tree
class Node:
    def __init__(self, days, attributes, level = 0):
        self.data = Data(days, attributes)
        self.level = level
        self.left = None
        self.center = None
        self.right = None
        #could be good to know?
        self.attributeSplitOn = None
    
    def getData(self):
        return self.data

    def setLeft(self, node):
        self.left = node
    
    def setCenter(self, node):
        self.center = node

    def setRight(self, node):
        self.right = node

#tree to hold the decision tree
class Tree:
    def __init__(self, root = None):
        self.root = root
        self.totalLevels = 0

    def getRoot(self):
        return self.root

    #questions:
        # how to increase level - add an add function to tree