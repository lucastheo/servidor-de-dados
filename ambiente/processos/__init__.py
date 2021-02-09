import subprocess
from multiprocessing import Process

class Processos:
    lista_processos = list()

    @staticmethod
    def iniciar(comando:str):
        p = Process( target= lambda:subprocess.call( comando , shell=True ) )
        p.start()
        Processos.lista_processos.append( {"processo":p, "comando":comando} )
        