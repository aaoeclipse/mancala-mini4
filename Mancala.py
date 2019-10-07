

class Mancala:
    """ Aqui estan el juego de mancla con todas las reglas """
    """ 1. Solo se puede elegir las pociciones del lado de uno
        2.  En mancala al escoger uno se distribuyen cada uno de las piedras de forma counter-clockwise
        3. Si acaba en los puntos entonces la persona toma otro turno
        4. si cae en un vacio entonces ese  y los del otro lado caen en el puntaje del jugador
    """

    def __init__(self):
        """ crea tablero inicial """
        """ El tablero es un array del 0 a 13 (14 posiciones) """
        self.tablero = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
        self.turno_jugador = 1
        self.jugada_inicial = None


    def hacer_jugada(self,posicion_de_jugada):
        """ Recive la posicion en la cual se va a hacer la jugada """
        stack_de_piezas = self.tablero[posicion_de_jugada]
        self.tablero[posicion_de_jugada] = 0
        # Distribuir la distribucion de piezas
        ultimo_turno = self.distribucion_piezas(stack_de_piezas,posicion_de_jugada)
        # Ver si aplican una de las reglas especiales
        self.reglas_especiales(ultimo_turno)
        # Cambiar de turno de jugador
        self.cambio_de_turno()


    def distribucion_piezas(self, stack, posicion_obtenido):
        """ distribucion de piezas """
        posicion_ahora = 0
        # Distribuir las piedras
        while stack > 0:
            posicion_obtenido += 1
            # En teoria quiero hacer que si la posicion se pasa del tablero
            # este regrese a 0
            if (posicion_ahora+posicion_obtenido) >= len(self.tablero):
                posicion_ahora -= 14
            # Agregamos uno a esa posicion almenos que sea el de puntos del enemigo
            if self.turno_jugador == 1 and (posicion_ahora+posicion_obtenido) != 13:
                self.tablero[posicion_ahora+posicion_obtenido] += 1
                stack -= 1

            if self.turno_jugador == 2 and (posicion_ahora+posicion_obtenido) != 6:
                self.tablero[posicion_ahora+posicion_obtenido] += 1
                stack -= 1

        # hay que ver donde cae la ultima pieza
        ultima_piedra = (posicion_ahora+posicion_obtenido)
        return ultima_piedra


    def reglas_especiales(self, posicion_final):
        """ Hay dos reglas especiales
        Si la ultima pieza cae en tu propio puntaje, entonces tienes otro turno
        si la ultima pieza cae en uno vacio, entonces el que esta del otro lado y se van a tu puntaje """
        # Jugador 1
        if self.turno_jugador == 1: 
            if posicion_final == 6:
                self.cambio_de_turno()
            elif self.tablero[posicion_final] == 1:
                self.tablero[posicion_final] = 0
                self.tablero[6] += 1
                self.tablero[6] += self.tablero[12-posicion_final]
                self.tablero[12-posicion_final] = 0
        # Jugador 2
        else:
            if posicion_final == 13:
                self.cambio_de_turno()
            elif self.tablero[posicion_final] == 1:
                self.tablero[posicion_final] = 0
                self.tablero[13] += 1
                self.tablero[13] += self.tablero[12-posicion_final]
                self.tablero[12-posicion_final] = 0



    def cambio_de_turno(self):
        next_player = self.turno_jugador % 2
        self.turno_jugador = next_player + 1


    def posibles_jugadas(self):
        """ Regresa una lista de posibles posiciones que elegir """
        # Miramos quien esta jugando
        jugadas_posibles = []
        if self.turno_jugador == 1:
            jugadas_posibles = [0,1,2,3,4,5]
        else:
            jugadas_posibles = [7,8,9,10,11,12]
        # la lista para borrar
        elements_to_delete = []
        # guardamos las jugadas que estan vacias
        for x in jugadas_posibles:
            if self.tablero[x] == 0:
                elements_to_delete.append(x)
        
        # Borramos esas posibilidades
        for x in elements_to_delete:
            jugadas_posibles.remove(x)

        # Si regresa vacio es que es Game Over, esto lo hace handle el monte_carlo_mancala.py
        return jugadas_posibles


    def get_ganador(self, end=False):
        """ Aqui hay que contar las casillas de las esquinas para los jugadores """
        jugador_1 = sum(self.tablero[0:7])
        jugador_2 = sum(self.tablero[7:14])
        if end:
            print('Puntaje del jugado: {}'.format(jugador_2))
            print('Puntaje del AI: {}'.format(jugador_1))

        if (jugador_1 > jugador_2):
            return 1
        elif(jugador_1 < jugador_2):
            return 2
        else:
            return 0


    def get_primera_jugada(self):
        return self.jugada_inicial


    def set_primera_jugada(self, jugada_1):
        self.jugada_inicial = jugada_1

    def print_tablero(self):
        return self.tablero

    def __str__(self):
        tabl_reverse = self.tablero[::-1]
        tablero_en_string = " " + str(tabl_reverse[8:]) + "\n"
        tablero_en_string += str(self.tablero[6])+ "                  "+ str(self.tablero[13]) + "\n"
        tablero_en_string += " " + str(self.tablero[7:13])
        return tablero_en_string