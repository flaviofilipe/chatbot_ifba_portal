from robo import validar_comando

if __name__ == '__main__':
    comando = ''
    while(comando != 'sair'):
        comando = input("Como posso ajudar?: ")
        validar_comando(comando)
    print('Até a próxima!')
