class MismosCaracteres:
    def __init__(self):
        self.lista_palabras = []
        self.cantidad_palabras = 0

    def solicitar_cantidad_palabras(self):
        while True:
            try:
                self.cantidad_palabras = int(input("Ingresa la cantidad de palabras que deseas analizar: "))
    
                break
            except:
                raise ValueError("ERROR: ingresa una cantidad válida")

    def solicitar_palabras(self):
        for i in range(self.cantidad_palabras):
            palabra = input(f'Ingresa la palabra {i + 1}: ')
            self.lista_palabras.append(palabra)

    def analizar_caracteres(self):
        lista_mismos_caracteres = []
        for i in range(len(self.lista_palabras)):
            for j in range(i + 1, len(self.lista_palabras)):
                if sorted(self.lista_palabras[i]) == sorted(self.lista_palabras[j]):
                    if self.lista_palabras[i] not in lista_mismos_caracteres:
                        lista_mismos_caracteres.append(self.lista_palabras[i])
                    if self.lista_palabras[j] not in lista_mismos_caracteres:
                        lista_mismos_caracteres.append(self.lista_palabras[j])

        if not lista_mismos_caracteres:
            print('No existen elementos que comparten los mismos caracteres')
            return ''

        print(f'Los elementos que comparten los mismos caracteres son: {lista_mismos_caracteres}')

try:
    caracteres = MismosCaracteres()
    caracteres.solicitar_cantidad_palabras()
    caracteres.solicitar_palabras()
    caracteres.analizar_caracteres()
except Exception as error:
    print(f'{error}')    