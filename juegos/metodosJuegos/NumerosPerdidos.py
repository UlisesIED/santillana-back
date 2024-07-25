class NumerosPerdidos:
    
    def __init__(self, numeros) -> None:
        self.__numeros = numeros
        
    def obtener_numeros_faltantes(self) -> str:
        return self.__calcular_numeros_faltantes()
        
    def __calcular_numeros_faltantes(self) -> str:
        lista_reversa = self.__numeros[::-1]
        longitud = len(lista_reversa)
        numero = int(lista_reversa[0])
        centinela = 0
        numeros_faltantes = ''
        while numero > 0:
            if longitud == centinela:
                numeros_faltantes += f' {numero}'
                numero -= 1
            else:
                if lista_reversa[centinela] == numero:
                    centinela += 1
                    numero -= 1
                else:
                    numeros_faltantes += f' {numero}'
                    numero -= 1
        return numeros_faltantes