print('======= BEM VINDO =======')
print('Jornada do Héroi!')

nome = input('Nobre herói, diga-me o teu nome: \n')
classe = int(input('Qual a sua classe? \n [1] - Mago \n [2] - Guerreiro \n [3] - Arqueiro'))
hp = 100
moedas = 0
desmaiou = False

for c in range (1,5):
  qtd_moedas = int(input('Quantas moedas você coletou no dia {}?'.format(c)))
  moedas = moedas + qtd_moedas
  qtd_hp = int(input('Quantos pontos de hp você perdeu no dia {}?'.format(c)))
  hp = hp - qtd_hp
  if hp < 0: desmaiou = True
  break

if hp > 0:
  print('Você terminou a campanha vivo!')
  if moedas > 500 or classe == 1:
    print("Tesouro Lendário obtido!")
  else:
    print("Bolsa de Ouro Comum obtida.")
elif hp <= 0:
  print("Você desmaiou durante a campanha!")
  if moedas > 200:
    print("Resgatado pela guilda, mas perdeu metade do ouro." )
    moedas = moedas / 2
    print('Saldo final: {}'.format(moedas))
  else:
    print("Fim de jogo: Perdeu tudo e acordou na taverna sem um tostão.")
else:
  print('Insira dados válidos!')

print('RELATÓRIO FINAL DA QUEST:')
print('Nome do aventureiro: {} \n Classe: {} \n Hp final: {} \n Dinheiro final: {}'.format(nome, classe, hp, moedas))
