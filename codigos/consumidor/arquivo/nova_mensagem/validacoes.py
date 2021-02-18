import json
def validacoes( entrada ):
    if 'arquivo' not in entrada.keys():
        return json.dumps( {'erro':"Não contem arquivo"} )
    if 'caminho' not in entrada.keys() or type( entrada['caminho']) != str:
        return json.dumps( {'erro':"Não contem caminho ou invalido"} )
    return None
