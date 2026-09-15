print('======= O Portal do Julgamento de Santiago =======')
print('Seja bem-vindo, visitante!')

tipo = int(input('Que tipo de visitante você é? \n [1] - Peregrino \n [2] - Cavaleiro \n [3] - Clero \n [4] - Suspeito \n'))
dist = int(input('Qual a distância percorrida? \n'))
papa = input('Acaso carregais um induto papal? (Sim/Não) \n').lower()
armas = input('Está carregando armas visíveis? (Sim/Não) \n').lower()

if tipo == 3 or papa == 'sim':
    print('Acesso permitido ao altar principal!')

elif tipo == 1:
    if dist >= 100 and armas == 'não':
        print('Acesso permitido')
    else:
        print('Acesso negado!')

elif tipo == 2:
    if armas == 'sim':
        aceite = input('O cavaleiro aceita retirar as armas? (Sim/Não) ').lower()
        if aceite == 'sim':
            print('Acesso ao santuário permitido!')
        else:
            print('Já que não aceita desarmar-se, você será conduzido ao pátio externo do santuário.')
    else:
        if dist >= 50:
            print('Acesso permitido ao santuário!')
        else:
            print('Acesso negado! Distância percorrida insuficiente para um cavaleiro desarmado.')

else:
    print('Acesso negado, pagão, herege!')
