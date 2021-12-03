#Chea, Cohen, Gao, Hiciano
#CS5800 Spring 2021 Final Project
#Program that matches lists of 2D coordinates by comparing 
#the areas of the triangles formed by sets of three Points.

from itertools import combinations
import sys

class Point():
    '''
    A Point in a given triangle represented by its x and y coordinate values.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

def triangleGeneration(arr):
    '''
    Traverses list of triangles, arr,  and computes area of each triangle.
    Returns sorted list of the computed triangle areas.
    '''
    #generate possible combinations of 3 from arr (all possible triangles) 
    comb = list(combinations(arr, 3))

    #will contain all computed areas at end of for loop
    triAreas = []

    for tri in comb:
        area = triangleArea(tri)
        #append newly generated triangle to list of tris
        triAreas.append(area)
    
    #sort and return list of triangle areas
    return sorted(triAreas)


def triangleArea(vertices):
    '''
    Helper: Calculates and returns area of a triangle, defined by the vertices parameters.
    '''
    sum1 = 0
    sum2 = 0

    for i in range(0,2):
        sum1 = sum1 + vertices[i].getX() * vertices[i+1].getY()
        sum2 = sum2 + vertices[i].getY() * vertices[i+1].getX()

    #Add xn.y1
    sum1 = sum1 + vertices[3-1].getX() *vertices[0].getY()
    #Add x1.yn
    sum2 = sum2 + vertices[0].getX()*vertices[3-1].getY()

    area = abs(sum1 - sum2) / 2

    return area


def matchTriangle(newTriAreas, ogTriAreas):
    diff = 0
    for i in range(len(newTriAreas)):
        diff += abs(newTriAreas[i] - ogTriAreas[i])

    return diff

#helper
def compareImages(newImage, library):
    newTriangles = triangleGeneration(newImage)

    matches = []
    for img in library:
        ogTriangles = triangleGeneration(img)
        diff = matchTriangle(newTriangles, ogTriangles)
        matches.append(diff)

    print(matches)


#driver code
if __name__ == '__main__':
    #sample lists of triangle coordinate points
    image = [Point(1, 6),
           Point(1, 2),
           Point(7, 6),
           Point(4, 5),
           Point(2, 4),
           Point(3, 2),
           Point(0, 4),
           Point(5, 2),
           Point(6, 4),
           Point(8, 2)
           ]
    image1 = [Point(1, 6),
            Point(1, 2),
            Point(7, 6),
            Point(4, 5),
            Point(2, 4),
            Point(3, 2),
            Point(0, 4),
            Point(5, 2),
            Point(6, 4),
            Point(8, 2)
            ]

    image2 = [Point(1, 9),
             Point(1, 2),
             Point(7, 6),
             Point(4, 5),
             Point(2, 4),
             Point(3, 2),
             Point(0, 4),
             Point(5, 2),
             Point(6, 4),
             Point(8, 2)
             ]

    image3 = [Point(1, 9),
             Point(1, 4),
             Point(7, 6),
             Point(4, 5),
             Point(5, 4),
             Point(3, 2),
             Point(0, 4),
             Point(8, 2),
             Point(6, 4),
             Point(8, 2)
             ]

    image4 = [Point(1, 5), Point(6, 5), Point(4, 9),
             Point(0, -6), Point(9, 3), Point(5, 5),
             Point(1, 9), Point(1, -5), Point(0, 5),
             Point(2, 7)]

    library = [image1, image3, image4, image2]

    compareImages(image, library)
