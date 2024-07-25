import unicodedata

class Palindromo():
    
    def __init__(self, palabra) -> None:
        self.__palabra = palabra
        
    def es_palindromo(self) -> bool:
        palabra_normalizada = self.__normalizar_palabra()
        lista_caracteres_palabra = self.__generar_lista_caracteres(palabra_normalizada)
        palabra_invertida = self.__invertir_palabra(lista_caracteres_palabra)
        es_palindromo = self.__compararPalabras(palabra_normalizada, palabra_invertida)
        return es_palindromo
        
    def __normalizar_palabra(self) -> str:
        palabra_normalizada = unicodedata.normalize("NFKD", self.__palabra).encode("ascii","ignore").decode("ascii")
        return palabra_normalizada
    
    def __generar_lista_caracteres(self, palabra) -> list:
        return list(palabra)
    
    def __invertir_palabra(self, lista) -> str:
        palabra = ""
        for caracter in reversed(lista):
            palabra += caracter
        return palabra
    
    def __compararPalabras(self, palabra, palabra_inversa):
        if palabra == palabra_inversa:
            return True
        else:
            return False 