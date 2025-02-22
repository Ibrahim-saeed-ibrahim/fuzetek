class Point:
   
    
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
        
    
    def distance_to_origin(self):
        return ((self.x-0)**2 + (self.y-0)**2)**0.5
    
    def calculate_distance(self, other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
    
    def move(self, dx, dy):
        return Point( self.x + dx , self.y +dy)
        
    
    def __add__(self, other):
        return Point( self.x + other.x , self.y +other.y)
    
    def __eq__(self, other):
        return ( self.x == other.x and self.y == other.y)
    
    def __str__(self):
        return f"  x = {self.x} , y = {self.y}"
    
class ColoredPoint(Point):
    
    
    def __init__(self, x, y, color):
        self.x=x
        self.y=y
        self.color=color
    
    def __str__(self):
        """
        Override the string representation of the object.
        :return: A string describing the colored point.
        """
        return f"x is {self.x} y is {self.y} color is {self.color}"


p1=Point(5,2)
p2=Point(4,1)
p4=ColoredPoint(5,3,"black")
print (p4)