import random as r
from art import * # pip install art
from colorama import Fore, Style
import time
import sys
import tqdm

# ----------------------------------------- General Functions --------------------------------------------------------
# Funcion inicializar
def startArray(r,c):
    m = []
    for i in range(r):
        a = ['*']*c
        m.append(a)
    return m
# Muestra el array
def showA(mF):
    print("1        2       3       4")
    for i in range(len(mF)):
        print()
        for j in range(len(mF[i])):
            print(mF[i][j],"\t",end=' ')
        print(i+1)
# Muestra que ganó el juego
def gameWon(pInG,pT,pInGP):
    a = "El ganador fue {}".format(pInG[pInGP]) 
    tprint(a)
    print("\n\t\t\tLe tomó un total de {} turnos para ganar!\n".format(pT[pInGP]))

# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- End General Functions -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.

# ----------------------------------------------- Menu --------------------------------------------------------
# Mostrar el menú principal
def mainMenu():
    print(Fore.RED)
    tprint("Memorama",font="random")
    print(Fore.BLUE + "-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- Menu -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")
    print(Style.RESET_ALL)
    print("\t\t\t \t{} Selecciona una opción {}\n".format(art("woman"),art("woman")) )
    print("\t\t\t \t\tJugar --> 1\n")
    print("\t\t\t \t\tInstrucciones --> 2\n")
    print("\t\t\t \t\tEstadisticas --> 3\n")
    print(Fore.RED + "\t\t\t \t\tCerrar juego :c --> 0\n")
    print(Style.RESET_ALL)
    mO = int(input("\t\t\t \t\tOpción: "))
    print(Fore.BLUE + "\n-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")
    print(Style.RESET_ALL)

    selectOption(mO)

def selectOption(mO):
    mL = 1
    while mL:
        if mO == 1:
            mO = game()
        elif mO == 2:
            mO = instructions()
        elif mO == 3:
            mO = stats()
        elif mO == 0:
            print("\t\t\t \t\tNos vemos la próxima\n")
            print(Fore.BLUE + "\n-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")
            mL = 0
        else: # Respuesta si es que esta fuera del rango
            print(Fore.RED +"\t\t\t \tJuego finalizado\n")
            mL = 0
            print(Fore.BLUE + "\n-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")

# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. End menu -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.

# ----------------------------------------------- Game --------------------------------------------------------
def game():

    # -------------------------------------------- Initial considerations  --------------------------------------------------------

    P1 = input(("\t\t\t \t\tIngresa el nombre del primer jugador: "))
    P2 = input(("\n\t\t\t \t\tIngresa el nombre del segundo jugador: "))
    print(Fore.BLUE + "\n-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")
    print(Style.RESET_ALL)
    tprint("Juguemos!",font="random")
    # De las coordenadas que el usuario elija, será equivalente a una x posicion en valueMatrix
    selectionDictionary = {
        "00": "0",    "01": "1",  "02": "2",  "03": "3",
        "10": "4",    "11": "5",  "12": "6",  "13": "7",
        "20": "8",    "21": "9",  "22": "10", "23": "11",
        "30": "12",   "31": "13", "32": "14", "33": "15"
    }

    # -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- End Initial considerations -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.


    playGame = 1 # Inicialización del juego
    while playGame:
        # ------------------------- Initial instances in game --------------------------------

        m = startArray(4,4) # Inicializamos la matriz (m = Matrix)
        valueMatrix = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8] # Números pares que se usarán
        r.shuffle(valueMatrix) # Los revolvemos y guardamos contemplandolo como otro array
        gC = True # Continuidad del juego (gC = Game Continuity)
        nSP1 = []; nSP2 = [] # Números seleccionados por cada jugador (nSP1 = Number Selected Player 1)
        cSP1 = []; cSP2 = [] # Coordenadas seleccionadas por cada jugador (cSP1 = Coordinate Selected Player 1)
        pInG = [P1,P2]; pInGP = 0 # Jugador en juego y su posicion (pInGP = Player in Game Position)
        pT = [1,1] # Turno (pT = Player turn)

        #  -.-.-.-.-.-.-.-.-.-.-.-.-. Initial instances in game  -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
        while gC:
            print("\n------------------------------------")
            showA(m)
            print("\n------------------------------------")

            # Comprobamos si ya ingresó 2 numeros o no
            if len(nSP1) == 2 or len(nSP2) == 2:
                coordinate = input("\nIncorrecto\nIngresa 11 para cambiar al turno {} del otro jugador: \n".format(pT[pInGP]))
                print(nSP1,nSP2)
            else: 
                coordinate = input("\nIngresa un valor, {}: ".format(pInG[pInGP]))
            # Cambio a coordenadas reales de lectura (Ej. 11 cambia a 00)
            coordinate = str(int(coordinate[1])-1)+str(int(coordinate[0])-1) 

            # Considerar que sea una coordenada correcta, dentro de 00 y 44
            if coordinate in selectionDictionary: 

                # Obtenemos el valor equivalente en ValueMatrix y lo mostramos en la matriz
                m[int(coordinate[0])][int(coordinate[1])] = valueMatrix[int(selectionDictionary[coordinate])] 

                # Denotamos cual jugador esta actualmente en turno
                if pInGP == 0:
                    
                    # Guardamos el valor y coordenada seleccionados
                    nSP1.append(valueMatrix[int(selectionDictionary[coordinate])]) 
                    cSP1.append(coordinate) 
                    if len(nSP1) == 3: 
                        
                        # Comprobamos que no use la misma casilla
                        if cSP1[0] == cSP1[1]: 
                            print("Esta casilla es la misma que seleccionaste antes!!")
                            m = startArray(4,4)
                            pInGP = 1
                            
                        else:
                            m = startArray(4,4)
                            # Valorar si son valores iguales y si es asi, un jugador gana
                            if nSP1[0] == nSP1[1]: 
                                gC = False # Terminar juego
                            else: # En el caso que no gana, se reinician los valores y cambia el turno
                                nSP1.clear();cSP1.clear()
                                print("-.-.-.-.-.-.-.- Siguiente turno!! -.-.-.-.-.-.-.-")
                                m = startArray(4,4) # Reinicio la matriz mostrado
                                pInGP = 1
                                pT[0] += 1
                    elif len(nSP1) == 2:
                        if nSP1[0] == nSP1[1]: # Valorar si son números iguales
                            gC = False # Terminar juego
                elif pInGP == 1:

                    # Guardamos el valor seleccionado
                    nSP2.append(valueMatrix[int(selectionDictionary[coordinate])]) 
                    cSP2.append(coordinate)
                    if len(nSP2) == 3:

                        # Comprobamos que no use la misma casilla
                        if cSP2[0] == cSP2[1]: 
                            print("Esta casilla es la misma que seleccionaste antes!!")
                            m = startArray(4,4)
                            pInGP = 0
                        else:
                            m = startArray(4,4)

                            # Valorar si son números iguales y si es verdadero, hubo un ganador
                            if nSP2[0] == nSP2[1]:  
                                gC = False # Terminar juego
                            else: # En el caso que no gana, se reinician los valores y cambia el turno
                                nSP2.clear();cSP2.clear()
                                print("-.-.-.-.-.-.-.- Siguiente turno!! -.-.-.-.-.-.-.-")
                                m = startArray(4,4) # Reinicio la matriz mostrado
                                pInGP = 0
                                pT[1] += 1
                    elif len(nSP2) == 2:
                        if nSP2[0] == nSP2[1]: # Valorar si son números iguales y si es verdadero, hubo un ganador
                                gC = False # Terminar juego
            else:
                print("\t\t\tEsta no es una coordenada adecuada!!\n")
                print("\t\t\tPierdes tu turno\n")
                if pInGP == 0:
                    pT[pInGP] += 1
                    pInGP = 1
                else:
                    pT[pInGP] += 1
                    pInGP = 0
                m = startArray(4,4)
        gameWon(pInG,pT,pInGP)
        print("\t\t\t¿Quieres jugar de nuevo?\n")
        playGame = int(input("Ingresa 1 y enter para jugar de nuevo!\t\tIngresa 0 y enter para cerrar el juego :(\n"))

    # Falta escribir correctamente la informacion en data.txt de cada partida y tambien verificar si es un usuario que ya ha entrado
    # con anterioridad

    # data = open("data.txt","w")
    # data.write(pInG[0])
    # data.write(",")
    # data.write(pT[0])
    # data.write("\n")
    # data.write(pInG[1])
    # data.write(",")
    # data.write(pT[1])

# ----------------------------------------------- Instructions --------------------------------------------------------
def instructions():
    iL = 1
    while iL:
        print(Fore.BLUE + "-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- Instrucciones -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")
        print(Style.RESET_ALL)
        f = open("instrucciones.txt", "r")
        for i in f:
            print (i,end=" ")
            sys.stdout.flush()
            time.sleep(0.3) 
        iL = int(input(("\t\t\t \t\tPresiona 0 para cerrar: ")))
        if iL == 0:
            print(Fore.BLUE + "\n-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")
            print(Style.RESET_ALL)
            f.close()
            mO = 0
            return mO
        else:
            f.close()
            print(Fore.RED + "\t\t\t \t\tTe equivocaste de numero!\n")

# ----------------------------------------------- Stats --------------------------------------------------------
def stats():
    sL = 1
    while sL == True:
        print(Fore.BLUE + "-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- Estadisticas -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")
        print(Style.RESET_ALL)
        f = open("data.txt", "r")
        print("\t\t\t \t\tEstadisticas...\n")
        print("\tNombre\tPartidas ganadas")
        for i in f:
            print (i,end=" ")
            sys.stdout.flush()
            time.sleep(0.7)
        
        sL = int(input(("\t\t\t \t\tPresiona 0 para cerrar: ")))
        if sL == 0:
            print(Fore.BLUE + "\n-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")
            print(Style.RESET_ALL)
            mO = 0
            f.close()
            return mO
        else:
            print(Fore.RED + "\t\t\t \t\tTe equivocaste de numero!\n")
            f.close()

# ................................................ Main ...................................................
print(Fore.RED,"\t\t\t \t******Se recomienda hacer mas grande la consola******")
data = range(100)
print("\t\t\t \t\t\tCargando...")
print(Fore.GREEN)
for _ in tqdm.tqdm(data):
    time.sleep(0.05)

print(Style.RESET_ALL)
mainMenu()
