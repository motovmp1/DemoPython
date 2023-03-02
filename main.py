import random
from .message_gen import display_message

while True:
    resposta = input('Deseja receber um concelho?  S/N : ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_message)
        print(mensagem)
        print()

