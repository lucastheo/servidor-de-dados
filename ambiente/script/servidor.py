import os
import sys
import requests
import subprocess
from multiprocessing import Process
sys.path.append(os.getcwd())

from ambiente.variaveis import ServidorMensagemVariaveis

class ServidorAmbiente:
    def __init__(self):
        self.path = ServidorMensagemVariaveis.path.base
        self.path_server = self.path + "demo-0.0.1-SNAPSHOT.jar"
        self.path_config = self.path + "configuracoes_servidor.json"
        self.url_sqm_jar = ServidorMensagemVariaveis.url.sqm_jar
        self.url_sqm_config = ServidorMensagemVariaveis.url.sqm_config
    
    def prepara( self ):
        if not os.path.exists( self.path ):
            os.mkdir(self.path )
        
        if not os.path.exists( self.path_server ):
            r = requests.get(self.url_sqm_jar, allow_redirects=True)
            open(self.path_server, 'wb').write(r.content)
        
        if not os.path.exists( self.path_config ):
            r = requests.get(self.url_sqm_config, allow_redirects=True)
            open(self.path_config, 'wb').write(r.content)
    
    def execute(self):
        p = Process( target= lambda:subprocess.call( f"cd {self.path}; java -jar {self.path_server}" , shell=True ) )
        p.start()
        