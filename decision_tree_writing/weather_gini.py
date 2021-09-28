from tree import Tree
from tree import Node
from tree import Data
import csv

'''
Reading in the data
'''
def readIn(file):
    attributes = []
    days = {}

    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        attributes = next(csvreader)
        attributes.remove("Day")
        attributes.remove("Play?")

        for row in csvreader:
            day = int(row.pop(0))
            #play = 1 if row.pop(-1)=="Yes" else 0
            play = row.pop(-1)
            days[day] = (row, play)

    return days, attributes

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
def attributeValues(attributes, days):
    atrbValues = {}
    #go through each row and identify values for attribute
    #put in dict with attribute as key (i.e. Weather, Temp, etc) with
    #  values as value (i.e sunny/cloud/rainy, hot/mild, etc)
    for atrb in attributes:
        index = attributes.index(atrb)
        allValues = [days.get(day)[0][index] for day in days]
        atrbValues[atrb] = sorted(set(allValues))

    return atrbValues


def split(nodeToSplit, attributes, atrbValues):
    #identifies splits
    #calculates info gain for each
    #identifies best and splits on that
    informationGain = 0
    #for attribute in atrbValues
    

"""
The math things
General idea?: find all potential splits -> run information gain on each -> info gain calls gini impurity
"""

#general idea - can customize to data structures later
#parameters: parent set, sets of children?
def informationGain(parent):
    #EDIT pass parent to giniImpurity
    parentGini = giniImpurity(parent)
    #initialize these variables
    childrenTotalSum = 0
    avgChildrenTotal = 0

    numChildren = (2 if parent.center == None else 3)

    for child in numChildren:
        #do gini impurity for each
        childrenTotalSum += giniImpurity()
    avgChildrenTotal = childrenTotalSum / numChildren

    
#calculates the gini impurity for a single node
def giniImpurity(datanode):
    totalNum = datanode.getNumDays()

    play = []
    yesplay = 0
    noplay = 0
    
    for day in datanode.getDays():
        if (datanode.getDays().get(day)[1] == 1):
            yesplay += 1
        else:
            noplay += 1

    print("Yes: ", yesplay , ", No: " , noplay, ", total days: ", totalNum)
        
    giniImpurity = 1 - (yesplay/totalNum)**2 - (noplay/totalNum)**2
    print(giniImpurity)
    
    return giniImpurity



def main():
    print("Starting decision tree making")
    days, attributes = readIn('weather_play.csv')

    #print('Attribute names are: ' + ', '.join(attribute for attribute in attributes))
    #print(days)
    #print('\n')

    
    ourTree = Tree()
    root = Node(days, attributes)
    ourTree.root = root

    #print(ourTree.root)
    giniImpurity(ourTree.getRoot())    
    atrbValues = attributeValues(attributes, days)
    print(atrbValues)
    print(ourTree.getRoot().getDays())
    


if __name__ == "__main__":
    main()



