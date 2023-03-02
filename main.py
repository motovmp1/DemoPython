import random

display_message = [
    'Seja feliz :)',
    'Fque tranquilo, tudo vai acabar bem!',
    'Ola, nova mensagem'

]

while True:
    resposta = input('Deseja receber um concelho?  S/N : ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_message)
        print(mensagem)
        print()

