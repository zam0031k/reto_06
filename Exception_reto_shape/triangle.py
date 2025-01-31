from Exception_reto_shape.shape import Shape
from Exception_reto_shape.point import Point


class Triangle(Shape):
    # Clase Triangle que hereda de la clase Shape.
    
    def __init__(self, p1: Point, p2: Point, p3: Point):
        vertices = [p1, p2, p3]
        super().__init__(vertices)
        
    def compute_area(self):
        a, b, c = list(map(lambda edge: edge.get_length(), self.get_edges())) #[edge.get_length() for edge in self._edges]
        s = (a + b + c) / 2  # Semi-perimeter
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Heron's formula
    
    def compute_perimeter(self):
        return sum(map(lambda edge: edge.get_length(), self.get_edges()))

    def compute_inner_angles(self):
        a, b, c = [edge.get_length() for edge in self._edges]
        from math import acos, degrees
        angle1 = degrees(acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle2 = degrees(acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle3 = 180 - (angle1 + angle2)
        self._inner_angles = [angle1, angle2, angle3]
        return self._inner_angles

class Equilateral(Triangle):
    # Triangulo equilátero: Todos los lados y angulos son iguales.
    
    def __init__(self, point_start: Point, side):
        height = (3**0.5 / 2) * side
        p1 = point_start    
        p2 = Point(side, point_start._y)
        p3 = Point(side / 2, height)
        super().__init__(p1, p2, p3)
        self._is_regular = True

    def __repr__(self):
        return f"Equilateral Triangle(side={self._edges[0].get_length()})"

class Isosceles(Triangle):
    # Triangulo isocesles: Dos lados iguales.
    
    def __init__(self, point_start: Point, base, side):
        height = (side**2 - (base / 2)**2)**0.5
        p1 = point_start
        p2 = Point(base, point_start._y)    
        p3 = Point(base / 2, height)
        super().__init__(p1, p2, p3)
        self._is_regular = False

    def __repr__(self):
        return f"Isosceles Triangle(base={self._edges[0].get_length()}, side={self._edges[1].get_length()})"
    
class Scalene(Triangle):
    # Triangulo escaleno: Todos sus lados son distintos.
    
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        self._is_regular = False

class TriRectangle(Triangle):
    # Triangulo rectangulo: Uno de sus angulos es 90°.
    
    def __init__(self, point_start: Point, base, height):
        p1 = point_start
        p2 = Point(base, point_start._y)
        p3 = Point(point_start._x , height)
        super().__init__(p1, p2, p3)
        self.is_regular = False