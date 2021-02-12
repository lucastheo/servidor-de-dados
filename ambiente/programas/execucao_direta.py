import re

class ExecucaoDireta:
    RE_IDENTIFICADO = re.compile(r"#consumidor_fila [0-9]+ ")
    @staticmethod
    def pertence(  string ):
        return len( re.findall(ExecucaoDireta.RE_IDENTIFICADO , string ) ) > 0
    @staticmethod
    def codigo_execucao( string ):
        var = {'tipo'      :'ConsumidoresFila',
               'pre-codigo' :string,
               'codigo'     :re.sub(ExecucaoDireta.RE_IDENTIFICADO, '', string ),
               'quantidade' :ExecucaoDireta.gera_quantidade(string)}

        return var
    @staticmethod
    def gera_quantidade(string):
        busca = re.findall("[0-9]+", string )
        if len( busca ) == 0:
            return 0
        return int( busca[0] )