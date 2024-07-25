from random import choice

class Truco_trato():
    
    __sustos = ['🎃', '👻', '💀', '🕷', '🕸', '🦇']
    __dulces = ['🍰', '🍬', '🍡', '🍭', '🍪', '🍫', '🧁', '🍩']
    
    def __init__(self, personas) -> None:
        self.__personas = personas
        
    def truco_trato(self, eleccion):
        elecciones = [self.__asignar_sustos, self.__asignar_dulces]
        total = elecciones[eleccion]()
        return total
        
    def __asignar_sustos(self):
        total_sustos = self.__calcular_total_sustos()
        sustos = ""
        for index in range(total_sustos):
            sustos += choice(self.__sustos)
        return sustos
    
    def __asignar_dulces(self):
        total_dulces = self.__calcular_total_dulces()
        dulces = ""
        for index in range(total_dulces):
            dulces += choice(self.__dulces)
        return dulces
        
    def __calcular_total_sustos(self):
        altura_total = sum(int(persona['altura']) for persona in self.__personas)
        sustos_nombre = sum(self.__obtener_sustos_nombre(persona['nombre']) for persona in self.__personas)
        sustos_edad = sum(self.__obtener_sustos_edad(int(persona['edad'])) for persona in self.__personas)
        sustos_altura = self.__obtener_sustos_altura(altura_total)
        sustos_totales = sustos_edad + sustos_altura + sustos_nombre
        return sustos_totales
    
    def __calcular_total_dulces(self):
        dulces_nombre = sum(self.__obtener_dulces_nombre(persona['nombre']) for persona in self.__personas)
        dulces_edad = sum(self.__obtener_dulces_edad(int(persona['edad'])) for persona in self.__personas)
        dulces_altura = sum(self.__obtener_dulces_altura(int(persona['altura'])) for persona in self.__personas)
        dulces_totales = dulces_altura + dulces_edad + dulces_nombre
        return dulces_totales
    
    def __obtener_sustos_nombre(self, nombre) -> int:
        longitud_nombre = len(nombre)
        total_sustos = longitud_nombre // 2
        return total_sustos
    
    def __obtener_sustos_edad(self, edad) -> int:
        if edad % 2 == 0:
            return 2
        else: return 0
        
    def __obtener_sustos_altura(self, altura) -> int:
        premio_sustos = altura // 100
        total_sustos = premio_sustos * 3
        return total_sustos
    
    def __obtener_dulces_nombre(self, nombre) -> int:
        return len(nombre)
    
    def __obtener_dulces_edad(self, edad) -> int:
        if edad > 10: 
            return 3
        else:
            return edad // 3
        
    def __obtener_dulces_altura(self, altura) -> int:
        if altura > 150:
            return 6
        else:
            return (altura // 50) * 2 
    
"""
persona = [
    {
        nombre
        edad
        altura
    }
]
"""