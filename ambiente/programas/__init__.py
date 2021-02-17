#programas precisam de um helf check

import os
import sys
import re
sys.path.append(os.getcwd())

from ambiente.variaveis import ArquivosVariaveis
from ambiente.programas.execucao_direta import ExecucaoDireta
from ambiente.programas.programados_fixo import ProgramadosFixo
from ambiente.programas.programados_batch import ProgramadosBatch
from ambiente.processos import Processos
from ambiente.variaveis import IgnorarEsseArquivo

def execute():
    ignorar_esse_arquivo = IgnorarEsseArquivo()
    path_codigos = ArquivosVariaveis.path.codigos

    lista_forma_executar = list()
    for dir_path ,_, file_names  in os.walk(path_codigos):
        if len( file_names ) > 0:
            for file_name in file_names:
                if not ignorar_esse_arquivo.execute( file_name ):
                    lista_forma_executar.extend( comando( dir_path + '/' + file_name ) )
    
    for forma in lista_forma_executar:
        if forma['tipo'] == 'ExecucaoDireta':
            for _ in range(forma['quantidade']):
                execute_direto(forma)
        elif forma['tipo'] == 'ProgramadosBatch':
            executa_batch(forma)
    


def execute_direto( forma ):
    Processos.iniciar_direto( forma['codigo'] )

def executa_batch( forma ):
    Processos.iniciar_batch( forma['codigo']  , forma['tempo'] )

def comando(file_path:str)->list:
    comandos = list()
    with open(file_path, 'r') as arq:
        for line in arq.readlines():
            if ExecucaoDireta.pertence(line):
                comandos.append( ExecucaoDireta.codigo_execucao( line ) )
            elif ProgramadosFixo.pertence( line ):
                comandos.append( line )
            elif ProgramadosBatch.pertence( line ):
                comandos.append( ProgramadosBatch.codigo_execucao( line ) )
    
    for i , comando in enumerate( comandos ):
        if '{esse-arquivo}' in comando['codigo']:
            comandos[i]['codigo']=comando['codigo'].replace('{esse-arquivo}', f'"{file_path}"') if comando['codigo'] != None else None
            comandos[i]['pre-codigo']=comando['pre-codigo'].replace('{esse-arquivo}', f'"{file_path}"')
    return comandos

    