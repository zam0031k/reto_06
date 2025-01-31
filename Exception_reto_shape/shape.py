from Exception_reto_shape.line import Line

class Shape:
    def __init__(self, vertices: list):
        self._vertices = vertices  # lista de objetos Point (vértices)
        self._edges = self.edges()  # lista de objetos Line (bordes)
        self._edge_lengths = [edge.get_length() for edge in self._edges]  # lista de longitudes de los bordes
        self._inner_angles = self.compute_inner_angles()  # lista de ángulos internos
        self._is_regular = self.regular()  # True si la figura es regular, False en caso contrario

    def edges(self):
        edges = []
        self.num_vertices = len(self._vertices)
        for i in range(self.num_vertices):
            edges.append(Line(self._vertices[i], self._vertices[(i + 1) % self.num_vertices]))  # Conecta los vértices y cierra la figura
        return edges

    def regular(self):
        return all(map(lambda length: length == self._edge_lengths[0], self._edge_lengths))

    def compute_area(self):  # Método abstracto para aplicar polimorfismo
        pass

    def compute_perimeter(self):  # Método abstracto para aplicar polimorfismo
        pass

    def compute_inner_angles(self):
        if self.regular():
            angles = (self.num_vertices - 2) * 180 / self.num_vertices
            return [angles] * self.num_vertices
        else:
            angles = []
            for i in range(self.num_vertices):
                a = self._edge_lengths[i - 1]  # Lado anterior
                b = self._edge_lengths[i]      # Lado actual
                c = self._edge_lengths[(i + 1) % self.num_vertices]  # Lado siguiente
                angle = self.calculate_angle(a, b, c)
                angles.append(angle)
            return angles

    def calculate_angle(self, a, b, c):
        import math
        cos_angle = (a**2 + b**2 - c**2) / (2 * a * b)
        angle = math.acos(cos_angle)
        return math.degrees(angle)
    
    # Getters
    def get_vertices(self):
        return self._vertices

    def get_inner_angles(self):
        return self._inner_angles

    def get_edge_lengths(self):
        return self._edge_lengths

    def get_edges(self):
        return self._edges
    
    def get_is_regular(self):
        return self._is_regular

    # Setters
    def set_vertices(self, vertices: list):
        self._vertices = vertices