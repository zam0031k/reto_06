# Reto 06: Manejo de Excepciones en POO

## **Descripción General**: 

Este repositorio contiene la implementación de dos retos en el curso de Programación Orientada a Objetos (POO), con el agregado de manejo de excepciones para garantizar la robustez del código ante entradas inválidas y errores de ejecución.

## **Estructura**:
````bash
reto_06/
├── Exception_reto_01/
│   ├── mayor_suma.py
│   ├── mismos_caracteres.py
│   ├── palindromos.py
├── Exception_reto_shape/
│   ├── __init__.py
│   ├── point.py
│   ├── line.py
│   ├── rectangle.py
│   ├── shape.py
│   ├── triangle.py
│   ├── numeros_primos.py
│   ├── operaciones_aritmeticas.py
├── main_exception_shape.py
````
## **Descripción de Archivos y Manejo de Excepciones**
1. Exception_reto_01/
Contiene los archivos del reto 01, donde se aplicaron excepciones para manejar posibles errores en el ingreso de datos por parte del usuario.

### **1.1. palindromos.py:**
- Excepción personalizada: ``ErrorPalindromo``
Se utiliza para capturar errores específicos en la verificación de palíndromos.

Se levanta cuando el usuario ingresa una palabra no válida que no cumple con los requisitos esperados.
````python
class ErrorPalindromo(Exception):
    def __init__(self, menssage):
        super().__init__(menssage)
````
### **1.2. operaciones_aritméticas.py:**
- Excepción: ``ValueError``
Se maneja al definir_valores, donde se solicita al usuario dos números y un operador.

Si el usuario ingresa un valor no numérico, se levanta un ValueError con un mensaje de error.
````python
while True:
    try: 
        self.primer_num = int(input('Ingresa el primer número: '))
        self.segundo_num = int(input('Ingresa el segundo número: '))
        self.operador = input('Ingrese el operador: ')
        break
    except:
        raise ValueError('los valores ingresados no son números')
````

### **1.3. numeros_primos.py:**
- Excepción: ``ValueError``
Se maneja en solicitar_numeros, donde se solicita al usuario un número entero.

Si el usuario ingresa un valor inválido, se levanta un ValueError con un mensaje aclaratorio.
`````python
while True:
    try:
        for i in range(cantidad):
            num = int(input(f"Digite el valor {i + 1}: "))
            self.lista_numeros.append(num)
        break
    except:
        raise ValueError("ERROR: Valor NO numérico ingresado, por favor vuelve a intentarlo.")
``````
### **1.4. mismos_caracteres.py:**
- Excepción: ``ValueError``
Se maneja en el método solicitar_cantidad_palabras, donde se solicita al usuario un número entero.

Se captura cualquier valor no entero y se muestra un mensaje indicando el error.
`````python
while True:
    try:
        self.cantidad_palabras = int(input("Ingresa la cantidad de palabras que deseas analizar: "))
        break
    except:
        raise ValueError("ERROR: ingresa una cantidad válida")
``````
### **1.5. mayor_suma.py:**
- Excepción: ``ValueError``
Se maneja en el método ingresar_numeros, donde se solicita al usuario una cantidad de números.

Si el usuario ingresa un valor no numérico, se levanta la excepción ValueError con un mensaje de error.

`````python
while True:
    try:
        cantidad = int(input("Define la cantidad de números que desea tener en su lista: "))
        for i in range(cantidad):
            valor = int(input(f"Ingresa el valor {i + 1}: "))
            self.lista_numeros.append(valor)
        break
    except:
        raise ValueError("ERROR: el valor ingresado NO es numérico, por favor vuelve a intentarlo.")
``````
## **2. Exception_reto_shape/**
Contiene el reto de programación de formas geométricas, donde se aplicaron excepciones para validar entradas incorrectas y asegurar la correcta creación de objetos.

### **2.1. main_exception_shape.py:**
- Excepción: ``ValueError``
Se maneja en la creación y cálculo de propiedades de objetos geométricos.

Si hay un error en la inicialización o manipulación de objetos, se captura y se notifica al usuario.
`````python
try:
    rect_point_x = float(input('Coordenada del primer punto en x: '))
    rect_point_y = float(input('Coordenada del primer punto en y: '))
    rect_width = float(input('Ancho: '))
    rect_heigh = float(input('Alto: '))
except ValueError:
    # Captura de errores de conversión de entrada a float
    raise ValueError ("Error: Las coordenadas y dimensiones deben ser números.")  
``````






