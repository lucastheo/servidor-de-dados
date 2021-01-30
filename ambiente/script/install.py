import os
import sys
sys.path.append(os.getcwd())

from ambiente.script.servidor import ServidorAmbiente
from ambiente.script.dados_arquivos import ArquivoServidor

def execute():
    servidor = ServidorAmbiente()
    arquivos = ArquivoServidor()

    servidor.prepara()
    arquivos.prepara()
    servidor.execute()