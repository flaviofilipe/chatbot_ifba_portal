from chatterbot import ChatBot
from difflib import SequenceMatcher
import integration.portal_bot as portal

ACEITACAO = 0.70


def comparar_mensagens(mensagem, mensagem_candidata):
    confianca = 0.0

    if mensagem.text and mensagem_candidata.text:
        texto_mensagem = mensagem.text
        texto_mensagem_candidata = mensagem_candidata.text

        confianca = SequenceMatcher(
            None,
            texto_mensagem,
            texto_mensagem_candidata
        )
        confianca = round(confianca.ratio(), 2)
        if confianca < ACEITACAO:
            confianca = 0.0
        else:
            print("mensagem do usuario:", texto_mensagem, ", mensagem candidata:", mensagem_candidata,
                  ", nível de confiança:", confianca)

    return confianca


def selecionar_resposta(mensagem, lista_respostas, storage=None):
    resposta = lista_respostas[0]
    print("resposta escolhida:", resposta)
    return resposta


def portal_integration(message):
    if message == 'noticia_categorias':
        return 'Listar noticias por categoria'

    if message == 'noticias':
        return portal.get_last_posts()

    if message == 'search':
        return 'Pesquisar noticia'

    if message == 'contato':
        return 'Listar contato'

    if message == 'comunicados':
        return 'Listar comunicados'

    if message == 'editais':
        return 'Listar Editais'

    if message == 'online':
        return 'Verificar se está online'

    return 'Não encontrado!'


def robo() -> ChatBot:
    logic_adapters = [
        {"import_path": "chatterbot.logic.BestMatch"}
    ]
    return ChatBot("Robô do Portal",
                   read_only=True,
                   statement_comparison_function=comparar_mensagens,
                   response_selection_method=selecionar_resposta,
                   logic_adapters=logic_adapters)


def run():
    while True:
        comando = input(">> ")
        if comando in ['sair', 'exit']:
            print('Até a próxima!')
            return
        resposta = robo().get_response(comando)
        if resposta.confidence > 0.0:
            print(portal_integration(resposta.text))
        else:
            print("ainda nao sei como responder essa pergunta")
            print("pergunte outra coisa...")
