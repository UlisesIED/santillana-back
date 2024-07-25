class Anagrama():
    
    def __init__(self, palabra_1, palabra_2) -> None:
        self.__palabra_1 = palabra_1
        self.__palabra_2 = palabra_2
        
    def es_anagrama(self) -> bool:
        misma_longitud = self.__misma_longitud()
        if not misma_longitud: return False
        palabra_1 = self.__normalizar_texto(self.__palabra_1)
        palabra_2 = self.__normalizar_texto(self.__palabra_2)
        palabra_1_separada = self.__separar_palabras(palabra_1)
        palabra_2_separada = self.__separar_palabras(palabra_2)
        palabra_1_contada = self.__contar_palabras(palabra_1_separada)
        palabra_2_contada = self.__contar_palabras(palabra_2_separada)
        atributos = self.__obtenerAtributos(palabra_1_contada)
        mismos_atributos = self.__verificar_atributos(palabra_2, atributos)
        if not mismos_atributos: return False
        es_anagrama = self.__comparar_palabras(atributos, palabra_1_contada, palabra_2_contada)
        return es_anagrama
        
    def __misma_longitud(self) -> bool:
        longitud_1 = len(self.__palabra_1)
        longitud_2 = len(self.__palabra_2)
        if longitud_1 == longitud_2: return True
        else: return False
        
    def __normalizar_texto(self, texto):
        return texto.lower()
    
    def __separar_palabras(self, texto) -> list:
        return list(texto)
    
    def __contar_palabras(self, lista) -> dict:
        palabras_contadas = {}
        for palabra in lista:
            if palabra in palabras_contadas:
                palabras_contadas[palabra] += 1
            else:
                palabras_contadas[palabra] = 1
        return palabras_contadas
    
    def __obtenerAtributos(self, palabras) -> list:
        atributos = []
        for atributo in palabras:
            atributos.append(atributo)
        return atributos
    
    def __verificar_atributos(self, palabras_2, atributos) -> bool:
        for atributo in atributos:
            if atributo in palabras_2:
                continue
            else:
                return False
        return True
    
    def __comparar_palabras(self, atributos, palabras_1, palabras_2) -> bool:
        for atributo in atributos:
            if palabras_1[atributo] != palabras_2[atributo]:
                return False
        return True
    
    