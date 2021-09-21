import pandas as pd

weatherData = pd.read_csv('decision_tree_writing\weather_play.csv')
print(weatherData.head())

class Node:
    def __init__(self):
        self.n = None
        self.left = None
        self.center = None
        self.right = None
        #other things

#directed graph implementation
#function to determine path as variable of node?

def giniImpurity(set, totalNum):
    #set of format [# in catg 1, # in catg 2, ..., # in catg n]
    giniImpurity = 1
    for category in set:
        giniImpurity -= (category/totalNum)**2

    return giniImpurity


def informationGain(numChildren):
    #pass parent to giniImpurity
    parentTotal = 0
    childrenTotalSum = 0
    avgChildrenTotal = 0

    for child in numChildren:
        #do gini impurity for each
        childrenTotalSum += giniImpurity()
    avgChildrenTotal = childrenTotalSum / numChildren

