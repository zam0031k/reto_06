class MayorSuma:
    def __init__(self):
        self.lista_numeros = []

    def ingresar_numeros(self):
        while True:
            try:
                cantidad = int(input("Define la cantidad de números que desea tener en su lista: "))
                for i in range(cantidad):
                    valor = int(input(f"Ingresa el valor {i + 1}: "))
                    self.lista_numeros.append(valor)
                break
            except:
                raise ValueError("ERROR: el valor ingresado NO es numérico, por favor vuelve a intentarlo.")

    def mayor_suma_elementos(self):
        mayor_suma = 0
        valor1 = 0
        valor2 = 0

        for i in range(len(self.lista_numeros) - 1):
            suma_actual = self.lista_numeros[i] + self.lista_numeros[i + 1]
            if mayor_suma < suma_actual:
                mayor_suma = suma_actual
                valor1 = self.lista_numeros[i]
                valor2 = self.lista_numeros[i + 1]

        print(f"La suma entre los elementos consecutivos {valor1} y {valor2} da el mayor resultado: {mayor_suma}") 

try:
    suma = MayorSuma()
    suma.ingresar_numeros()
    suma.mayor_suma_elementos()
except Exception as error:
    print(f'{error}')