import math
from operator import itemgetter
from .settings import *
from .Point import Point
from .Segment import Segment


class Polygon:
    # Essential Variables
    selected=True
    Initial=Point(0,0)
    radius=1
    angle=0
    sides=0
    pivot_X = 0
    pivot_Y = 0
    max_X=0
    max_Y = 0
    min_X=0
    min_Y=0
    width=1000
    thickness=0
    cordinates=[]
    check = 0
    color=(0,0,0)
    rect=None

    # Constructor
    def __init__(self,point1,num,d,thickness):
        # assigns values to essential variables
        self.cordinates=[]
        self.sides=num
        self.Initial=point1
        self.pivot_X=self.Initial.x
        self.pivot_Y=self.Initial.y
        self.color=d
        self.angle = 2 * math.pi / num
        self.thickness=thickness

        #Generating Cordinates Of Polygon Using Number Of Sides
        for i in range (num):
            x = (self.pivot_X + self.radius * math.sin(i * self.angle));
            y = (self.pivot_Y + self.radius * math.cos(i * self.angle));
            self.cordinates.append((x,y))

    # Draw Function
    def Draw(self,win):
        self.rect=pygame.draw.polygon(win, self.color, self.cordinates, width=self.thickness)

    # Changes Width Of Shape
    def changewidth(self,width):
        if ((self.Initial.x + (width + self.radius)) <= 600 and (self.Initial.x - (width + self.radius)) >= 0) and (self.Initial.y + (width + self.radius)) <= 600 and (self.Initial.y - (width + self.radius) >= 0) and ((self.Initial.x - (width + self.radius)) <= 600 and (self.Initial.x + (width + self.radius)) >= 0) and (self.Initial.y - (width + self.radius)) <= 600 and (self.Initial.y + (width + self.radius) >= 0):
            self.radius += width
        self.cordinates=[]

        for i in range (self.sides):
            x = self.Initial.x + self.radius * math.sin(i * self.angle);
            y = self.Initial.y + self.radius * math.cos(i * self.angle);
            self.cordinates.append((x,y))
            self.max_Y = max(self.cordinates, key=itemgetter(1))[1]
            self.max_X = max(self.cordinates, key=itemgetter(0))[0]
            self.min_X = min(self.cordinates, key=itemgetter(0))[0]
            self.min_Y = min(self.cordinates, key=itemgetter(1))[1]

    # Changes Height Of Shape
    def changeheight(self,height):
        print()

    # Changes Horizontal Position
    def change_position_x(self,change):
        self.Initial.x+=change
        self.cordinates = []
        for i in range(self.sides):
            x = self.Initial.x + self.radius * math.sin(i * self.angle);
            y = self.Initial.y + self.radius * math.cos(i * self.angle);
            self.cordinates.append((x, y))

    # Changes Vertical Position
    def change_position_y(self,change):
        self.Initial.y+=change
        self.cordinates = []
        for i in range(self.sides):
            x = self.Initial.x + self.radius * math.sin(i * self.angle);
            y = self.Initial.y + self.radius * math.cos(i * self.angle);
            self.cordinates.append((x, y))

    # Finds Minimum X Cordinate Of Shape
    def MinimumX(self):
        minimum=1000
        for x in self.cordinates:
            if x[0]<minimum: minimum=x[0]
        return minimum

    # Finds Maximum X Cordinate Of Shape
    def MaximumX(self):
        maximum=-1000
        for x in self.cordinates:
            if x[0]>maximum: maximum=x[0]
        return maximum

    # Finds Minimum Y Cordinate Of Shape
    def MinimumY(self):
        minimum = 1000
        for x in self.cordinates:
            if x[1] < minimum: minimum = x[1]
        return minimum

    # Finds Maximum Y Cordinate Of Shape
    def MaximumY(self):
        maximum = -1000
        for x in self.cordinates:
            if x[1] > maximum: maximum = x[1]
        return maximum

    # Gets All Edges Of Shape
    def GetEdges(self):
        edges = []
        for i in range(len(self.cordinates)):
            if i == len(self.cordinates) - 1:
                i2 = 0
            else:
                i2 = i + 1
            edges.append(Segment(Point(self.cordinates[i][0],self.cordinates[i][1]), Point(self.cordinates[i2][0],self.cordinates[i2][1])))
        return edges


