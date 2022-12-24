from .settings import *
from .Rectangle import Rectangle
from .Square import Square
from .Triangle import Triangle
from .Point import Point
from.Polygon import Polygon
from .Diamond import Diamond
from .Star import Star

#Factory For Creating All Shapes
class ShapeFactory:

    #Creates Shapes
    def Create(self,name,d):
        #Creates Rectangle
        if name == "Rectangle":
            rectangle_left = int(pygame.mouse.get_pos()[0]) - 1
            rectangle_right = int(pygame.mouse.get_pos()[1]) - 1
            rect= Rectangle(rectangle_left,rectangle_right,1,1,d,3)
            return rect
        # Creates Square
        if name == "Square":
            rectangle_left = int(pygame.mouse.get_pos()[0]) - 1
            rectangle_right = int(pygame.mouse.get_pos()[1]) - 1
            rect= Square(rectangle_left,rectangle_right,1,d,3)
            return rect
        # Creates Triangle
        if name == "Triangle":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            triangle= Triangle(Point1,1,1,d,3)
            return triangle
        # Creates Diamond
        if name == "Diamond":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            diamond= Diamond(Point1,1,1,d,3)
            return diamond
        # Creates Star
        if name == "Star":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Star(Point1,d)
            return shape
        # Creates 5 sided Polygon
        if name == "5gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,5,d,3)
            return shape
        # Creates 6 sided Polygon
        if name == "6gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,6,d,3)
            return shape
        # Creates 7 sided Polygon
        if name == "7gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,7,d,3)
            return shape
        # Creates 8 sided Polygon
        if name == "8gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,8,d,3)
            return shape
        # Creates 9 sided Polygon
        if name == "9gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,9,d,3)
            return shape
        # Creates 10 sided Polygon
        if name == "10gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,10,d,3)
            return shape
        # Creates 11 sided Polygon
        if name == "11gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,11,d,3)
            return shape
        # Creates 12 sided Polygon
        if name == "12gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,12,d,3)
            return shape
        # Creates 13 sided Polygon
        if name == "13gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,13,d,3)
            return shape
        # Creates 14 sided Polygon
        if name == "14gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,14,d,3)
            return shape
        # Creates 15 sided Polygon
        if name == "15gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,15,d,3)
            return shape
        # Creates 16 sided Polygon
        if name == "16gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,16,d,3)
            return shape
        # Creates 17 sided Polygon
        if name == "17gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,17,d,3)
            return shape
        # Creates 18 sided Polygon
        if name == "18gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,18,d,3)
            return shape
        # Creates 19 sided Polygon
        if name == "19gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,19,d,3)
            return shape
        # Creates 20 sided Polygon
        if name == "20gon":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
            shape= Polygon(Point1,20,d,3)
            return shape
        # Creates Symmetric Triangle
        if name == "STriangle":
            Point1 = (Point(int(pygame.mouse.get_pos()[0]), int(pygame.mouse.get_pos()[1])))
            shape = Polygon(Point1, 3,d,3)
            return shape

    #Creates A selected Shape
    def create_selected(self,x,y,width,height,d):
        rect = Rectangle(x, y, width, height,d)
        return rect
