import os
import sys
sys.path.append(os.getcwd())

from ambiente.servidor_mensagem.servidor import ServidorAmbiente

def execute():
    servidor = ServidorAmbiente()
    servidor.prepara()
    servidor.execute()