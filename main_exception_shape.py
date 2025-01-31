from Exception_reto_shape.triangle import Triangle, Equilateral, Isosceles, Scalene, TriRectangle
from Exception_reto_shape.rectangle import Rectangle, Square
from Exception_reto_shape.point import Point

def main():
    print('*****************************************')
    print('RECTÁNGULO: ')
    
    # Validación de entrada de datos
    try:
        rect_point_x = float(input('Coordenada del primer punto en x: '))
        rect_point_y = float(input('Coordenada del primer punto en y: '))
        rect_width = float(input('Ancho: '))
        rect_heigh = float(input('Alto: '))
    except ValueError:
        # Captura de errores de conversión de entrada a float
        raise ValueError ("Error: Las coordenadas y dimensiones deben ser números.")
        
    
    # Validación de dimensiones
    if rect_width <= 0 or rect_heigh <= 0:
        raise ValueError ("Error: El ancho y el alto deben ser positivos.")
        
    
    # Creación del objeto Rectangle
    rectangle = Rectangle(Point(rect_point_x, rect_point_y), rect_width, rect_heigh)
    
    # Cálculos y resultados
    print("Área del rectángulo:", rectangle.compute_area())
    print("Perímetro del rectángulo:", rectangle.compute_perimeter())
    print("Vértices:", rectangle.get_vertices())
    print("Bordes:", rectangle.get_edges())
    print("Longitudes de los lados:", rectangle.get_edge_lengths())
    print("Ángulos internos:", rectangle.get_inner_angles())

    print('\n*****************************************')
    print("CUADRADO")
    
    # Validación de entrada de datos para el cuadrado
    try:
        square_point_x = float(input('Coordenada del primer punto en x: '))
        square_point_y = float(input('Coordenada del primer punto en y: '))
        square_side = float(input('Lado: '))
    except ValueError:
        # Captura de errores de conversión de entrada a float
        raise ValueError ("Error: Las coordenadas y dimensiones deben ser números.")
        
    
    # Validación de dimensiones
    if square_side <= 0:
        # Verificación de que el lado sea positivo
        raise ValueError ("El lado debe ser positivo.")
        
    
    # Creación del objeto Square
    square = Square(Point(square_point_x, square_point_y), square_side)
    
    # Cálculos y resultados
    print("Área del cuadrado:", square.compute_area())
    print("Perímetro del cuadrado:", square.compute_perimeter())
    print("Vértices:", square.get_vertices())
    print("Bordes:", square.get_edges())
    print("Longitudes de los lados:", square.get_edge_lengths())
    print("Ángulos internos:", square.get_inner_angles())

    print('\n*****************************************')
    print("TRIÁNGULO EQUILÁTERO")
    
    # Validación de entrada de datos para el triángulo equilátero
    try:
        tri_equilateral_point1_x = float(input('Coordenada del primer punto en x: '))
        tri_equilateral_point1_y = float(input('Coordenada del primer punto en y: '))
        tri_equilateral_side = float(input('Lado: '))
    except ValueError:
        # Captura de errores de conversión de entrada a float
        raise ValueError ("Error: Las coordenadas deben ser números.")
        
    
    # Creación del objeto Equilateral
    equilateral_triangle = Equilateral(Point(tri_equilateral_point1_x, tri_equilateral_point1_y), tri_equilateral_side)
    
    # Cálculos y resultados
    print("Área del triángulo equilátero:", equilateral_triangle.compute_area())
    print("Perímetro del triángulo equilátero:", equilateral_triangle.compute_perimeter())
    print("Vértices:", equilateral_triangle.get_vertices())
    print("Bordes:", equilateral_triangle.get_edges())
    print("Longitudes de los lados:", equilateral_triangle.get_edge_lengths())
    print("Ángulos internos:", equilateral_triangle.get_inner_angles())

    print('\n*****************************************')
    print("TRIÁNGULO ISÓSCELES")
    
    # Validación de entrada de datos para el triángulo isósceles
    try:
        tri_iso_point1_x = float(input('Coordenada del primer punto en x: '))
        tri_iso_point1_y = float(input('Coordenada del primer punto en y: '))
        tri_iso_base = float(input('Base: '))
        tri_iso_sice = float(input('Lado: '))
        
    except ValueError:
        # Captura de errores de conversión de entrada a float
        raise ValueError ("Error: Las coordenadas deben ser números.")
        
    
    # Creación del objeto Isosceles
    isosceles_triangle = Isosceles(Point(tri_iso_point1_x, tri_iso_point1_y), tri_iso_base, tri_iso_sice)
    
    # Cálculos y resultados
    print("Área del triángulo isósceles:", isosceles_triangle.compute_area())
    print("Perímetro del triángulo isósceles:", isosceles_triangle.compute_perimeter())
    print("Vértices:", isosceles_triangle.get_vertices())
    print("Bordes:", isosceles_triangle.get_edges())
    print("Longitudes de los lados:", isosceles_triangle.get_edge_lengths())
    print("Ángulos internos:", isosceles_triangle.get_inner_angles())

    print('\n*****************************************')
    print("TRIÁNGULO RECTÁNGULO")
    
    # Validación de entrada de datos para el triángulo rectángulo
    try:
        tri_rect_point1_x = float(input('Coordenada del primer punto en x: '))
        tri_rect_point1_y = float(input('Coordenada del primer punto en y: '))
        tri_rect_base = float(input('Base: '))
        tri_rect_heigh = float(input('Altura: '))
    except ValueError:
        # Captura de errores de conversión de entrada a float
        raise ValueError ("Error: Las coordenadas deben ser números.")
        
    
    # Creación del objeto TriRectangle
    tri_rect = TriRectangle(Point(tri_rect_point1_x, tri_rect_point1_y), tri_rect_base, tri_rect_heigh)
    
    # Cálculos y resultados
    print("Área del triángulo rectángulo:", tri_rect.compute_area())
    print("Perímetro del triángulo rectángulo:", tri_rect.compute_perimeter())
    print("Vértices:", tri_rect.get_vertices())
    print("Bordes:", tri_rect.get_edges())
    print("Longitudes de los lados:", tri_rect.get_edge_lengths())
    print("Ángulos internos:", tri_rect.get_inner_angles())
    
    print('\n*****************************************')
    print("TRIÁNGULO ESCALENO")
    
    # Validación de entrada de datos para el triángulo escaleno
    try:
        tri_scalene_point1_x = float(input('Coordenada del primer punto en x: '))
        tri_scalene_point1_y = float(input('Coordenada del primer punto en y: '))
        tri_scalene_point2_x = float(input('Coordenada del segundo punto en x: '))
        tri_scalene_point2_y = float(input('Coordenada del segundo punto en y: '))
        tri_scalene_point3_x = float(input('Coordenada del tercer punto en x: '))
        tri_scalene_point3_y = float(input('Coordenada del tercer punto en y: '))
    except ValueError:
        # Captura de errores de conversión de entrada a float
        raise ValueError ("Error: Las coordenadas deben ser números.")
        
    
    # Creación del objeto Scalene
    scalene_triangle = Scalene(Point(tri_scalene_point1_x, tri_scalene_point1_y), Point(tri_scalene_point2_x, tri_scalene_point2_y), Point(tri_scalene_point3_x, tri_scalene_point3_y))
    
    # Cálculos y resultados
    print("Área del triángulo escaleno:", scalene_triangle.compute_area())
    print("Perímetro del triángulo escaleno:", scalene_triangle.compute_perimeter())
    print("Vértices:", scalene_triangle.get_vertices())
    print("Bordes:", scalene_triangle.get_edges())
    print("Longitudes de los lados:", scalene_triangle.get_edge_lengths())
    print("Ángulos internos:", scalene_triangle.get_inner_angles())

if __name__ == "__main__":
    try: 
        main()  
    except ValueError as error:
        print(f'{error}')