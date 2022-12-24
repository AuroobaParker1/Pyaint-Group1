from .settings import *
from .Segment import Segment
from .Point import Point

class Rectangle:
    # Essential Variables
    selected=True
    pivot_X=0
    pivot_Y=0
    color=(0,0,0)
    width=0
    rect=None
    check = 0
    height=0
    cordinates = []
    thickness=0

    # Constructor
    def __init__(self,left,right,width,height,d,thickness):
        # assigns values to essential variables
        self.pivot_X=left
        self.pivot_Y=right
        self.width=width
        self.height=height
        self.color=d
        self.thickness=thickness

    # Draw Function
    def Draw(self,win):
        if (int(self.width) < 0 and int(self.height) < 0):
            rect = pygame.Rect(self.pivot_X + int(self.width), self.pivot_Y + int(self.height), abs(int(self.width)),
                               abs(int(self.height)))

        elif (int(self.width) < 0 and int(self.height) > 0):
            rect = pygame.Rect(self.pivot_X + int(self.width), self.pivot_Y, abs(int(self.width)),
                               abs(int(self.height)))

        elif (int(self.width) > 0 and int(self.height) < 0):
            rect = pygame.Rect(self.pivot_X, self.pivot_Y + int(self.height), abs(int(self.width)),
                               abs(int(self.height)))

        else:
            rect = pygame.Rect(self.pivot_X, self.pivot_Y, abs(int(self.width)), abs(int(self.height)))
        self.cordinates=[(rect.left,rect.top),(rect.left,rect.bottom),(rect.right,rect.bottom),(rect.right,rect.top)]
        self.rect=pygame.draw.rect(win, self.color, rect,  width=self.thickness)

    #Draw Shape Selection Rectangle
    def Draw_Selected(self, win):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
        rect = pygame.Rect(self.pivot_X, self.pivot_Y, int(self.width), int(self.height))
        img = pygame.image.load("rotate.png").convert_alpha()
        img = pygame.transform.scale(img, (20, 20))
        win.blit(img, (self.pivot_X + self.width / 2 - 5, self.pivot_Y - 20))

        img2 = pygame.image.load("download.png").convert_alpha()
        img2 = pygame.transform.scale(img2, (20, 20))
        win.blit(img2, (self.pivot_X + self.width / 2 - 5, self.pivot_Y + self.height + 10))

        rect2 = pygame.Rect(self.pivot_X, self.pivot_Y, 10, 10)
        rect3 = pygame.Rect(self.pivot_X, self.pivot_Y + self.height - 5, 10, 10)
        rect4 = pygame.Rect(self.pivot_X + self.width - 5, self.pivot_Y, 10, 10)
        rect5 = pygame.Rect(self.pivot_X + self.width - 5, self.pivot_Y + self.height - 5, 10, 10)

        pygame.draw.rect(win, (0, 0, 0), rect2, 2, 3)
        pygame.draw.rect(win, (0, 0, 0), rect3, 2, 3)
        pygame.draw.rect(win, (0, 0, 0), rect4, 2, 3)
        pygame.draw.rect(win, (0, 0, 0), rect5, 2, 3)
        pygame.draw.rect(win, (197, 198, 208), rect, 2, 3)


        return rect2,rect3,rect4,rect5

    # Changes Width Of Shape
    def changewidth(self, width):
        if ((self.pivot_X + (width + self.width)) <= 600 and (self.pivot_X + (width + self.width)) >= 0):
            self.width += width

    # Changes Height Of Shape
    def changeheight(self, height):
        if ((self.pivot_Y + (height + self.height)) <= 600 and (self.pivot_Y + (height + self.height)) >= 0) :
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
