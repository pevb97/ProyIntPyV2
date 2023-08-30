import os
from readchar import key, readkey

class Juego:
    
    def __init__(self, mapa):
        self.mapa = mapa
        
        
    def __get_bordes_mapa(self):
        #Obtencion de las posiciones de los bordes del laberinto
        len_x_mapa = len(self.mapa[0])
        len_y_mapa = len(self.mapa)

        coord_borde_izq_map = list(map(lambda x: [0, x], range(len_y_mapa)))
        coord_borde_der_map = list(map(lambda x: [len_y_mapa-1, x], range(len_y_mapa)))
        coord_borde_sup_map = list(map(lambda x: [x, 0], range(len_x_mapa)))
        coord_borde_inf_map = list(map(lambda x: [x, len_x_mapa-1], range(len_x_mapa)))

        return coord_borde_izq_map + coord_borde_der_map + coord_borde_sup_map + coord_borde_inf_map
    

    def get_in_out_mapa(self)->list:
        #Obtencion de las posiciones en las que existe una entrada o salida del laberinto
        pos_in_out = list()
        for i in self.__get_bordes_mapa():
            if self.mapa[i[0]][i[1]] == ".":
                pos_in_out.append(i)
        return pos_in_out


    def update_sreen(self):
        os.system('cls' if os.name=='nt' else 'clear')
        for i in self.mapa:
            print("".join(i))


    def main(self):
        pos_inicial, pos_final = self.get_in_out_mapa()
        py, px = pos_inicial

        while([py,px] != pos_final):
            lim_x, lim_y = range(len(self.mapa[0])), range(len(self.mapa))
            self.mapa[py][px] = "P"
            self.update_sreen()
            while True:
                k = readkey()
                if(k == key.UP and (py-1 in lim_y) and (self.mapa[py-1][px]) == "."):
                    self.mapa[py][px] = "."
                    py -= 1
                    self.mapa[py][px] = "P"
                    break
                elif(k == key.DOWN and (py+1 in lim_y) and (self.mapa[py+1][px]) == "."):
                    self.mapa[py][px] = "."
                    py += 1
                    self.mapa[py][px] = "P"
                    break
                elif(k == key.RIGHT and (px+1 in lim_x) and (self.mapa[py][px+1]) == "."):
                    self.mapa[py][px] = "."
                    px += 1
                    self.mapa[py][px] = "P"
                    break
                elif(k == key.LEFT and (px-1 in lim_x) and (self.mapa[py][px-1]) == "."):
                    self.mapa[py][px] = "."
                    px -= 1
                    self.mapa[py][px] = "P"
                    break
