import threading
import time

class Cliente(threading.Thread):
    def __init__(self,nombre,barbero):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.barbero = barbero
    def levantar_barbero(self):
        if self.barbero.dormido==True:
            print(f'{self.nombre} ha levantado al barbero')
            self.barbero.dormido=False
        else:
            pass
    def llegar(self):
        print(f'{self.nombre} acaba de llegar')
        self.barbero.cola.append(self)
    def cortarse_el_pelo(self):
        self.llegar()
        self.levantar_barbero()
        if self.barbero.silla.locked()==False:
            print(f'{self.nombre} esta listo para empezar')
    def run(self):
        self.cortarse_el_pelo()