#ITI1120
#Assinment 5
#Jannah Hossain, 8616189
#Jennifer Vo, 7277323
class Rectangle:
    'class that represents a rectangle in the plane'

    def __init__(self, bottom_left, top_right, color):
        ''' (Point,Point, colour) -> None
        initialize point coordinates to (point 1, point 2, colour)'''
        self.corner1 = bottom_left
        self.corner2 = top_right
        self.c = color

    def __str__(self):
        '''(Point)->tuple
        Returns a tuple with point 1, point 2 and the colour'''
        return "I am a {4} rectangle with bottom left corner at ({0},{1}) and top right corner at ({2},{3}).".format(self.corner1.x,self.corner1.y,self.corner2.x,self.corner2.y, self.c)
    
    def __repr__(self):
        '''(Point)->tuple
        Returns a tuple with point 1, point 2 and the colour'''
        return "Rectangle({0},{1},'{2}')".format(self.corner1,self.corner2, self.c)

    def __eq__(self,other):
        '''(Point)->tuple
        Returns a tuple with rectangle 1 and rectangle 2 are equal or not'''
        if other.corner1 == self.corner1 and other.corner2 == self.corner2 and other.c == self.c:
            return True
        else:
            return False
    
    def get_bottom_left(self):
        '''(Point)->tuple
        Returns a tuple with point 1'''
        return (self.corner1)
    
    def get_top_right(self):
        '''(Point)->tuple
        Returns a tuple with point 2'''
        return (self.corner2)

    def reset_color(self,dc):
        '''(Point)->None
        changes the colour'''
        self.c = dc

    def get_color(self):
        '''(Point)->tuple
        Returns a tuple with the colour'''
        return (self.c)
    
    def move(self,dx,dy):
        '''(Point,Point)->None
        Takes a new points and move the points by that new point'''
        #moves the x and y values
        self.corner1.x += dx
        self.corner2.x += dx
        self.corner1.y += dy
        self.corner2.y += dy

    def get_perimeter(self):
        '''(Point)->tuple
        Returns a tuple with the parameter of the rectangle'''
        #finds the diffrence
        q = self.corner2.x - self.corner1.x
        r = self.corner2.y - self.corner1.y
        #adds the diffrence then multiplies the total to determin the perimeter
        s = (q+r)*2
        print(s)
        
    def get_area(self):
        '''(Point)->tuple
        Returns a tuple with the area of the rectangle'''
        #finds the diffrence
        q = self.corner2.x - self.corner1.x
        r = self.corner2.y - self.corner1.y
        #multiplies the diffrence to determin the area
        s = (q*r)
        print(s)

    def contains(self,q,w):
        '''(Number,Number)-> Boolean
        Returns a Boolean value and determins if the point is present in the rectangle'''
        if q >= self.corner1.x and q <= self.corner2.x:
            if w >= self.corner1.y and w <= self.corner2.y:
                return True
            
    def intersects(self,other):
        '''(Point)->tuple
        Returns a tuple to determin if the rectangles intersect or not'''
        if other.corner1.x >= self.corner1.x and other.corner2.x <= self.corner2.x:
            if other.corner1.y >= self.corner1.y and other.corner2.y <= self.corner2.y or other.corner1.y <= self.corner1.y and other.corner2.y >= self.corner2.y:
                return True
            else:
                return False
        else:
            return False
        
    def inter(self,other):
        '''(Point)->tuple
        Returns a tuple to determin if the rectangles intersect or not'''
        return (other.corner2.x >= self.corner1.x and other.corner1.x <= self.corner2.x and other.corner2.y == self.corner1.y and other.corner1.y <= self.corner2.y)


class Canvas:
    'class that represents a canvas of rectangles in the plane'

    def __init__(self):
        ''' (Point) -> None
        initialize the canvas of rectangles'''
        self.h = []
        

    def __repr__(self):
        '''(Point)->tuple
        Returns a tuple with the list of rectangles in the canvas'''
        return "Canvas({0})".format(self.h)

    def __len__(self):
        '''(Point)->tuple
        Returns a tuple with the number of rectangles in the canvas'''
        return len(self.h)
        
    def add_one_rectangle(self,v):
        '''(Rectangle)->tuple
        Returns a tuple by adding a rectangles in the canvas'''
        self.h.append(v)

    def count_same_color(self,sc):
        '''(Colour)->tuple
        Returns a tuple by counting the colour of rectangles in the canvas that was entred'''
        f = 0
        for item in self.h:
            if item.c == sc:
                f += 1
        return f

    def total_perimeter(self):
        '''(Point)->tuple
        Returns a tuple with the total parameter of the canvas of rectangles'''
        p = 0
        for i in self.h:
            q = i.corner2.x - i.corner1.x
            r = i.corner2.y - i.corner1.y
            s = (q+r)*2
            p = s + p
        return p
    
    def min_enclosing_rectangle(self):
         '''(Point)->tuple
        Returns a tuple by determining the minimum enclosed area of the rectangles in the canvas'''
         a = self.h[0].corner1.x
         b = self.h[0].corner1.y
         c = self.h[0].corner2.x
         d = self.h[0].corner2.y
         for i in self.h:
             if i.corner1.x < a:
                 a = i.corner1.x
             if i.corner1.y < b:
                 b = i.corner1.y
             if i.corner2.x > c:
                 c = i.corner2.x
             if i.corner2.y > d:
                 d = i.corner2.y 
            
         return Rectangle(Point(a,b),Point(c,d),'red')

    def common_point(self):
        '''(Point)->tuple
        Returns a tuple by determining the common point of the rectangles in the canvas'''
        a = 1
        for i in range(0,len(self.h)):
             for j in range(1,len(self.h)):
                if self.h[i].inter(self.h[j]):
                    a = 0
                else:
                    a = a
        if a == 0:
            return True
        else:
            return False
           
class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    
