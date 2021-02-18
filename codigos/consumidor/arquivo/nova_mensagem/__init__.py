#execucao_direta 2 python3 {esse-arquivo}

import sys, os, json
sys.path.append( os.getcwd())
from bibliotecas.python.smq.cliente import SmqCliente
from ambiente.variaveis import ArquivosVariaveis
from codigos.consumidor.arquivo.servicos.criar_diretorio import criar_diretorios
from codigos.consumidor.arquivo.servicos.comprimir import comprime_arquivo
from codigos.consumidor.arquivo.nova_mensagem.validacoes import validacoes

FILE_CONSUMO_ARQUIVO = 'nova_mensagem'
FILA_ENVIA_ERRO = 'processou_com_erro'
FILA_ENVIA_SUCESSO = 'processou_com_sucesso'

LISTA_FILA_ENVIA_SUCESSO = ['tag', 'caminho', 'compressão', 'geral' , 'ultimo_acesso' ]


def consome( path_arquivos , recebe ):  
    if validacoes(recebe) != None:
        raise Exception(f"Erro de validação {validacoes(recebe)}")
    else:
        path = criar_diretorios( path_arquivos , recebe )
        comprime_arquivo( path , recebe['arquivo'])
    
def envia_erro( smq_client , mensagem = '' , detalhes='' , bruto =''):
    var = {'mensagem':mensagem, 'detalhes':detalhes, 'bruto':bruto }
    smq_client.envia(FILA_ENVIA_ERRO , mensagem=json.dumps(var))
    
def envia_sucesso( smq_client , recebe ):
    smq_client.envia(FILA_ENVIA_SUCESSO , LISTA_FILA_ENVIA_SUCESSO ,  mensagem=json.dumps(recebe))


if __name__=='__main__':
    path_arquivos = ArquivosVariaveis.path.arquivos
    smq_client = SmqCliente() 
    while True:
        try:
            recebe = smq_client.recebe_bloqueante( FILE_CONSUMO_ARQUIVO )
            entrada = recebe.mensagem()

            try:
                dto = json.loads( entrada )
                consome( path_arquivos , dto )
                envia_sucesso( smq_client , dto )
            except Exception as e:
                envia_erro( smq_client , 'nova-mensagem_consumo: erro em compimir mensagem', entrada , str(e))
            finally:
                recebe.commit()
        except:
            print("Erro durante processamento, como vamos lidar com isso")
        

        