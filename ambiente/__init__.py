import os
import sys
sys.path.append(os.getcwd())

from ambiente.arquivos import execute as arquivos_execute
from ambiente.servidor_mensagem import execute as servidor_mensagem_execute
from ambiente.programas import execute as programas_execute


def execute():
    arquivos_execute()
    servidor_mensagem_execute()
    programas_execute()