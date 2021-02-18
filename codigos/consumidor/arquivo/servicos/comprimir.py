import lzma

def comprime_arquivo( path , conteudo ):
    return comprime( f'{path}arquivo' , conteudo )

def comprime( path , conteudo ):

    with lzma.open(path, 'w') as file:
        if type( conteudo ) == str:
            file.write( conteudo.encode() )
        else:
            file.write( bytes(conteudo) )
    