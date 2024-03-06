class Sokoban:

    mapa = [] # mapa del juego
    personaje_columna = 0
    personaje_fila = 0

    def __init__(self, ):
        #Construir mapa
        self.mapa = [
            [3,3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,0,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3,3]
        ]

        #Posicion del jugador
        self.personaje_columna = 4
        self.personaje_fila = 4

        #Definir posicion del jugador
        #self.mapa 

    def pintar_mapa(self,):
        for fila in self.mapa:
            print(fila)

    def mover_izquierda(self):
        if self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4: 
                print("el personaje no se puede mover hacia la izquierda. Llegaste al limite del mapa.")
                return self.mapa
        else:
            if self.mapa[self.personaje_fila][self.personaje_columna -1] == 3: #Valida si tienes pared
                return self.mapa
            else:
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1] = self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna]
                self.personaje_columna -= 1


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

            
    def mover_derecha(self):
        if self.personaje_columna == len(self.mapa[self.personaje_fila]) - 1:
            print("No se puede mover hacia la derecha. Llegaste al final del mapa.")
            return self.mapa
        else:
            if self.mapa[self.personaje_fila][self.personaje_columna +1] == 3:
                return self.mapa
            else:
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna +1] = self.mapa[self.personaje_fila][self.personaje_columna +1], self.mapa[self.personaje_fila][self.personaje_columna]
                self.personaje_columna += 1

    def mover_arriba(self):  
        if self.personaje_columna == len(self.mapa[self.personaje_fila]) - 1:
            print("No se puede mover hacia arriba. Llegaste al final del mapa.")
            return self.mapa
        else:
            if self.mapa[self.personaje_fila -1][self.personaje_columna] == 3:
                return self.mapa
            else:
               self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila -1][self.personaje_columna] = self.mapa[self.personaje_fila -1][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna]
               self.personaje_fila -= 1
    
    def mover_abajo(self):  
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
