from random import randint
import os

def gerar_numeros(qtd):
    numeros_gerados = []
    while len(numeros_gerados) != qtd:
        numero = randint(1,60)
        if numero in numeros_gerados:
            numeros_gerados.pop()
        else:
            numeros_gerados.append(numero) 
    return numeros_gerados

def limpar_terminal():
    sistema_operacional = os.name
    if sistema_operacional == 'posix':  # Unix/Linux/Mac
        os.system('clear')
    elif sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:
        print("Não foi possível detectar o sistema operacional. Tente limpar manualmente.")


label = (f'self.resultado{1}_label')                
print(label)