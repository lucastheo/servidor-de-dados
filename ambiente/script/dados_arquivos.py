import os
import sys
import requests
sys.path.append(os.getcwd())

from ambiente.variaveis import ArquivosVariaveis

class ArquivoServidor:
    def __init__( self ):
        self.arquivos                 = ArquivosVariaveis.path.arquivos                
        self.compressap               = ArquivosVariaveis.path.compressap              
        self.caminho                  = ArquivosVariaveis.path.caminho                 
        self.busca_tag                = ArquivosVariaveis.path.busca_tag               
        self.buisca_tag_file          = ArquivosVariaveis.path.buisca_tag_file         
        self.tmp_descomprimidos       = ArquivosVariaveis.path.tmp_descomprimidos      
        self.tmp_descomprimidos_file  = ArquivosVariaveis.path.tmp_descomprimidos_file
        self.erros_arquivos           = ArquivosVariaveis.path.erros_arquivos          
        self.erros_arquivos_file      = ArquivosVariaveis.path.erros_arquivos_file    
        self.logs_geral               = ArquivosVariaveis.path.logs_geral              
        self.logs_geral_file          = ArquivosVariaveis.path.logs_geral_file  

    def prepara( self ):
        if not os.path.exists( self.arquivos                 ):
            os.makedirs(self.arquivos                )
        if not os.path.exists( self.compressap               ):
            os.makedirs(self.compressap              )
        if not os.path.exists( self.caminho                  ):
            os.makedirs(self.caminho                 )
        if not os.path.exists( self.busca_tag                ):
            os.makedirs(self.busca_tag               )
        if not os.path.exists( self.buisca_tag_file          ):
            open(self.buisca_tag_file, "w").write("")
        if not os.path.exists( self.tmp_descomprimidos       ):
            os.makedirs(self.tmp_descomprimidos      )
        if not os.path.exists( self.tmp_descomprimidos_file  ):
            open(self.tmp_descomprimidos_file, "w").write("{}")
        if not os.path.exists( self.erros_arquivos           ):
            os.makedirs(self.erros_arquivos          )
        if not os.path.exists( self.erros_arquivos_file      ):
            open(self.erros_arquivos_file , "w").write("{}")
        if not os.path.exists( self.logs_geral               ):
            os.makedirs(self.logs_geral              )
        if not os.path.exists( self.logs_geral_file          ):
            open(self.erros_arquivos_file , "w").write("")