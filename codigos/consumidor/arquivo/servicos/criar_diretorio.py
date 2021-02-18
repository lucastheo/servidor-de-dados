import re,os

def de_uuid_para_diretorio( uuid ):
    s = ''
    for e in re.findall('[0-9a-f]{2}' , uuid ):
        s += f'{e}/'
    return s

def criar_diretorios( path_arquivos ,  entrada:dict ):
    uuid = entrada['uuid']
    path_uuid = f'{path_arquivos}{de_uuid_para_diretorio(uuid)}'
    os.makedirs(path_uuid,exist_ok=True)
    return path_uuid
