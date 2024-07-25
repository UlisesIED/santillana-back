from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
import json

from juegos.models import Marcador_juego
from juegos.api.serializer import Marcador_juego_serializer
from juegos.metodosJuegos.Anagrama import Anagrama
from juegos.metodosJuegos.CalculaFechas import CalcularFechas
from juegos.metodosJuegos.ContandoPalabras import ContandoPalabras
from juegos.metodosJuegos.NumerosPerdidos import NumerosPerdidos
from juegos.metodosJuegos.Palíndromo import Palindromo
from juegos.metodosJuegos.PiedraPapelTijera import Piedra_papel_tijera
from juegos.metodosJuegos.TrucoTrato import Truco_trato


class Marcador_juego_view_set(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = Marcador_juego_serializer
    queryset = Marcador_juego.objects.all()
    
    @action(
        detail=False,
        methods=['post'],
        url_path='anagrama'
    )
    def anagrama(self, request):
        anagrama = Anagrama(
            palabra_1=request.data['palabra_1'], 
            palabra_2=request.data['palabra_2']
        )
        es_anagrama = anagrama.es_anagrama()
        response = {
            'es_anagrama': es_anagrama
        }
        return Response( response, status=HTTP_200_OK)
    
    @action(
        detail=False,
        methods=['post'],
        url_path='contando_palabras'
    )
    def contando_palabras(self, request):
        contar_palabras = ContandoPalabras(request.data['texto'])
        total_palabras = contar_palabras.contar_palabras()
        response = {
            "palabras_contadas": total_palabras
        }
        return Response( response, status=HTTP_200_OK)
    
    @action(
        detail=False,
        methods=['post'],
        url_path='calcula_fechas'
    )
    def calcula_fechas(self, request):
        fechas = CalcularFechas(
            request.data['fecha_1'], 
            request.data['fecha_2']
        )
        dias_transcurridos = fechas.calcular_dias_transcurridos()
        response = {
            "dias_transcurridos": dias_transcurridos
        }
        return Response( response, status=HTTP_200_OK)
    
    @action(
        detail=False,
        methods=['post'],
        url_path='numeros_perdidos'
    )
    def numeros_perdidos(self, request):
        numero = json.loads(request.data['secuencia_numeros'])
        numeros = NumerosPerdidos(numero)
        numeros_faltantes = numeros.obtener_numeros_faltantes()
        response = {
            "numeros_faltantes": numeros_faltantes
        }
        return Response(response, status=HTTP_200_OK)
    
    @action(
        detail=False,
        methods=['post'],
        url_path='palindromos'
    )
    def palindromos(self, request):
        palindromo = Palindromo(request.data['palabra'])
        es_palindromo = palindromo.es_palindromo()
        response = {
            'es_palindromo': es_palindromo
        }
        return Response(response, status=HTTP_200_OK)
    
    @action(
        detail=False,
        methods=['post'],
        url_path='piedra_papel_tijera'
    )
    def piedra_papel_tijera(self, request):
        partida = json.loads(request.data['partida'])
        juego = Piedra_papel_tijera(partida)
        resultado = juego.ganador()
        response = {
            'resultado': resultado
        }
        return Response(response, status=HTTP_200_OK)
    
    @action(
        detail=False,
        methods=['post'],
        url_path='truco_trato'
    )
    def truco_trato(self, request):
        personas = json.loads(request.data['personas'])
        solicitud = int(request.data['solicitud'])
        truco_trato = Truco_trato(personas)
        resultado = truco_trato.truco_trato(solicitud)
        response = {
            'resultado': resultado
        }
        return Response( response, status=HTTP_200_OK)