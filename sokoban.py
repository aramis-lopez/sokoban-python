class Sokoban:

    mapa = [] # mapa del juego
    personaje_columna = 0
    personaje_fila = 0
    mapa1 = []

    def __init__(self, ):
        #Construir mapa
        self.mapa = [
            [3,3,3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,2,2,4,4,4,4,3],
            [3,4,4,2,2,2,4,1,4,4,3],
            [3,4,4,4,2,4,4,4,4,4,3],
            [3,4,4,2,4,2,4,4,4,4,3],
            [3,4,4,1,4,4,0,2,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3,3,3]
        ]

        self.mapa1 = [
            [4,4,4,4,4,4,4,4,4,4,4],
            [4,4,4,4,4,4,4,4,4,4,4],
            [4,4,4,4,4,4,4,4,4,4,4],
            [4,4,4,4,4,4,4,4,4,4,4],
            [4,4,4,4,1,4,4,2,4,4,4],
            [4,4,4,4,4,4,4,4,4,4,4],
            [4,4,4,4,4,4,0,4,4,4,4],
            [4,4,4,4,4,4,4,4,4,4,4],
            [4,4,4,4,4,4,4,4,4,4,4]
        ]

        #Posicion del jugador
        self.personaje_columna = 6
        self.personaje_fila = 6

        #Definir posicion del jugador
        #self.mapa 

    def pintar_mapa(self,):
        for fila in self.mapa:
            print(fila)       
    def cambiar_mapa(self):
        #cambia de nivel al ya no aver ninguna caja
        if not any(1 in fila for fila in self.mapa):
            self.mapa = self.mapa1
            self.personaje_columna = 6  # Nuevas coordenadas del personaje
            self.personaje_fila = 6

# movimientos apoder hacer [2,1,0]-[6,0,4]
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
        elif (self.mapa[self.personaje_fila][self.personaje_columna ]) == 5: #validamos si somos personaje meta
                if(self.mapa[self.personaje_fila][self.personaje_columna-2]) == 2: #validar si tiene meta a alado de la caja
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2, 0, 6
                    self.personaje_columna -= 1
        
        elif(self.mapa[self.personaje_fila][self.personaje_columna -2]) == 2: #Validar si tenemos meta alado de la caja
            #[posicion_actual, posicion_destino, caja_destino]
            self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4, self.mapa[self.personaje_fila][self.personaje_columna], 6
            self.personaje_columna -= 1

        # elif(self.mapa[self.personaje_fila][self.personaje_columna])
        else: #Pared alado de la caja
            print('No se puede mover la caja, tienes una pared.')
            return self.mapa

# movimientos apoder hacer [4,0]-[0,4]
    def mover_izquierda(self):
        if self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4: #Validar si hay pasillo
           if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #validar si somos personaje_meta
                #[posicion_actual, posicion_destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1] = 2, 0,
                self.personaje_columna -= 1
           else:
                #Movemos personaje a la izquierda
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1] = self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna]
                self.personaje_columna -= 1    
        elif self.mapa[self.personaje_fila][self.personaje_columna -1] == 2: #validar si tiene meta
                if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #validar si somos personaje meta
                 #[posicion_actual, posicion_destino] para convertirnos en personaje meta sin tener una caja enfrente
                 self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1] = 2, 5,
                 self.personaje_columna -= 1
                else:
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1] = 4, 5,
                    self.personaje_columna -= 1 #si no somos personaje meta dejaremos un espacio
        elif self.mapa[self.personaje_fila][self.personaje_columna -1] == 1: #Valida si tienes caja
            self.mover_izquierda_caja()
        elif self.mapa[self.personaje_fila][self.personaje_columna -1] == 6: #Valida si tienes caja_meta
            if(self.mapa[self.personaje_fila][self.personaje_columna -2]) == 4: #Validar si tienes pasillo alado de la caja_meta
                if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5:#valida si somos personaje meta
                    #[posicion_actual, posicion_destio, ceja_meta_destino]
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2, 5, 1
                    self.personaje_columna -= 1
                else:
                #[posicion_actual, posicion_destino, caja_meta-destino]
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4, 5, 1
                    self.personaje_columna -= 1
            elif self.mapa[self.personaje_fila][self.personaje_columna -1] == 6: #valida si tenemos caja_meta
                if(self.mapa[self.personaje_fila][self.personaje_columna -2]) == 2: #valida si tenemos meta enfrente de caja_meta
                    if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #valida si somos personaje meta 
                        #[posicion_actual, posicion_destino, posicion_caja]
                        self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2, 5, 6
                        self.personaje_columna -= 1
                    else:
                        self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1], self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4, 5, 6
                        self.personaje_columna -= 1
                        #salida

        else:
            print('No se puede mover al jugar, se llego al limite del mapa')
            return self.mapa

#los movimintos del personaje
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

#            
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
        elif (self.mapa[self.personaje_fila][self.personaje_columna ]) == 5:  #validamos si somos personaje meta
                if(self.mapa[self.personaje_fila][self.personaje_columna +2]) == 2: #validar si tiene meta a alado de la caja
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna +1], self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2, 0, 6
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
           if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #validar si somos personaje_meta
                #[posicion_actual, posicion_destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna +1] = 2, 0,
                self.personaje_columna += 1
           else:
                #Movemos personaje a la izquierda
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna +1] = self.mapa[self.personaje_fila][self.personaje_columna +1], self.mapa[self.personaje_fila][self.personaje_columna]
                self.personaje_columna += 1    
        elif self.mapa[self.personaje_fila][self.personaje_columna +1] == 2: #validar si tiene meta
                if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #validar si somos personaje meta
                 #[posicion_actual, posicion_destino] para convertirnos en personaje meta sin tener una caja enfrente
                 self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna +1] = 2, 5,
                 self.personaje_columna += 1
                else:
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna +1] = 4, 5,
                    self.personaje_columna += 1       
        elif self.mapa[self.personaje_fila][self.personaje_columna +1] == 1: #Valida si tienes caja
            self.mover_derecha_caja()
        elif self.mapa[self.personaje_fila][self.personaje_columna +1] == 6: #Valida si tienes caja_meta
            if(self.mapa[self.personaje_fila][self.personaje_columna +2]) == 4: #Validar si tienes pasillo alado de la caja_meta
                if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5:#valida si somos personaje meta
                    #[posicion_actual, posicion_destio, ceja_meta_destino]
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna + 1], self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2, 5, 1
                    self.personaje_columna += 1
                else:
                #[posicion_actual, posicion_destino, caja_meta-destino]
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna + 1], self.mapa[self.personaje_fila][self.personaje_columna + 2] = 4, 5, 1
                    self.personaje_columna += 1
            elif self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6: #valida si tenemos caja_meta
                if(self.mapa[self.personaje_fila][self.personaje_columna + 2]) == 2: #valida si tenemos meta enfrente de caja_meta
                    if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #valida si somos personaje meta 
                        #[posicion_actual, posicion_destino, posicion_caja]
                        self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna + 1], self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2, 5, 6
                        self.personaje_columna += 1
                    else:
                        self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna + 1], self.mapa[self.personaje_fila][self.personaje_columna + 2] = 4, 5, 6
                        self.personaje_columna += 1
                        #salida
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
        elif (self.mapa[self.personaje_fila][self.personaje_columna ]) == 5: #validar si somos personaje meta 
                if(self.mapa[self.personaje_fila -2][self.personaje_columna]) == 2: #validar si tiene meta a alado de la caja
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila -1][self.personaje_columna], self.mapa[self.personaje_fila - 2][self.personaje_columna] = 2, 0, 6
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
           if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #validar si somos personaje_meta
                #[posicion_actual, posicion_destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila -1][self.personaje_columna] = 2, 0,
                self.personaje_fila -= 1
           else:
                #Movemos personaje a la izquierda
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila -1][self.personaje_columna] = self.mapa[self.personaje_fila -1][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna]
                self.personaje_fila -= 1    
        elif self.mapa[self.personaje_fila -1][self.personaje_columna] == 2: #validar si tiene meta
                if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #validar si somos personaje meta
                 #[posicion_actual, posicion_destino] para convertirnos en personaje meta sin tener una caja arriba
                 self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila - 1][self.personaje_columna] = 2, 5,
                 self.personaje_fila -= 1
                else:
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila - 1][self.personaje_columna] = 4, 5,
                    self.personaje_fila -= 1 
        elif self.mapa[self.personaje_fila -1][self.personaje_columna] == 1: #Valida si tienes caja
            self.mover_arriba_caja()
        elif self.mapa[self.personaje_fila -1][self.personaje_columna] == 6: #Valida si tienes caja_meta
            if(self.mapa[self.personaje_fila -2][self.personaje_columna]) == 4: #Validar si tienes pasillo arriba de la caja_meta
                if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5:#valida si somos personaje meta
                    #[posicion_actual, posicion_destio, ceja_meta_destino]
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila - 1][self.personaje_columna], self.mapa[self.personaje_fila -2][self.personaje_columna] = 2, 5, 1
                    self.personaje_fila -= 1
                else:
                #[posicion_actual, posicion_destino, caja_meta-destino]
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila - 1][self.personaje_columna], self.mapa[self.personaje_fila - 2][self.personaje_columna] = 4, 5, 1
                    self.personaje_fila -= 1
            elif self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6: #valida si tenemos caja_meta
                if(self.mapa[self.personaje_fila - 2][self.personaje_columna]) == 2: #valida si tenemos meta enfrente de caja_meta
                    if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #valida si somos personaje meta 
                        #[posicion_actual, posicion_destino, posicion_caja]
                        self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila - 1][self.personaje_columna], self.mapa[self.personaje_fila - 2][self.personaje_columna] = 2, 5, 6
                        self.personaje_fila -= 1 
                    else:
                        self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila - 1][self.personaje_columna], self.mapa[self.personaje_fila - 2][self.personaje_columna] = 4, 5, 6
                        self.personaje_fila -= 1
                        #salida
        
        else: #pared arriba de la caja
            print('No se puede mover la caja, tienes una pared.')
            return self.mapa

            

        


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
        elif (self.mapa[self.personaje_fila][self.personaje_columna ]) == 5: #validamos si somos personaje meta
                if(self.mapa[self.personaje_fila + 2][self.personaje_columna]) == 2 :#validar si tiene meta a alado de la caja
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila + 1][self.personaje_columna ], self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2, 0, 6
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
           if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #validar si somos personaje_meta
                #[posicion_actual, posicion_destino]
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila +1][self.personaje_columna] = 2, 0,
                self.personaje_fila += 1
           else:
                #Movemos personaje a la izquierda
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila +1][self.personaje_columna] = self.mapa[self.personaje_fila +1][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna]
                self.personaje_fila += 1    
        elif self.mapa[self.personaje_fila +1][self.personaje_columna] == 2: #validar si tiene meta
                if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #validar si somos personaje meta
                 #[posicion_actual, posicion_destino] para convertirnos en personaje meta sin tener una caja abajo
                 self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila + 1][self.personaje_columna] = 2, 5,
                 self.personaje_fila += 1
                else:
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila + 1][self.personaje_columna] = 4, 5,
                    self.personaje_fila += 1
        elif self.mapa[self.personaje_fila +1][self.personaje_columna] == 1: #Valida si tienes caja
            self.mover_abajo_caja()
        elif self.mapa[self.personaje_fila +1][self.personaje_columna] == 6: #Valida si tienes caja_meta
            if(self.mapa[self.personaje_fila +2][self.personaje_columna]) == 4: #Validar si tienes pasillo abajo de la caja_meta
                if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5:#valida si somos personaje meta
                    #[posicion_actual, posicion_destio, ceja_meta_destino]
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila + 1][self.personaje_columna], self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2, 5, 1
                    self.personaje_fila += 1
                else:
                #[posicion_actual, posicion_destino, caja_meta-destino]
                    self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila + 1][self.personaje_columna], self.mapa[self.personaje_fila + 2][self.personaje_columna] = 4, 5, 1
                    self.personaje_fila += 1
            elif self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6: #valida si tenemos caja_meta
                if(self.mapa[self.personaje_fila + 2][self.personaje_columna]) == 2: #valida si tenemos meta abajo de caja_meta
                    if(self.mapa[self.personaje_fila][self.personaje_columna]) == 5: #valida si somos personaje meta 
                        #[posicion_actual, posicion_destino, posicion_caja]
                        self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila + 1][self.personaje_columna], self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2, 5, 6
                        self.personaje_fila += 1 
                    else:
                        self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila + 1][self.personaje_columna], self.mapa[self.personaje_fila + 2][self.personaje_columna] = 4, 5, 6
                        self.personaje_fila += 1
                        #salida
        
        else: #pared arriba de la caja
            print('No se puede mover la caja, tienes una pared.')
            return self.mapa
    
    
    def jugar(self):
        while True:
            self.cambiar_mapa()
            self.pintar_mapa()
            direccion = input("¿En qué dirección quieres mover al personaje? (a o A - izquierda, d o D - derecha): ")
            self.mover_personaje(direccion)


sokobanObjeto = Sokoban()
sokobanObjeto.jugar()