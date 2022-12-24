from .settings import *
from .Segment import Segment
from .Point import Point

class Square:
    # Essential Variables
    selected=True
    pivot_X=0
    pivot_Y=0
    width=0
    height=0
    check=0
    rect=pygame.Rect(0, 0, 1, 1)
    color=(0,0,0)
    thickness=0

    # Constructor
    def __init__(self,left,right,width,d,thickness):
        # assigns values to essential variables
        self.color=d
        self.pivot_X=left
        self.pivot_Y=right
        self.width=width
        self.height = width
        cordinates = []
        self.thickness=thickness

    # Draw Function
    def Draw(self,win):
        if(int(self.width<0)):
            rect = pygame.Rect(self.pivot_X+int(self.width), self.pivot_Y+int(self.width), abs(int(self.width)), abs(int(self.width)))
        else:rect = pygame.Rect(self.pivot_X, self.pivot_Y, (int(self.width)), (int(self.width)))
        self.cordinates=[(rect.left,rect.top),(rect.left,rect.bottom),(rect.right,rect.bottom),(rect.right,rect.top)]

        self.rect=pygame.draw.rect(win, self.color, rect, width=self.thickness)

    # Changes Width Of Shape
    def changewidth(self,width):
        if ((self.pivot_X + (width + self.width)) <= 600 and (self.pivot_X + (width + self.width)) >= 0) and (self.pivot_Y + (width + self.width)) <= 600 and (self.pivot_Y + (width + self.width)) >= 0 :
            self.width += width
            self.height += width

    # Changes Height Of Shape
    def changeheight(self,height):
        print()

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
