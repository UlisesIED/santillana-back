from datetime import datetime

class CalcularFechas():
    
    def __init__(self, fecha_1, fecha_2) -> None:
        self.__fecha_1 = fecha_1
        self.__fecha_2 = fecha_2
        
    def calcular_dias_transcurridos(self) -> int:
        fecha_1 = self.__ordenar_fecha(self.__fecha_1)
        fecha_2 = self.__ordenar_fecha(self.__fecha_2)
        
        fecha_1_formato = self.__obtener_fecha_formato(fecha_1)
        fecha_2_formato = self.__obtener_fecha_formato(fecha_2)
        
        dias_transcurridos = self.__obtener_dias_transcurridos(fecha_1_formato, fecha_2_formato)
        return dias_transcurridos
        
    def __ordenar_fecha(self, fecha) -> dict:
        fecha = {
            'dia': fecha[0:2],
            'mes': fecha[2:4],
            'año': fecha[4:8] 
        }
        return fecha
        
    def __obtener_fecha_formato(self, fecha):
        fecha = datetime.strptime(f"{fecha['año']}-{fecha['mes']}-{fecha['dia']}", "%Y-%m-%d")
        return fecha
    
    def __obtener_dias_transcurridos(self, fecha_1, fecha_2) -> int:
        dias = fecha_1 - fecha_2
        return abs(dias.days)