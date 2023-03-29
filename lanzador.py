from barbero import *
from cliente import *
import time

def lanzar():
    barbero=Barbero()
    cliente1=Cliente('Javi',barbero)
    cliente2=Cliente('Antonio',barbero)
    cliente3=Cliente('Andres',barbero)
    clientes=[cliente1,cliente2,cliente3]

    barbero.start()
    for cliente in clientes:
        cliente.start()
        time.sleep(2)