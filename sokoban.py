import copy

class Sokoban:

    # mapa del juego
    mapa = []

    #Coordenadas personaje
    personaje_columna = 0
    personaje_fila = 0

    #Registro de niveles
    nivel_actual = 0
    niveles_disponibles = [0, 1, 2, 3]

    #Power up
    powerup_count = 0  # Contador de powerups utilizados
    powerup_max_count = 2

    #Emojis
    emojis = {
        0: '🏃',
        1: '📦',
        2: '🏁',
        3: '🧱',
        4: '  ',
        5: '🙇',
        6: '🚩',
    }

    #Arreglo de mapas para jugar
    mapas = [
        [
            [3,3,3,3,3,3,3,3,3,3,3],
            [3,0,4,4,3,2,2,2,4,4,3],
            [3,4,4,4,1,1,4,4,3,3,3],
            [3,4,4,1,4,4,4,4,3,4,4],
            [3,4,4,4,3,3,3,3,3,4,4],
            [3,4,4,4,3,4,4,4,4,4,4],
            [3,3,3,3,3,4,4,4,4,4,4],
            [4,4,4,4,4,4,4,4,4,4,4],
            [4,4,4,4,4,4,4,4,4,4,4]
        ],    
        [
            [4,4,3,3,3,3,3,3,3,3,3],
            [4,4,3,4,4,4,4,4,4,4,3],
            [4,4,3,4,4,4,4,4,4,4,3],
            [4,4,3,4,1,4,4,4,4,4,3],
            [4,4,3,4,4,3,4,4,4,3,3],
            [4,3,3,4,3,3,3,3,3,3,4],
            [4,3,0,1,4,4,4,4,4,3,4],
            [4,3,2,4,2,4,4,4,4,3,4],
            [4,3,3,3,3,3,3,3,3,3,4]
        ],    
        [
            [4,4,4,3,3,3,3,3,4,4,4],
            [4,3,3,3,4,4,4,3,4,4,4],
            [4,3,0,1,4,3,4,3,4,4,4],
            [4,3,1,1,4,4,4,3,4,4,4],
            [3,3,4,3,3,4,3,3,4,4,4],
            [3,4,4,2,4,4,4,3,4,4,4],
            [3,2,4,4,4,4,4,3,4,4,4],
            [3,3,4,4,4,2,4,3,4,4,4],
            [4,3,3,3,3,3,3,3,4,4,4]
        ],    
        [
            [3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4],
            [3,4,2,4,4,4,4,4,4,4,3,4,4,4,4,4],
            [3,4,4,4,2,3,4,4,3,4,3,4,4,4,4,4],
            [3,3,1,3,4,4,4,4,4,4,3,4,4,4,4,4],
            [4,3,0,4,3,4,4,4,4,4,3,4,4,4,4,4],
            [4,3,3,1,4,4,4,4,3,4,3,4,4,4,4,4],
            [3,3,4,4,4,4,3,4,4,2,3,4,4,4,4,4],
            [3,4,1,4,3,4,4,4,4,4,3,4,4,4,4,4],
            [3,4,4,1,4,4,4,4,3,2,3,4,4,4,4,4],
            [3,4,4,4,3,4,4,4,4,4,3,4,4,4,4,4],
            [3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4]
        ],    
    ]
    posiciones_personaje = [
        [1,1],
        [2,6],
        [2,2],
        [2,4],
        [6,6],
    ]

    def __init__(self):
        #Asignamos mapa por nivel
        self.mapa = copy.deepcopy(self.mapas[self.nivel_actual])

        #Asignamos la posicion del jugador
        self.personaje_columna = self.posiciones_personaje[self.nivel_actual][0]
        self.personaje_fila = self.posiciones_personaje[self.nivel_actual][1]

    def pintar_mapa(self):
        print("\n")
        print(f'************ Nivel {self.nivel_actual} ************')
        for fila in self.mapa:
            for numero in fila:
                print(self.emojis[numero], end=' ')
            print()

    def pintar_menu(self):
        print("=" * 40)
        print(f"Posición actual del personaje: [{self.personaje_columna}, {self.personaje_fila}]")
        print("=" * 40)
        direccion = input("¿En qué dirección quieres mover al personaje? (a/d/s/w): ").strip().lower()
        self.mover_personaje(direccion)

    def reseter_nivel(self):
        #Cambiamos referencia al mapa
        self.mapa = copy.deepcopy(self.mapas[self.nivel_actual])

        #Reseteamos posicion del personaje
        self.personaje_columna = self.posiciones_personaje[self.nivel_actual][0]
        self.personaje_fila = self.posiciones_personaje[self.nivel_actual][1]

        #Resetear el power up
        self.powerup_count = 0

    def seleccionar_nivel(self): 
        print("\n" + "=" * 40)
        print("           Selección de Nivel")
        print("=" * 40)
        print("Niveles Disponibles:")

        for i, nivel in enumerate(self.niveles_disponibles):
            print(f"  [{i}] Nivel {nivel}")

        while True:
            opcion = input("Selecciona un nivel (0, 1, 2, 3): ").strip()

            if opcion.isdigit() and int(opcion) in self.niveles_disponibles:
                return int(opcion)
            else:
                print("Opción no válida. Por favor, selecciona un nivel válido.")

    def validar_mapa(self):
        # Verifica si ya no hay cajas
        if not any(1 in fila for fila in self.mapa):
            self.pintar_mapa()

            print("\n" + "=" * 40)
            print("           ¡Nivel Completado!")
            print("=" * 40)
            print("¡Felicidades! Has superado el nivel.")

            while True:
                print("Opciones:")
                print("  - Presiona 'R' para reiniciar el nivel.")
                print("  - Presiona 'S' para avanzar al siguiente nivel.")
                print("  - Presiona 'Q' para salir del juego.")

                accion = input("Elige una opción: ").strip().lower()

                if accion == 'r':
                    self.reseter_nivel()
                    return
                elif accion == 's':
                    if self.nivel_actual + 1 < len(self.mapas):
                        self.nivel_actual += 1
                        self.reseter_nivel()
                        return
                    else:
                        print("¡Felicidades! Has completado todos los niveles.")
                        return
                elif accion == 'q':
                    print("¡Gracias por jugar!")
                    exit()
                else:
                    print("Opción no válida. Por favor, elige una opción válida.")

        else:
            return


    def powerup(self):
        # Verificar si se puede usar el powerup
        if self.powerup_count < self.powerup_max_count:
            print("¡Has usado el powerup!")
            self.powerup_count += 1
        else:
            print("Ya has usado el powerup el máximo de veces permitido en este mapa.")

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
        elif direccion.lower() == 'q':
            self.powerup()
        elif (direccion.lower() == 'c'):
            #Reseteamos el nivel actual
            self.reseter_nivel()
        else:
            print("Dirección no válida. Por favor, introduce 'a','d','w','s' o 'c' para mover a su personaje")
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
    
    def powerup (self):
        if self.powerup_count < 2:  # Verificar si se han usado menos de dos powerups
            if self.mapa[self.personaje_fila][self.personaje_columna - 1] == 3: # verifica si tiene pared a la izquierda
                # quita la pared 
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna -1] = 4, 0,
                # Cambia posicion de personaje
                self.personaje_columna -= 1

                # Sube power up counter
                print("Has utilizado un powerup.")
                self.powerup_count += 1

        if self.powerup_count < 2:
            if self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3:
                self.mapa[self.personaje_fila][self.personaje_columna], self.mapa[self.personaje_fila][self.personaje_columna +1] = 4, 0,
                self.personaje_columna += 1
                print("Has utilizado un powerup.")
                self.powerup_count += 1
        else:
            print("Ya has utilizado todos los powerups disponibles para este mapa.")
    
    def pintar_menu_juego(self):
        print("\n" + "=" * 40)
        print("           MENÚ DE JUEGO")
        print("Opciones:")
        print("  - Presiona 'C' para reiniciar el nivel.")
        print("  - Presiona 'Q' para usar el power up.")
        print("=" * 40)
        print("Direcciones:")
        print("  - Presiona 'A' para mover a la izquierda.")
        print("  - Presiona 'D' para mover a la derecha.")
        print("  - Presiona 'S' para mover hacia abajo.")
        print("  - Presiona 'W' para mover hacia arriba.")
        print("=" * 40 + "\n")

    def jugar(self):
        self.pintar_menu_juego()

        #Selecciona el nivel por primera vez
        opcion_final = self.seleccionar_nivel()
        self.nivel_actual = opcion_final
        self.reseter_nivel()
        while True:
            self.pintar_mapa()
            self.pintar_menu()
            self.validar_mapa()


sokobanObjeto = Sokoban()
sokobanObjeto.jugar()