class OperacionesAritmeticas:
    def __init__(self):
        self.primer_num = None
        self.segundo_num = None
        self.operador = ''
        
    def definir_valores(self):
        while True:
            try: 
                self.primer_num = int(input('Ingresa el primer número: '))
                self.segundo_num = int(input('Ingresa el segundo número: '))
                self.operador = input('Ingrese el operador: ')
                break
            except:
                raise ValueError('los valores ingresados no son números')
        
    def calcular(self):
        """
        Realiza una operación matemática entre dos números según el operador.

        para self.primer_num: El primer número.
        para self.segundo_num: El segundo número.
        para operador: El operador a usar para la operación ('+', '-', '*', '/').
        return: El resultado de la operación.
        """
        match self.operador:  # Se usa match-case para determinar el operador.
            case '+':  
                resultado = self.primer_num + self.segundo_num
            case '-': 
                resultado = self.primer_num - self.segundo_num
            case '*':  
                resultado = self.primer_num * self.segundo_num
            case '/':  
                if self.segundo_num == 0:
                    raise ZeroDivisionError('no se puede dividir entre cero')

                else:
                    resultado = self.primer_num / self.segundo_num
            case _:  # Caso por defecto si el operador no es válido.
                raise ValueError('operador no reconocido. Por favor vuelva a intentarlo')

        print(f'El resultado de la operación {self.primer_num} {self.operador} {self.segundo_num} es: {resultado}')
        
try:
    operacion = OperacionesAritmeticas()
    operacion.definir_valores()
    operacion.calcular()

except Exception as error:
    print(f'Error: {error}')