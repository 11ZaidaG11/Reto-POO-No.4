class Point:
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y

    def compute_distance(self, point: "Point")-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance

class Line():
    def __init__(self, start:Point, end:Point):
        self.start = start
        self.end = end

    def length(self)-> float:
        length = self.start.compute_distance(self.start, self.end)
        return length

class Shape():
    def __init__(self):
        pass
    def vertices(self) -> list[Point]:
        pass
    def edges(self) -> list[Line]:
        pass
    def inner_angles(self) -> list[float]:
        pass


    def compute_area(self):
        pass
    def compute_perimeter(self):
        pass
    def compute_inner_angles(self):
        pass

class Rectangle(Shape):
    def __init__(self, b:float, h:float):
        super().__init__()
        self.b = b
        self.h = h

    def compute_area(self) -> float:
        return self.b * self.h
    
    def compute_perimeter(self) -> float:
        return 2*self.b + 2*self.h
    

class Square(Rectangle):
    def __init__(self, l:float):
        super().__init__()
        self.l = l

    def compute_area(self) -> float:
        return self.l ** 2
    
    def compute_perimeter(self) -> float:
        return 4*self.l

class Triangle(Shape):
    def __init__(self, b:float, h:float):
        super().__init__()
        self.b = b
        self.h = h

    def compute_area(self) -> float:
        return (self.b * self.h) / 2
    
class Equilateral(Triangle):
    pass

class Isosceles(Triangle):
    pass

class Scalene(Triangle):
    pass

class TriRectangle(Triangle):
    pass