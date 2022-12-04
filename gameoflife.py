# I did it with some of the help of DotCsv
import pygame
import numpy as np
import time

pygame.init()

# Se crea la pantalla del juego
width, height = 1250, 600
screen = pygame.display.set_mode((width, height))
bg = 25, 25, 25
screen.fill(bg)
# Se dan las dimensiones de cada célula
nxC, nyC = 45, 35
dimCW = width / nxC
dimCH = height / nyC
# Inician todas en cero, o sea muertas
gameState = np.zeros((nxC,nyC))
# Se escribe que celula estara viva
gameState[21,21] = 1
gameState[22,21] = 1
gameState[23,21] = 1
gameState[20,22] = 1
gameState[24,22] = 1
gameState[21,24] = 1
gameState[22,24] = 1
gameState[23,24] = 1
gameState[32, 24] = 1
gameState[21,29] = 1
gameState[22,29] = 1
gameState[23,29] = 1
gameState[20,30] = 1
gameState[24,30] = 1
gameState[21,32] = 1
gameState[22,32] = 1
gameState[23,32] = 1
# Pausa o inicio del juego
pauseExect = False
mouseClick = 0
#Incrementar velocidad y eficacia
allowed_events = (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT)
for event in allowed_events:
    pygame.event.set_allowed(event)

# Calculos
while 1:
    # Se hace una copia del juego para progresar con los resultados de las proximas generaciones
    new_gS = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.1) # Esta es el tiempo de cada generacion

    ev = pygame.event.get() # Cuando se ingresa un evento
    for event in ev:
        mouseClick = pygame.mouse.get_pressed()
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            new_gS[celX, celY] = not mouseClick[2]

    for y in range(0, nyC):
        for x in range(0, nxC):
            if not pauseExect:
                n_neigh = gameState[(x - 1) % nxC,  (y - 1) % nyC] + \
                          gameState[ x % nxC,       (y - 1) % nyC] + \
                          gameState[(x + 1) % nxC,  (y - 1) % nyC] + \
                          gameState[(x - 1) % nxC,  (y) % nyC] + \
                          gameState[(x + 1) % nxC,  (y) % nyC] + \
                          gameState[(x - 1) % nxC,  (y + 1) % nyC]+ \
                          gameState[(x) % nxC,      (y + 1) % nyC] + \
                          gameState[(x + 1) % nxC,  (y + 1) % nyC]
                # Una celula muerta con exactamente 3 celulas vecinas vivas "nace"
                if gameState[x, y] == 0 and n_neigh == 3:
                    new_gS[x,y] = 1
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    new_gS[x, y] = 0
                 # Una celula viva con 2 o 3 celulas vecinas vivas sigue con vida, en otro caso, muere

                poly = [( x   * dimCW,  y * dimCH),
                        ((x+1) * dimCW,  y * dimCH),
                        ((x+1) * dimCW, (y+1) * dimCH),
                        ( x   * dimCW, (y+1) * dimCH)]
                if new_gS[x, y] == 0:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
                else:
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    gameState = np.copy(new_gS)
    pygame.display.flip()
