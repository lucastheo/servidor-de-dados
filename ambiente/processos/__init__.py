import subprocess
from datetime import datetime, timedelta
from multiprocessing import Process, Queue
from time import sleep

class Processos:
    lista_ambiente = list()
    lista_processos = list()
    lista_batch = list() # não tem os processo, somente o rastro
    queue_batch = Queue()

    @staticmethod
    def iniciar_direto(comando:str):
        p = Process( target= lambda:subprocess.call( comando , shell=True ) )
        p.start()
        Processos.lista_processos.append( {"processo":p, "comando":comando } )
        
    @staticmethod
    def iniciar_batch( comando , tempo ):
        var = {"processo": None , "comanado":comando , "proxima_execucao":datetime.now() , "tempo":tempo}
        Processos.lista_batch.append(var)
        Processos.queue_batch.put(var)
    
    @staticmethod
    def iniciar_ambiente( comando , arg=None ):
        if arg == None:
            p = Process( target= comando )
        else:
            p = Process( target=comando , args=(arg,))
        p.start()
        Processos.lista_ambiente.append( {"processo": p , "comanado":comando })
    
    @staticmethod
    def execute_batch(queue:Queue):
        def join_processos( lista ):
            for var in lista_batch_:
                if var['processo'] != None:
                    var['processo'].kill()

        def recebe_elemento( queue , lista_batch_):
            if queue.qsize() > 0:
                conteudo = queue.get()
                if type(conteudo) == dict:
                    lista_batch_.append( conteudo )
                elif type(conteudo == str):
                    if conteudo=='kill-all':
                        join_processos( lista_batch_)

        def novo_processo( execucao ):
            if execucao['processo'] != None:
                try:
                    execucao['processo'].kill()    
                except Exception as e:
                    print("Erro ao matar o processo")    
            
            execucao['processo'] = Process( target=lambda:subprocess.call( execucao['comanado'] , shell=True ) )
            execucao['processo'].start()
            execucao["proxima_execucao"]= datetime.now() + timedelta(minutes=int(execucao["tempo"]))
        
        lista_batch_ = list()
        while 1:
            recebe_elemento(queue,lista_batch_)      
            for execucao in lista_batch_:
                if execucao['proxima_execucao'] < datetime.now():
                    novo_processo( execucao )
                sleep(0.09/len(lista_batch_))
            sleep(0.1)

    @staticmethod
    def kill():
        lista_ambiente_ = list( Processos.lista_ambiente )
        lista_processos_ = list( Processos.lista_processos )

        Processos.queue_batch.put("kill-all")
        for processo_processos in lista_processos_:
            processo_processos['processo'].kill()
        for processo_ambiente in lista_ambiente_:
            processo_ambiente['processo'].kill()
        
        
    