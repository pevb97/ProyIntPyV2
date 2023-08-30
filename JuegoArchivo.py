import os
import random
from Juego import Juego

class JuegoArchivo(Juego):
    def __init__(self, mapa :str = f'maps/{random.choice(os.listdir("maps"))}'):
        self.__arch_map = mapa
        Juego.__init__(self, self.__covert_map())
        

    def __covert_map(self)-> map:
        with open(self.__arch_map, "r") as arc:
            return list(map(list, arc.read().split("\n")))
    
while True:
    juego = JuegoArchivo()
    juego.main()
