class Sokoban:

    mapa = [] # mapa del juego
    personaje_columna = 0
    personaje_fila = 0

    def __init__(self, ):
        #Construir mapa
        self.mapa = [
            [3,3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,4,4,3],
            [3,4,4,2,1,4,4,4,4,3],
            [3,4,4,4,4,2,1,4,4,3],
            [3,4,4,4,4,4,4,0,4,3],
            [3,3,3,3,3,3,3,3,3,3]
        ]

        #Posicion del jugador
        self.personaje_columna = 7
        self.personaje_fila = 4

        #Definir posicion del jugador
        #self.mapa 

    def pintar_mapa(self,):
        for fila in self.mapa:
            print(fila)

#
    def mover_izquierda_caja(self):
        if(self.mapa[self.personaje_fila][self.personaje_columna -2]) == 4: #Validar si tienes pasillo alado de la caja
            if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #Validar si esta en personaje_meta
                #[posicion_actual, posicion_destino, caja_destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2, 0, 1
                self.personaje_columna -= 1
            else: #Personaje no esta en meta, mover caja
                #[posicion_actual, posicion_destino, caja_destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4, self.mapa[self.personaje_fila][self.personaje_columna], 1
                self.personaje_columna -= 1
        elif(self.mapa[self.personaje_fila][self.personaje_columna -2]) == 2: #Validar si tenemos meta alado de la caja
            #[posicion_actual, posicion_destino, caja_destino]
            self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4, self.mapa[self.personaje_fila][self.personaje_columna], 6
            self.personaje_columna -= 1
        else: #Pared alado de la caja
            print('No se puede mover la caja, tienes una pared.')
            return self.mapa


    def mover_izquierda(self):
        if self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4: #Validar si hay pasillo
                #Movemos personaje a la izquierda
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1] = self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna]
                self.personaje_columna -= 1
        elif self.mapa[self.personaje_fila][self.personaje_columna -1] == 1: #Valida si tienes caja
            self.mover_izquierda_caja()
        elif self.mapa[self.personaje_fila][self.personaje_columna -1] == 6: #Valida si tienes caja_meta
            if(self.mapa[self.personaje_fila][self.personaje_columna -2]) == 4: #Validar si tienes pasillo alado de la caja_meta
                #[posicion_actual, posicion_destino, caja_meta-destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4, 5, 1
                self.personaje_columna -= 1
        else:
            print('No se puede mover al jugar, se llego al limite del mapa')
            return self.mapa


    def mover_personaje(self, direccion):
        if direccion.lower() == 'a':
            self.mover_izquierda()
        elif direccion.lower() == 'd':
            self.mover_derecha()
        elif direccion.lower() == 'w':
            self.mover_arriba()
        elif direccion.lower() == 's':
            self.mover_abajo()
        else:
            print("Dirección no válida. Por favor, introduce 'a','d','w','s' para mover a su personaje.")
            return self.mapa

            
    def mover_derecha_caja(self):
        if(self.mapa[self.personaje_fila][self.personaje_columna +2]) == 4: #Validar si tienes pasillo alado de la caja
            if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #Validar si esta en personaje_meta
                #[posicion_actual, posicion_destino, caja_destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna +1], self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2, 0, 1
                self.personaje_columna += 1
            else: #Personaje no esta en meta, mover caja
                #[posicion_actual, posicion_destino, caja_destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna +1], self.mapa[self.personaje_fila][self.personaje_columna + 2] = 4, self.mapa[self.personaje_fila][self.personaje_columna], 1
                self.personaje_columna += 1
        elif(self.mapa[self.personaje_fila][self.personaje_columna +2]) == 2: #Validar si tenemos meta alado de la caja
            #[posicion_actual, posicion_destino, caja_destino]
            self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna +1], self.mapa[self.personaje_fila][self.personaje_columna + 2] = 4, self.mapa[self.personaje_fila][self.personaje_columna], 6
            self.personaje_columna += 1
        else: #Pared alado de la caja
            print('No se puede mover la caja, tienes una pared.')
            return self.mapa       
    
    
    def mover_derecha(self):
        if self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4: #Validar si hay pasillo
                #Movemos personaje a la izquierda
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna +1] = self.mapa[self.personaje_fila][self.personaje_columna +1], self.mapa[self.personaje_fila][self.personaje_columna]
                self.personaje_columna += 1
        elif self.mapa[self.personaje_fila][self.personaje_columna +1] == 1: #Valida si tienes caja
            self.mover_derecha_caja()
        elif self.mapa[self.personaje_fila][self.personaje_columna +1] == 6: #Valida si tienes caja_meta
            if(self.mapa[self.personaje_fila][self.personaje_columna +2]) == 4: #Validar si tienes pasillo alado de la caja_meta
                #[posicion_actual, posicion_destino, caja_meta-destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna +1], self.mapa[self.personaje_fila][self.personaje_columna + 2] = 4, 5, 1
                self.personaje_columna += 1
        else:
            print('No se puede mover al jugar, se llego al limite del mapa')
            return self.mapa
    
    def mover_arriba_caja(self):
        if(self.mapa[self.personaje_fila -2][self.personaje_columna]) == 4: #Validar si tienes pasillo alado de la caja
            if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #Validar si esta en personaje_meta
                #[posicion_actual, posicion_destino, caja_destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila -1][self.personaje_columna], self.mapa[self.personaje_fila - 2][self.personaje_columna] = 2, 0, 1
                self.personaje_fila -= 1
            else: #Personaje no esta en meta, mover caja
                #[posicion_actual, posicion_destino, caja_destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila -1][self.personaje_columna], self.mapa[self.personaje_fila - 2][self.personaje_columna] = 4, self.mapa[self.personaje_fila][self.personaje_columna], 1
                self.personaje_fila -= 1
        elif(self.mapa[self.personaje_fila -2][self.personaje_columna]) == 2: #Validar si tenemos meta alado de la caja
            #[posicion_actual, posicion_destino, caja_destino]
            self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila -1][self.personaje_columna], self.mapa[self.personaje_fila - 2][self.personaje_columna] = 4, self.mapa[self.personaje_fila][self.personaje_columna], 6
            self.personaje_fila -= 1
        else: #Pared alado de la caja
            print('No se puede mover la caja, tienes una pared.')
            return self.mapa
    

    def mover_arriba(self):  
        if self.mapa[self.personaje_fila -1][self.personaje_columna] == 4: #Validar si hay pasillo
                #Movemos personaje a la izquierda
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila-1][self.personaje_columna] = self.mapa[self.personaje_fila -1][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna]
                self.personaje_fila -= 1
        elif self.mapa[self.personaje_fila -1][self.personaje_columna] == 1: #Valida si tienes caja
            self.mover_arriba_caja()
        elif self.mapa[self.personaje_fila -1][self.personaje_columna] == 6: #Valida si tienes caja_meta
            if(self.mapa[self.personaje_fila -2][self.personaje_columna]) == 4: #Validar si tienes pasillo alado de la caja_meta
                #[posicion_actual, posicion_destino, caja_meta-destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila -1][self.personaje_columna], self.mapa[self.personaje_fila - 2][self.personaje_columna] = 4, 5, 1
                self.personaje_fila -= 1


    def mover_abajo_caja(self):
        if(self.mapa[self.personaje_fila +2][self.personaje_columna]) == 4: #Validar si tienes pasillo alado de la caja
            if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #Validar si esta en personaje_meta
                #[posicion_actual, posicion_destino, caja_destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila +1][self.personaje_columna], self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2, 0, 1
                self.personaje_fila += 1
            else: #Personaje no esta en meta, mover caja
                #[posicion_actual, posicion_destino, caja_destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila +1][self.personaje_columna], self.mapa[self.personaje_fila + 2][self.personaje_columna] = 4, self.mapa[self.personaje_fila][self.personaje_columna], 1
                self.personaje_fila += 1
        elif(self.mapa[self.personaje_fila +2][self.personaje_columna]) == 2: #Validar si tenemos meta alado de la caja
            #[posicion_actual, posicion_destino, caja_destino]
            self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila +1][self.personaje_columna], self.mapa[self.personaje_fila + 2][self.personaje_columna] = 4, self.mapa[self.personaje_fila][self.personaje_columna], 6
            self.personaje_fila += 1
        else: #Pared alado de la caja
            print('No se puede mover la caja, tienes una pared.')
            return self.mapa
    

    def mover_abajo(self):  
        if self.mapa[self.personaje_fila +1][self.personaje_columna] == 4: #Validar si hay pasillo
                #Movemos personaje a la izquierda
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila+1][self.personaje_columna] = self.mapa[self.personaje_fila +1][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna]
                self.personaje_fila += 1
        elif self.mapa[self.personaje_fila +1][self.personaje_columna] == 1: #Valida si tienes caja
            self.mover_abajo_caja()
        elif self.mapa[self.personaje_fila +1][self.personaje_columna] == 6: #Valida si tienes caja_meta
            if(self.mapa[self.personaje_fila +2][self.personaje_columna]) == 4: #Validar si tienes pasillo alado de la caja_meta
                #[posicion_actual, posicion_destino, caja_meta-destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila +1][self.personaje_columna], self.mapa[self.personaje_fila + 2][self.personaje_columna] = 4, 5, 1
                self.personaje_fila += 1
    
        if self.personaje_columna == len(self.mapa[self.personaje_fila]) - 1:
            print("No se puede mover hacia abajo. Llegaste al final del mapa.")
            return self.mapa
        else:
            if self.mapa[self.personaje_fila +1][self.personaje_columna] == 3:
                return self.mapa
            else:
              self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila +1][self.personaje_columna] = self.mapa[self.personaje_fila +1][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna]
              self.personaje_fila += 1
    
    def jugar(self):
        while True:
            self.pintar_mapa()
            direccion = input("¿En qué dirección quieres mover al personaje? (a o A - izquierda, d o D - derecha): ")
            self.mover_personaje(direccion)


sokobanObjeto = Sokoban()
sokobanObjeto.jugar()

