import pandas as pd
import csv

'''
READING IN THE DATA
'''
#weatherData = pd.read_csv('decision_tree_writing\weather_play.csv')
#print(weatherData.head())
filename = 'decision_tree_writing\weather_play.csv'
attributes = []
days = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    attributes = next(csvreader)
    for row in csvreader:
        days.append(row)

#print('Attribute names are: ' + ', '.join(attribute for attribute in attributes))
#print(days[2])

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
        allValues = [day[index] for day in days]
        atrbValues[atrb] = sorted(set(allValues))

    return atrbValues

def split(parentSet, attribute):
    informationGain = 0
    

"""
The math things
General idea?: find all potential splits -> run information gain on each -> info gain calls gini impurity
"""

#general idea - can customize to data structures later
#parameters: parent set, sets of children?
def informationGain(numChildren, set):
    #EDIT pass parent to giniImpurity
    parentTotal = 0
    #initialize these variables
    childrenTotalSum = 0
    avgChildrenTotal = 0

    for child in numChildren:
        #do gini impurity for each
        childrenTotalSum += giniImpurity()
    avgChildrenTotal = childrenTotalSum / numChildren

#general idea - can customize to data structures later
def giniImpurity(set, totalNum):
    #set of format [# in catg 1, # in catg 2, ..., # in catg n]
    giniImpurity = 1
    for category in set:
        giniImpurity -= (category/totalNum)**2

    return giniImpurity



#---------#

#need? maybe not, but this is how trees are displaced conceptually in the tutorials
class Node:
    def __init__(self):
        self.n = None
        self.left = None
        self.center = None
        self.right = None
        #other things
    #directed graph implementation?
    #function to determine path as variable of node?