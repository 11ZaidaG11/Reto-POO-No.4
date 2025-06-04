import math


class Point:
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y

    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y

    def reset(self):
        self.x = 0
        self.y = 0

class Line():
    def __init__(self, start:Point, end:Point):
        self.start = start
        self.end = end

    def compute_length(self)-> float: # √(x2-x1)^2 + (y2-y1)^2
        l_dx = (self.end.x - self.start.x)**2
        l_dy = (self.end.y - self.start.y)**2
        return math.sqrt(l_dx + l_dy)
    
    def compute_slope(self)-> float:
        m_dy = self.end.y - self.start.y
        m_dx = self.end.x - self.start.x
        if m_dx == 0:
            return None
        return m_dy / m_dx
        
    def compute_horizontal_cross(self)-> bool:
        case_1 = self.start.y > 0 and self.end.y < 0
        case_2 = self.start.y < 0 and self.end.y > 0
        return case_1 or case_2

    def compute_vertical_cross(self)-> bool:
        case_1 = self.start.x > 0 and self.end.x < 0
        case_2 = self.start.x < 0 and self.end.x > 0
        return case_1 or case_2

class Rectangle():
    def __init__(self, width:float, heigth:float, center:Point):
        self.width = width
        self.heigth = heigth
        self.center = center

    def compute_area(self):
        return self.width * self.heigth
    
    def compute_perimeter(self):
        return 2*self.width + 2*self.heigth
    
    def bottom_left(self)-> Point:
        bl_x = self.center.x - (self.width/2)
        bl_y = self.center.y - (self.heigth/2)
        bl = Point(bl_x, bl_y)
        return bl
    
    def bottom_rigth(self)-> Point:
        br_x = self.center.x + (self.width/2)
        br_y = self.center.y - (self.heigth/2)
        br = Point(br_x, br_y)
        return br
    
    def top_left(self)-> Point:
        tl_x = self.center.x - (self.width/2)
        tl_y = self.center.y + (self.heigth/2)
        tl = Point(tl_x, tl_y)
        return tl
    
    def top_rigth(self)-> Point:
        tr_x = self.center.x + (self.width/2)
        tr_y = self.center.y + (self.heigth/2)
        tr = Point(tr_x, tr_y)
        return tr
    
    def bottom(self)-> Line:
        return Line(self.bottom_left(), self.bottom_rigth())

    def left(self)-> Line:
        return Line(self.bottom_left(), self.top_left())

    def top(self)-> Line:
        return Line(self.top_left(), self.top_rigth())

    def right(self)-> Line:
        return Line(self.bottom_rigth(), self.top_rigth())
    
rectangle = Rectangle(4, 3, Point(4, -7)) # Crear el rectangulo