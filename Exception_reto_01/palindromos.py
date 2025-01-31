import re

class Palindromo():
    def __init__(self):
        self.palabra = ''
        self.lista_palabra = []
        self.palabra_invertida = []

    def solicitar_palabra(self):
        self.palabra = input('Escribe una palabra: ')
        self.palabra = self.palabra.lower()

    def convertir_palabra(self):
        for i in self.palabra:
            self.lista_palabra.append(i)
            self.palabra_invertida.append(i)

    def invertir_palabra(self):
        self.palabra_invertida.reverse()
        
    def validar_palabra(self):
        return bool(re.fullmatch(r'[a-z]+', self.palabra))

    def verificar_palindromo(self):
        if self.validar_palabra(): 
            if self.lista_palabra == self.palabra_invertida:
                print(f'La palabra proporcionada "{self.palabra}", efectivamente corresponde a un palíndromo.')
            else:
                print(f'La palabra proporcionada "{self.palabra}", NO corresponde a un palíndromo.')
        else: 
            raise ErrorPalindromo('Error: la palabra proporcionada contiene números, espaciones o caracteres especiales')

class ErrorPalindromo(Exception):
    def __init__(self, menssage):
        super().__init__(menssage)

try: 
    palindromo = Palindromo()
    palindromo.solicitar_palabra()
    palindromo.convertir_palabra()
    palindromo.invertir_palabra()
    palindromo.verificar_palindromo()
except ErrorPalindromo as error:
    print(f'{error}') 
    