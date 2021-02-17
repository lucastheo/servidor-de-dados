import uuid
import json
from tornado import gen

def validacoes( entrada ):
    if 'arquivo' not in entrada.keys():
        return json.dumps( {'erro':"Não contem arquivo"} )
    if 'caminho' not in entrada.keys() or type( entrada['caminho']) != str:
        return json.dumps( {'erro':"Não contem caminho ou invalido"} )
    return None

def gera_uuid():
    return str( uuid.uuid4() )

@gen.coroutine     
def envia_novo_arquivo( smq_cliente , entrada:dict ):
    entrada = json.loads(entrada)
    var = validacoes(entrada)
    if var != None:
        return var
    entrada['uuid'] = gera_uuid()
    smq_cliente.envia("nova_mensagem", mensagem=json.dumps(entrada))
    return json.dumps( {'id':entrada['uuid']} )
    