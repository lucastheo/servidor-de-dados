"""
Não devem ser usadas em todo código, somente em init ou definicoes
"""

import os

class ServidorMensagemVariaveis:
    class path:
        base = os.getcwd() + "/ambiente/servidor-mensagem/"
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

        