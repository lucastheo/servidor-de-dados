import re
class ProgramadosFixo:
    RE_IDENTIFICADO = re.compile(r"#Programado_fixo [0-9]{1,2}-[0-9]{2} ")
    @staticmethod
    def pertence(  string ):
        return len( re.findall(ProgramadosFixo.RE_IDENTIFICADO , string ) ) > 0
    @staticmethod
    def codigo_execucao( string ):
        var = {'tipo':'ConsumidoresFila',
               'pre-codigo':re.sub(ProgramadosFixo.RE_IDENTIFICADO, '', string ),
               'codigo':RuntimeError("Erro ao gerar o código")
        }
        return var
        