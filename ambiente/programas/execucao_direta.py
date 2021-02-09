import re

class ExecucaoDireta:
    RE_IDENTIFICADO = re.compile(r"#consumidor_fila [0-9]+ ")
    @staticmethod
    def pertence(  string ):
        return len( re.findall(ExecucaoDireta.RE_IDENTIFICADO , string ) ) > 0
    @staticmethod
    def codigo_execucao( string ):
        var = {'tipo'      :'ConsumidoresFila',
               'pre-codigo':re.sub(ExecucaoDireta.RE_IDENTIFICADO, '', string ),
               'codigo'    :re.sub(ExecucaoDireta.RE_IDENTIFICADO, '', string ) }
        return var
