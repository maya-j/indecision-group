#implementation of a tree for the decision trees

#one node of the decision tree
class Node:
    def __init__(self, data, level = 0):
        self.data = data
        self.level = level
        self.children = []
        self.numChildren = 0
        self.splitOn = None
        #could be good to know?
        self.attributeSplitOn = None

    def getData(self):
        return self.data

    def getNumData(self):
        return len(self.data)

    def addChild(self, node):
        self.children.append(node)
        self.numChildren += 1

    def getChildren(self):
        return self.children

    def getChildAt(self, position):
        return self.children[position]

    def getNumChildren(self):
        return self.numChildren
    
    def getLevel(self):
        return self.level

    def getSplitOn(self):
        return self.splitOn

    def setSplitOn(self, split):
        self.splitOn = split

    def __str__(self):
        return "Level " + str(self.level) + ", Split on: " + str(self.splitOn) + " - Days: " + str(self.data.keys())



#tree to hold the decision tree
class Tree:
    def __init__(self, root = None):
        self.root = root
        self.totalLevels = 0

    def getRoot(self):
        return self.root

    def setRoot(self, root):
        self.root = root

    def printHelper(self, node):
        if node == None:
            return
        for i in range (node.getLevel()):
            print("\t", end = "")
        print(node)
        for child in node.getChildren():
            self.printHelper(child)
    
    def printTree(self):
        self.printHelper(self.root)


    #questions:
        # how to increase level - add an add function to tree

    """this method is called in the function when creating 
       a level and updates the variable totalLevel
    """
    def levelIncrease(self):
        self.totalLevels += 1
