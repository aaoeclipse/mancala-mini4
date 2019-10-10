from Mancala import Mancala

import random
import copy


class Monte_carlo_mancala:
    """ Un juego de Mancala con una IA de puro monte carlo """

    def __init__(self, n=100):
        self.num_juegos_que_jugar = n # numero de juegos que hace el monte carlo
        self.juego_mancala = Mancala()

    def gameOver(self):
        ganador = self.juego_mancala.get_ganador(end=True)
        if ganador == 1:
            print('El AI Gano')
        elif ganador == 0:
            print('Empate')
        else:
            print('El jugador Gano')
        exit(0)
    
    def empezar_juego(self):
        """ Empieza el juego """
        juego_termino = False
        print(self.juego_mancala)

        # Empieza juego
        while not juego_termino:
            resultados_de_juegos = [0,0,0,0,0,0]
            # IA piensa a lo random
            for num_de_partida in range(self.num_juegos_que_jugar):
                # Se crea una copia del juego en la cual se va a probar hacer alguna jugada alazar
                copia_del_juego_actual = copy.deepcopy(self.juego_mancala)
                # Posibles jugadas
                posibles_jugadas  = copia_del_juego_actual.posibles_jugadas()
                if posibles_jugadas == []:
                    self.gameOver()
                # Se escoge uno al azar
                primera_jugada = random.choice(posibles_jugadas)
                # Se hace la jugada
                copia_del_juego_actual.hacer_jugada(primera_jugada)
                while True:
                    posibles_jugadas = copia_del_juego_actual.posibles_jugadas()
                    # si no hay posibles jugadas entonces significa que el juego se termino
                    if (posibles_jugadas == []):
                        break
                    copia_del_juego_actual.hacer_jugada(random.choice(posibles_jugadas))

                if copia_del_juego_actual.get_ganador() == 1:
                    resultados_de_juegos[primera_jugada] += 1

            # Turno de IA
            movida = resultados_de_juegos.index(max(resultados_de_juegos))
            self.juego_mancala.hacer_jugada(movida)
            print('AI movio {}'.format(movida+1))
            
            # Si no es turno del jugador, lo hace skip
            if self.juego_mancala.turno_jugador != 1:
                # Turno del Jugador
                # Mostrarle el tablero al jugador
                while self.juego_mancala.turno_jugador == 2:
                    print(self.juego_mancala)
                    posibles_jugadas = self.juego_mancala.posibles_jugadas()
                    if posibles_jugadas == []:
                        self.gameOver()
                        print('Game Over')
                    
                    for number in range(len(posibles_jugadas)):
                        posibles_jugadas[number] -= 6

                    print('Las posibles jugadas son: {}'.format(posibles_jugadas))
                    movida_player = input()
                    # movida_player += 6

                    if int(movida_player) not in posibles_jugadas:
                        while True:
                            print('no es posible la jugada')
                            movida_player = input()
                            if int(movida_player) in posibles_jugadas:
                                break
                    
                    self.juego_mancala.hacer_jugada(int(movida_player)+6)

                print(self.juego_mancala)
                print('========================')

          
            

juego = Monte_carlo_mancala(10000)
juego.empezar_juego()