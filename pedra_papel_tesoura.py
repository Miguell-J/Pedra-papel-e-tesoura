import random as rd

pontos_usuario = 0
pontos_maquina = 0

def jokenpo(pontos_usuario, pontos_maquina):
    
    print('------BEM VINDO AO JOKENPO!!!!!!------')
    print('------VOCÊ NÃO PODE ME GANHAR!!!!------')
    print('---QUEM CHEGAR A 5 PONTOS PRIMEIRO VENCE---')
    print('-----obs: boa sorte, vc vai precisar...---')

    
    while pontos_usuario or pontos_maquina < 5:
        
        if pontos_usuario == 5:
            print('------VOCÊ GANHOU!!!!------')
            break
        elif pontos_maquina == 5:
            print('----HAHAHA VOCÊ NUNCA VAI ME GANHAR!!!!----')
            break

        jogada_usuario = input("Escolha pedra, papel ou tesoura para jogar: \n").upper()
        lista_opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
        jogada_maquina = rd.choice(lista_opcoes)

        if jogada_usuario == 'PEDRA' and jogada_maquina == 'PEDRA':
            print('*' * 20)
            print('EMPATE!!!! \n')
            print('A sua escolha foi {}, e a escolha da máquina foi {} \n'.format(jogada_usuario, jogada_maquina))
            print("Pontos jogador: {} \nPontos maquina: {}\n".format(pontos_usuario, pontos_maquina))
            print('*' * 20)
            
        elif jogada_usuario == 'PEDRA' and jogada_maquina == 'PAPEL':
            pontos_maquina += 1
            print('*' * 20)
            print("VOCÊ PERDEU :( ")
            print('A sua escolha foi {}, e a escolha da máquina foi {}'.format(jogada_usuario, jogada_maquina))
            print("Pontos jogador: {} \nPontos maquina: {}".format(pontos_usuario, pontos_maquina))
            print('*' * 20)

        elif jogada_usuario == 'PEDRA' and jogada_maquina == 'TESOURA':
            pontos_usuario += 1
            print('*' * 20)
            print("VOCÊ VENCEU!!!!!")
            print('A sua escolha foi {}, e a escolha da máquina foi {}'.format(jogada_usuario, jogada_maquina))
            print("Pontos jogador: {} \nPontos maquina: {}".format(pontos_usuario, pontos_maquina))
            print('*' * 20)
            
            
        elif jogada_usuario == 'PAPEL' and jogada_maquina == 'PAPEL':
            print('*' * 20)
            print('EMPATE!!!!')
            print('A sua escolha foi {}, e a escolha da máquina foi {}'.format(jogada_usuario, jogada_maquina))
            print("Pontos jogador: {} \nPontos maquina: {}".format(pontos_usuario, pontos_maquina))
            print('*' * 20)
            
        elif jogada_usuario == 'PAPEL' and jogada_maquina == 'TESOURA':
            pontos_maquina += 1
            print('*' * 20)
            print("VOCÊ PERDEU :( ")
            print('A sua escolha foi {}, e a escolha da máquina foi {}'.format(jogada_usuario, jogada_maquina))
            print("Pontos jogador: {} \nPontos maquina: {}".format(pontos_usuario, pontos_maquina))
            print('*' * 20)

        elif jogada_usuario == 'PAPEL' and jogada_maquina == 'PEDRA':
            pontos_usuario += 1
            print('*' * 20)
            print("VOCÊ VENCEU!!!!!")
            print('A sua escolha foi {}, e a escolha da máquina foi {}'.format(jogada_usuario, jogada_maquina))
            print("Pontos jogador: {} \nPontos maquina: {}".format(pontos_usuario, pontos_maquina))
            print('*' * 20)

        elif jogada_usuario == 'TESOURA' and jogada_maquina == 'TESOURA':
            print('*' * 20)
            print('EMPATE!!!!')
            print('A sua escolha foi {}, e a escolha da máquina foi {}'.format(jogada_usuario, jogada_maquina))
            print("Pontos jogador: {} \nPontos maquina: {}".format(pontos_usuario, pontos_maquina))
            print('*' * 20)
            
        elif jogada_usuario == 'TESOURA' and jogada_maquina == 'PEDRA':
            pontos_maquina += 1
            print('*' * 20)
            print("VOCÊ PERDEU :( ")
            print('A sua escolha foi {}, e a escolha da máquina foi {}'.format(jogada_usuario, jogada_maquina))
            print("Pontos jogador: {} \nPontos maquina: {}".format(pontos_usuario, pontos_maquina))
            print('*' * 20)

        elif jogada_usuario == 'TESOURA' and jogada_maquina == 'PAPEL':
            pontos_usuario += 1
            print('*' * 20)
            print("VOCÊ VENCEU!!!!")
            print('A sua escolha foi {}, e a escolha da máquina foi {}'.format(jogada_usuario, jogada_maquina))
            print("Pontos jogador: {} \nPontos maquina: {}".format(pontos_usuario, pontos_maquina))
            print('*' * 20)
            
jokenpo(pontos_usuario, pontos_maquina)