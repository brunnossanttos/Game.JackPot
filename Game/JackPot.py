import random
from Game.lib.interface import *
cartas = ['Ás', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valente', 'Dama',
          'Rei']
naipes = ['Copas', 'Paus', 'Ouro', 'Espada']
jogadores = []
mao = []
while True:
    cabecalho('JOGO 21')
    njogadores = int(input('Quantos jogadores( 1, 2, 3 ou 4)? '))
    print(linha(65))
    if njogadores <= 4:
        break
    else:
        print('\033[31mNumero de jogadores inválido\033[m')
        print(linha(65))
for nj in range(1, njogadores + 1):
    jogadores.append(str(input(f'Qual o nome do jogador {nj}? ')))
    print(linha(65))
    nj += 1
for cards in range(0, njogadores):
    jogadores[cards] = print(f'Jogador {jogadores[cards]} tirou {random.sample(cartas, 1)} '
                             f'de {random.sample(naipes, 1)}', end='')
    jogadores[cards] = print(f' e {random.sample(cartas, 1)} de {random.sample(naipes, 1)}')
    print(linha(65))
    while True:
        while True:
            escolha = str(input('Deseja mais uma carta?(S/N) ')).strip().upper()
            print(linha(65))
            if escolha in 'SN':
                break
            else:
                    print('\033[31mResposta inválida. Use somente S ou N.\033[m')
        if escolha == 'S':
            jogadores[cards] = print(f'Vc pegou mais uma carta {random.sample(cartas, 1)} de {random.sample(naipes, 1)}')
            print(linha(65))
        if escolha == 'N':
            break
    cards += 1
