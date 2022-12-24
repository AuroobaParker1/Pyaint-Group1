from .settings import *
from .Point import Point
from .Segment import Segment

class Triangle:
    # Essential Variables
    selected=True
    Initial=Point(0,0)
    color=(0,0,0)
    width=0
    check=0
    height=0
    pivot_X=0
    pivot_Y=0
    rect=None
    cordinates = []
    thickness=0

    # Constructor
    def __init__(self,point1,width,height,d,thickness):
        # assigns values to essential variables
        self.height=height
        self.width=width
        self.Initial=point1
        self.pivot_X=self.Initial.x
        self.pivot_Y=self.Initial.y
        self.color=d
        self.thickness=thickness


    # Draw Function
    def Draw(self,win):
        self.cordinates=[(self.pivot_X + self.width, self.pivot_Y), (self.pivot_X + (self.width / 2), self.pivot_Y + self.height), (self.pivot_X, self.pivot_Y,)]
        self.rect=pygame.draw.polygon(win, self.color, ((self.pivot_X + self.width, self.pivot_Y), (self.pivot_X + (self.width / 2), self.pivot_Y + self.height), (self.pivot_X, self.pivot_Y,)), width=self.thickness)

    # Changes Width Of Shape
    def changewidth(self,width):
        if((self.pivot_X+(width+self.width))<=600 and (self.pivot_X-(width+self.width))>=0 and (self.pivot_X-(width+self.width))<=600 and (self.pivot_X+(width+self.width))>=0):
            self.width+=width

    # Changes Height Of Shape
    def changeheight(self,height):
        if ((self.pivot_Y + (height + self.height)) <= 600 and (self.pivot_Y - (height + self.height)) >= 0 and (self.pivot_Y - (height + self.height)) <= 600 and (self.pivot_Y + (height + self.height)) >= 0):
            self.height += height

    # Changes Horizontal Position
    def change_position_x(self,change):
        self.pivot_X+=change

    # Changes Vertical Position
    def change_position_y(self,change):
        self.pivot_Y+=change


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


