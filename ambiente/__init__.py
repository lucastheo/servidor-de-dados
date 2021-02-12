import os
import sys
sys.path.append(os.getcwd())

from ambiente.arquivos import execute as arquivos_execute
from ambiente.servidor_mensagem import execute as servidor_mensagem_execute
from ambiente.programas import execute as programas_execute
from ambiente.processos import Processos
from multiprocessing import Array
from time import sleep

def execute(): 
    arquivos_execute()
    Processos.iniciar_ambiente( Processos.execute_batch , Processos.queue_batch  )
    Processos.iniciar_ambiente( servidor_mensagem_execute )
    Processos.iniciar_ambiente(programas_execute())
    Processos.kill()