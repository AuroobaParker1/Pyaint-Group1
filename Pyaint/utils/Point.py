class Point:
    #Cordinates
    x =0
    y=0

    #Constructor
    def __init__(self,x,y):
        self.x=x
        self.y=y

    #Get Cordinates
    def Get(self):
        return(self.x,self.y)
