def validar_resposta(resposta):
    if(resposta == 'noticias'):
        return 'Listar notícias'
    
    if(resposta == 'comunicados'):
        return 'Listar notícias'

    if(resposta == 'editais'):
        return 'Listar editais'

    if(resposta == 'pesquisar'):
        return 'pesquisando'
    
    if(resposta == 'contato'):
        return 'Lista de contato'


def validar_comando(comando):
    ...