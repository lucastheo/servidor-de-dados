"""
Não devem ser usadas em todo código, somente em init ou definicoes
"""

import os,re

class ServidorMensagemVariaveis:
    class path:
        base = os.getcwd() + "/ambiente/servidor_mensagem/arquivos/"
    class url:
        sqm_jar = "https://smq-jar.s3-sa-east-1.amazonaws.com/0.0.0/demo-0.0.1-SNAPSHOT.jar"
        sqm_config = "https://smq-jar.s3-sa-east-1.amazonaws.com/0.0.0/configuracoes_servidor.json"

class ArquivosVariaveis:
    class path:
        arquivos                    = os.getcwd() + "/dados/arquivos/"
        compressap                  = os.getcwd() + "/dados/compressao/"
        caminho                     = os.getcwd() + "/dados/caminho/"
        busca_tag                   = os.getcwd() + "/dados/busca/tag/"
        buisca_tag_file             = os.getcwd() + "/dados/busca/tag/tag"
        tmp_descomprimidos          = os.getcwd() + "/dados/tmp/descomprimidos/"
        tmp_descomprimidos_file     = os.getcwd() + "/dados/tmp/descomprimidos/arquivos-tempo"
        erros_arquivos              = os.getcwd() + "/dados/erros/arquivos/"
        erros_arquivos_file         = os.getcwd() + "/dados/erros/arquivos/arquivos-tempo"
        logs_geral                  = os.getcwd() + "/dados/logs/"
        logs_geral_file             = os.getcwd() + "/dados/logs/geral"
        codigos                     = os.getcwd() + "/codigos/"

class IgnorarEsseArquivo:
    def __init__( self ):
        self._le_arquivo = list( self.__le_arquivo() )
    def __le_arquivo(self):
        for line in open( "./ambiente/ignorar_arquivo_na_execucao", "r"):
             yield re.compile( line )
    def execute( self , string ):
        for r in self._le_arquivo:
            if len( re.findall(r , string ) ) > 0:
                return True
        return False


    