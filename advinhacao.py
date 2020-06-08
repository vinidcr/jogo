import pygame
#comando para importar a biblioteca.
def linha (tam = 65):
    return '-' * tam
#estou definindo a quantida de - que quero quando solicitar o comando linha.
from random import randint
#significa dizer que da biblioteca random estou solicitando apenas a função randint.
from time import sleep
#significa dizer que da biblioteca time estou solicitando apenas a função sleep.
sleep(1)
#o numero entre parenteses informa o tempo.
pygame.mixer.init()
#iniciando o pygame.
pygame.mixer.music.load('musica.mp3')
#carregando a musica dentro do jogo.
pygame.mixer.music.play()
#dando o comando para musica iniciar dentro de tudo que estiver no while abaixo.
while(pygame.mixer.music.get_busy()):
    print(linha())
    print('Sou sua máquina... Acabei de processar um número entre 0 e 50.')
    print('Será que você consegue aduvinhar qual foi?')
    palp = int(input('Escolha um número de 0 a 50:'))
    print(linha())
    comp = randint(0,50)
    tentativa = 1
    print(linha())
    print('PROCESSANDO..........')
    print(linha())
    sleep(1)
    while not palp == comp:
        tentativa += 1
        if palp > comp:
            print(linha())
            palp = int(input('Errou! Tente um número menor!: '))
            print(linha())
            print('Processando...')
            print(linha())
            sleep(1)
        elif palp < comp:
            print(linha())
            palp = int(input('Errou! Tente um número maior!: '))
            print(linha())
            print('Processando...')
            print(linha())
            sleep(1)
    print(linha())
    break
#esse break diz a hora que a musica deve parar, sem ele o jogo fica em loop e a musica continua.
print('Acertou! Eu pensei no número {}. você fez um total de {} tentativas'.format(comp, tentativa))
print(linha())


