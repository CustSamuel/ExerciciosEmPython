#  Exercício: O Grande Prêmio de Computação
  # Você foi contratado para criar o sistema de cronometragem de um treino classificatório de corrida. 3 pilotos vão correr na pista, um por vez. O seu objetivo é descobrir quem vai largar na Pole Position (primeiro lugar) e se o tempo dele foi um recorde histórico.

print('======= O Grande Prêmio de Computação =======')

maior_velocidade = -1
nome_pole = ""

for c in range (1, 4):
  velocidade = 0

  nome = input('Nome do piloto {}: '.format(c))
  velocidade = int(input('Qual a velocidade do piloto {}: '.format(c)))
  infracao = int(input('O piloto {} cortou caminho na curva? (1-Sim / 0-Não) '.format(c)))

  if infracao == 1:
    velocidade = velocidade - 50

  if velocidade > maior_velocidade:
    maior_velocidade = velocidade
    nome_pole = nome

if maior_velocidade >= 250:
 if nome_pole == 'Hamilton' or nome_pole == 'Senna' or nome_pole == 'Verstappen':
      print("Pole Position histórica! {} voou na pista com {} km/h!".format(nome_pole, maior_velocidade))
 else:
      print("Pole Position garantida para {} com incríveis {} km/h!".format(nome_pole, maior_velocidade))
elif maior_velocidade >= 150 and maior_velocidade < 250:
      print("{} vai largar na frente com {} km/h, mas o tempo foi mediano.".format(nome_pole, maior_velocidade))
else:
  print("O treino foi um desastre! {} larga na frente, mas a corrida será lenta.".format(nome_pole))
