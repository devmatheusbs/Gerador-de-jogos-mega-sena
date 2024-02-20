from utils import gerar_numeros
from utils import limpar_terminal
from time import sleep
power = True
qtd_numeros = None
qtd_jogos = None
while power is True:
    print('#'*48)
    print('Gerador de Jogos da Mega-Sena')
    print('#'*48)
    sleep(1)
    print('Quantos números seu jogo terá?')
    while type(qtd_numeros) is not int: 
        try:
            qtd_numeros = int(input('Digite um número de 6 à 20: '))
            if qtd_numeros < 6 or qtd_numeros > 20:
                qtd_numeros = None
                print('Quantidade de números inválidos, informe um número de 6 à 20.')
        except ValueError:
            print('Caractere inválido, informe um número de 6 à 20.')
    print('Quantos jogos você fará na sua cartela?')
    while type(qtd_jogos) is not int: 
        try:
            qtd_jogos = int(input('Digite um número de 1 à 3: '))
            if qtd_jogos < 1 or qtd_jogos > 3:
                qtd_jogos = None
                print('Quantidade de jogos inválidos, informe um número de 1 à 3.')
        except ValueError:
            print('Caractere inválido, informe um número de 1 à 3.')
    for _ in range(qtd_jogos):
        aposta = gerar_numeros(qtd_numeros)
        aposta.sort()
        print(f'Gerando aposta {_+1}')
        sleep(1)
        print(f'Jogo {_+1}: {aposta}')
    sleep(1)
    print('#'*48)
    continuar = ('s', 'n')
    trigger = None
    while trigger not in continuar:
        try:
            trigger = str.lower(input('Deseja realizar um novo jogo? [s] ou [n]: '))
            if trigger == 'n':
                power = False
            elif trigger == 's':
                qtd_jogos = None
                qtd_numeros = None
                limpar_terminal()
            else:
                print('Caracter inválido')
        except ValueError:
            print('Caracter informado inválido.')
print('Gerador finalizado.')