from barbero import Barbero
from cliente import Cliente
import time

def lanzar():
    lista=[]
    barbero=Barbero(lista)
    cliente4=Cliente('Jose',barbero)
    lista.append(cliente4)
    cliente1=Cliente('Javi',barbero)
    cliente2=Cliente('Antonio',barbero)
    cliente3=Cliente('Andres',barbero)
    clientes=[cliente1,cliente2,cliente3]

    barbero.start()
    time.sleep(2)
    for cliente in clientes:
        cliente.start()
        time.sleep(2)