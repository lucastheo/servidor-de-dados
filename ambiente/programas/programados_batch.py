import re
class ProgramadosBatch:
    RE_IDENTIFICADO = re.compile(r"#programado_batch [0-9]+ ")
    @staticmethod
    def pertence(  string ):
        return len( re.findall(ProgramadosBatch.RE_IDENTIFICADO , string ) ) > 0
    @staticmethod
    def codigo_execucao( string ):
        var = {'tipo':'ProgramadosBatch',
               'pre-codigo': string,
               'codigo':re.sub(ProgramadosBatch.RE_IDENTIFICADO, '', string),
               'tempo':ProgramadosBatch.captura_tempo(string)
        }
        return var
    @staticmethod
    def captura_tempo( string ):
        var = re.findall("[0-9]+" , string)
        if len( var ) == 0:
            return 0
        return int( var[0] )

        