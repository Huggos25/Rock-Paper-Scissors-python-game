'''
Jogo Pedra Papel tesoura

tesoura > papel
tesoura == tesoura
tesoura < pedra

papel > pedra
papel == papel
papel < tesoura

pedra > tesoura
pedra == pedra
pedra < papel

'''

#importado random para geração aleatoria
#importado time para definir tempo neste caso tempo de espera
#importado os para fazer linhas de comando ocultas os(operative system)
import random
import time
import os

#Menu de arranque
def menu():
    os.system('cls')
    print('################--BEM VINDO--################')
    print('#---------Jogo do Pedra Papel Tesoura-------#')
    print('#-----------feito por Hugo Vieira-----------#')
    print('#############################################')

#Mecanica do jogo
def jogo(escolha, escolhaAI, nome):

        ficheiro = open("resultadosfinais.txt", "a")
        #Caso seja igual a opção retorna empate
        if escolha == escolhaAI:
            print(nome,'EMPATOU O JOGO!\n','\n',nome,'jogou',escolha,'e o Bot escolheu',escolhaAI)
            ficheiro.write('\n------------------------\n')
            ficheiro.write('"EMPATOU O JOGO!"\n')
            ficheiro.write(str(nome) + '---' + str(escolha)+'\n')
            ficheiro.write('Bot---' + str(escolhaAI)+ '\n')
            ficheiro.write('\n')
            ficheiro.write(str(time.ctime()))
            ficheiro.write('\n------------------------\n')
            ficheiro.write('\n')
            time.sleep(2)
  
        #Caso seja a escolha do user seja vencedora retorna que ganhou a ronda
        elif (escolha == 'tesoura' and escolhaAI == 'papel') or (escolha == 'papel' and escolhaAI == 'pedra') or (escolha == 'pedra' and escolhaAI == 'tesoura'):
            print(nome,'GANHOU O JOGO!\n','\n',nome,'jogou',escolha,'e o Bot escolheu',escolhaAI)
            ficheiro.write('\n------------------------\n')
            ficheiro.write('"GANHOU O JOGO!"\n')
            ficheiro.write(str(nome) + '---' + str(escolha)+'\n')
            ficheiro.write('Bot---' + str(escolhaAI)+ '\n')
            ficheiro.write('\n')
            ficheiro.write(str(time.ctime()))
            ficheiro.write('\n------------------------\n')
            ficheiro.write('\n')
            time.sleep(2)
       
        #Caso seja a escolha do user seja derrotada retorna que perdeu a ronda
        elif (escolha == 'tesoura' and escolhaAI == 'pedra') or (escolha == 'papel' and escolhaAI == 'tesoura') or (escolha == 'pedra' and escolhaAI == 'papel'):
            print(nome,'PERDEU O JOGO\n','\n',nome,'jogou',escolha,'e o Bot escolheu',escolhaAI)
            ficheiro.write('\n------------------------\n')
            ficheiro.write('"PERDEU O JOGO!"\n')
            ficheiro.write(str(nome) + '---' + str(escolha)+'\n')
            ficheiro.write('Bot---' + str(escolhaAI)+ '\n')
            ficheiro.write('\n')
            ficheiro.write(str(time.ctime()))
            ficheiro.write('\n------------------------\n')
            ficheiro.write('\n')
            time.sleep(2)

def main():
    menu()

    #Apenas inserir o nome
    time.sleep(2)
    nome = input('Insira seu nome:')
    if (nome == ""):
        print('Nao inseriu nome!')
        return main()
    elif (nome != ""):
        print()

    #Necessidade de saida por parte do usuario!
    time.sleep(1)
    print('SE PRETENDER SAIR DEIA ENTER')
    print()

    #Prevenção de crash do jogo e opção nao seja as dadas!
    while True:

        #Gerar da lista alguma opção pra jogar
        list = ["pedra","papel","tesoura"]
        escolha = input('Pedra/Papel/Tesoura:')
        escolha = escolha.lower()
        escolhaAI = random.choice(list)

        #Caso nao ponha nada acaba o jogo
        if(escolha == ""):
            print('FIM DO JOGO!')
            break

        #Caso nao corresponda as opções renicia
        elif escolha not in ('pedra', 'papel','tesoura'):
            print('Escolha invalida!\n')
            continue
        
        #Renicia a escolha, o jogo e limpa o terminal
        else:
            escolha = escolha.lower()
            jogo(escolha, escolhaAI, nome)
            time.sleep(4)
            os.system('cls')
main()