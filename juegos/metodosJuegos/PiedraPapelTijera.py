class Piedra_papel_tijera():
    
    def __init__(self, juego) -> None:
        self.__juegos = juego
        self.__marcador = {
            'player_1': 0,
            'player_2': 0
        }
        
    def ganador(self):
        for player_1, player_2 in self.__juegos:
            print(player_1)
            print(player_2)
            self.__obtener_resultado_partida(player_1, player_2)
        ganador = self.__obtener_ganador()
        return ganador
        
    def __obtener_resultado_partida(self, player_1, player_2) -> None:
        if player_1 == player_2: return
        if player_1 == 'R' and player_2 == 'S':
            self.__marcador['player_1'] += 1
        elif player_1 == 'P' and player_2 == 'R':
            self.__marcador['player_1'] += 1
        elif player_1 == 'S' and player_2 == 'P':
            self.__marcador['player_1'] += 1
        else:
            self.__marcador['player_2'] += 1
            
    def __obtener_ganador(self) -> str:
        if self.__marcador['player_1'] == self.__marcador['player_2']:
            return "Tie"
        elif self.__marcador['player_1'] > self.__marcador['player_2']:
            return "Player 1"  
        else:
            return "Player 2"
            
        
        
    
    """    
    • El par puede contener combinaciones de "R" (piedra), "P" (papel)
    • "S" (tijera).
    """
    