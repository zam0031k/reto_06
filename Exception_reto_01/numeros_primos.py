class NumerosPrimos:
    def __init__(self):
        self.lista_numeros = []

    def solicitar_numeros(self):
        """
        Solicita al usuario la cantidad de números a analizar y los números a analizar.
        """
        while True:
            try:
                cantidad = int(input("Ingresa la cantidad de números que deseas analizar: "))
                if cantidad == 0:
                    raise ValueError("ERROR: la cantidad de números no puede ser cero")
                break
            except:
                raise ValueError("ERROR: ingresa una cantidad válida")

    
        for i in range(cantidad):
            num = int(input(f"Digite el valor {i + 1}: "))
            self.lista_numeros.append(num)
    
    def valores_primos(self):
        """
        Encuentra y muestra los números primos de una lista dada.
        """
        primos = []
        for i in self.lista_numeros:
            if i > 1:
                for j in range(2, int(i**0.5) + 1):
                    if i % j == 0:
                        break
                else:
                    primos.append(i)

        print("De los números mencionados, aquellos que son primos son:")
        for primo in primos:
            print(primo, end=" ")

try: 
    primos = NumerosPrimos()
    primos.solicitar_numeros()
    primos.valores_primos()
except Exception as error:
    print(f'{error}')