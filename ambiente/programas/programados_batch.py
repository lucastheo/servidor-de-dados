import re
class ProgramadosBatch:
    RE_IDENTIFICADO = re.compile(r"#Programado_batch [0-9]+ ")
    @staticmethod
    def pertence(  string ):
        return len( re.findall(ProgramadosBatch.RE_IDENTIFICADO , string ) ) > 0
    @staticmethod
    def codigo_execucao( string ):
        var = {'tipo':'ConsumidoresFila',
               'pre-codigo':re.sub(ProgramadosBatch.RE_IDENTIFICADO, '', string ),
               'codigo':None
        }
        return var
        