from Exception_reto_shape.shape import Shape
from Exception_reto_shape.point import Point

class Rectangle(Shape):
    def __init__(self, point_start: Point, width, height):
        self._width = width
        self._height = height
        vertices = [
            point_start,
            Point(point_start.get_x() + width, point_start.get_y()),
            Point(point_start.get_x() + width, point_start.get_y() + height),
            Point(point_start.get_x(), point_start.get_y() + height)
        ]
        super().__init__(vertices)

    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
     
    def compute_area(self):
        return self.get_width() * self.get_height()

    def compute_perimeter(self):
        return 2 * (self.get_width() + self.get_height())
    
class Square(Rectangle):
    # Clase Square que hereda de la clase Rectangle.

    def __init__(self, point_start: Point, side):
        self._side = side
        p1 = point_start
        super().__init__(p1, side, side)
        self._is_regular = True

    def compute_area(self):
        return self._side ** 2

    def compute_perimeter(self):
        return 4 * self._side

    def __repr__(self):
        return f"Square(side={self._side})"
    