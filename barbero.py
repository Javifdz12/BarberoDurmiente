import threading
import time

class Barbero(threading.Thread):
    silla=threading.Lock()
    def __init__(self):
        threading.Thread.__init__(self)
        self.cola=[]
        self.dormido=True

    def atender(self):
        if self.cola!=[] and self.dormido!=True:
            for cliente in self.cola:
                print(f'Adelante {cliente.nombre}')
                Barbero.silla.acquire()
                print(f'Silla ocupada por {cliente.nombre}')
                time.sleep(5)
                Barbero.silla.release()
                print(f'{cliente.nombre} ya se ha cortado el pelo')
                print('Silla desocupada')
                self.cola.remove(cliente)
        else:
            self.dormido=True
            print('Toca siesta')

    def run(self):
        while True:
            self.atender()













