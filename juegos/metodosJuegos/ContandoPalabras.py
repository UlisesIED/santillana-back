import unicodedata

class ContandoPalabras():
    
    def __init__(self, texto) -> None:
        self.__texto = texto
        
    def contar_palabras(self) -> dict:
        texto_normalizado = self.__normalizar_texto()
        palabras_separadas = self.__separar_palabras(texto_normalizado)
        palabras_contadas = self.__contar_palabras(palabras_separadas)
        return palabras_contadas
        
    def __normalizar_texto(self) -> str:
        texto_normalizado = unicodedata.normalize("NFKD", self.__texto).encode("ascii","ignore").decode("ascii")
        for caracter in [',', '.', ';']:
            texto_normalizado = texto_normalizado.replace(caracter, '')
        return texto_normalizado
    
    def __separar_palabras(self, texto) -> list:
        return texto.split()
    
    def __contar_palabras(self, lista) -> dict:
        palabras_contadas = {}
        for palabra in lista:
            if palabra in palabras_contadas:
                palabras_contadas[palabra] += 1
            else:
                palabras_contadas[palabra] = 1
        return palabras_contadas