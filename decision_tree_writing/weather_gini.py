'''
To make general:
    - remove references to "play" as outcome
    - generalize outcome results (could be more than 2, and not just yes/no)
    - generalize reading in of data
    - deal with missing data
'''


from tree import Tree
from tree import Node
import csv

#attributes = []
#atrbValues = {}

'''
Reading in the data
'''
def readIn(file):
    attributes = []
    data = {}

    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        attributes = next(csvreader)
        attributes.remove("Day")
        attributes.remove("class")

        count = 1
        for row in csvreader:
            row.pop(0)
            outcome = row.pop(-1)
            data[count] = (row, outcome)
            count += 1

    return data, attributes

"""
General outline of a decision tree algorithm:
- identify potential splits
- find split with greatest information gain
- do that
- repeat until all purely classified or max depth
"""

#goal classification
classificationName = "Play?"

#identify all values of attributes
def attributeValues(attributes, data):
    atrbValues = {}
    #go through each row and identify values for attribute
    #put in dict with attribute as key (i.e. Weather, Temp, etc) with
    #  values as value (i.e sunny/cloud/rainy, hot/mild, etc)
    for atrb in attributes:
        index = attributes.index(atrb)
        allValues = [data.get(item)[0][index] for item in data]
        atrbValues[atrb] = sorted(set(allValues))

    return atrbValues

def outcomeValues(data):
    outcomeValues = [data.get(item)[1] for item in data]
    outcomeValues = sorted(set(outcomeValues))
    return outcomeValues


def testSplit(nodeToSplit, atrbValues):
    '''identifies splits
       calculates info gain for each
       identifies best and splits on that'''
    informationGains = {}

    for atrbName in atrbValues:
        location = attributes.index(atrbName)
        
        #fills a set for each attribute value with the number of yes plays and no plays
        values = {}
        for value in atrbValues.get(atrbName):
            values[value] = [0,0] #[no, yes]
        values['Total'] = [0,0]

        #calculates information gain
        split = {}
        for item, value in nodeToSplit.getData().items():
            outcome = value[1]

            attributeValue = value[0][location]
            split[item] = attributeValue
            if outcome == outcomeValues[0]:
                values[attributeValue][0] += 1
                values['Total'][0] += 1
            elif outcome == outcomeValues[1]:
                values[attributeValue][1] += 1
                values['Total'][1] += 1

        infoGain = informationGainSet(values)
        informationGains[atrbName] = infoGain
    
    #identifies the split with the most information gain 
    maxGain = max(informationGains.items(), key=lambda x: x[1])

    return maxGain
    
def makeSplit(nodeToSplit, splitOn, atrbValues):
    location = attributes.index(splitOn)

    #fills a dict with the attribute values and the days with that value
    splits = {}
    for atrbValue in atrbValues[splitOn]:
        splits[atrbValue] = {}
    for item, value in nodeToSplit.getData().items():
        attributeValue = value[0][location]
        splits[attributeValue][item] = value        

    #remove attributeValues with no days in them
    splits2 = {atrbValue: value for atrbValue, value in splits.items() if value != {}}

    #fill children of current node with splits
    #count = 1
    for atrbValue, value in splits2.items():
        child = Node(value, nodeToSplit.getLevel()+1)
        child.setSplitOn((splitOn, atrbValue))
        nodeToSplit.addChild(child)
        '''if (count == 1):
            nodeToSplit.setLeft(Node(value, nodeToSplit.getLevel()+1))
            nodeToSplit.getLeft().setSplitOn((splitOn, atrbValue))
        elif (count == 2):
            nodeToSplit.setRight(Node(value, nodeToSplit.getLevel()+1))
            nodeToSplit.getRight().setSplitOn((splitOn, atrbValue))
        elif (count == 3):
            nodeToSplit.setCenter(Node(value, nodeToSplit.getLevel()+1))  
            nodeToSplit.getCenter().setSplitOn((splitOn, atrbValue))      
        count += 1'''
    return


"""
The math things
General idea?: find all potential splits -> run information gain on each -> info gain calls gini impurity
"""

def informationGainSet(valueSet):
    #gets parent gini impurity
    parentGini = giniImpuritySet(valueSet['Total'])
    #initialize these variables
    childrenTotalSum = 0
    avgChildrenTotal = 0

    valueSet.pop("Total")
    for child in valueSet:
        #do gini impurity for each
        if (valueSet[child][0] + valueSet[child][1]) != 0:
            childrenTotalSum += giniImpuritySet(valueSet[child])
    avgChildrenTotal = childrenTotalSum / len(valueSet)
    return parentGini - avgChildrenTotal


#calculates the gini impurity for a single node
def giniImpuritySet(set):
    #set of form [no, yes]
    totalNum = set[0] + set[1]
    print(totalNum)
    giniImpurity = 1 - (set[0]/totalNum)**2 - (set[1]/totalNum)**2
    
    return giniImpurity


'''Checks all possible values to split on and makes the best one'''
def fillLevel(node, atrbValues):
    if(node == None):
        return

    splitOn, infoGain = testSplit(node, atrbValues)

    if(infoGain == 0.0):
        return

    makeSplit(node, splitOn, atrbValues)

    atrbValues.pop(splitOn)
    #if no new attributes to split on, return as leaf node
    if atrbValues == {}:
        return
    
    for child in node.getChildren():
        fillLevel(child, atrbValues)
    #fillLevel(node.getRight(), atrbValues)
    #fillLevel(node.getCenter(), atrbValues)

def splitdata(data, start, range):
    return data[start:range]

    
def main():
    print("Starting decision tree making")
    global attributes
    #data, attributes = readIn('agaricus-lepiota.csv')
    data, attributes = readIn('weather_play.csv')
    global outcomeValues
    outcomeValues = outcomeValues(data)
    #print(data)

    ourTree = Tree()
    root = Node(data)
    ourTree.setRoot(root)
    ourTree.getRoot().setSplitOn("Root")

    atrbValues = attributeValues(attributes, data)
    #print(atrbValues)
    #print(attributes)

    fillLevel(ourTree.getRoot(), atrbValues)
    print()
    ourTree.printTree()
    


if __name__ == "__main__":
    main()
