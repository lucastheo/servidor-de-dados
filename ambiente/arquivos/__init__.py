import os
import sys
sys.path.append(os.getcwd())

from ambiente.arquivos.dados_arquivos import ArquivoServidor

def execute():
    arquivos = ArquivoServidor()
    arquivos.prepara()
