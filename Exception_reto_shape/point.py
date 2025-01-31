class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    # Setters
    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    # Getters
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def compute_distance(self, new_point: "Point"):
        return ((new_point._x - self._x )**2 + (new_point._y - self._y)**2)**0.5

    def __repr__(self):
        return f"Point(x={self.get_x()}, y={self.get_y()})"   