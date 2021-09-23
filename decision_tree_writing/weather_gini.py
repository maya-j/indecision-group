import tree
import csv

'''
Reading in the data
'''
def readIn(file):
    #weatherData = pd.read_csv(file)
    #print(weatherData.head())
    attributes = []
    days = []

    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        attributes = next(csvreader)
        for row in csvreader:
            days.append(row)

    #print('Attribute names are: ' + ', '.join(attribute for attribute in attributes))
    #print(days[0])

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



def main():
    print("Starting decision tree making")
    readIn('decision_tree_writing\weather_play.csv')


if __name__ == "__main__":
    main()

