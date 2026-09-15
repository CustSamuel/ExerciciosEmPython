# Mistério na Mansão Java.
  # O milionário Barão von Java foi assassinado na noite passada. Restaram 3 suspeitos na mansão: o Mordomo, a Governante e o Sobrinho. Como detetive chefe, você deve interrogar cada um deles e, no final, apontar o culpado ou declarar o caso como inconcluído.

print('======= INTERROGATÓRIO NA MANSÃO JAVA =======')
print('O notório Barão von Java foi assassinado em sua mansão. \n Você foi chamado para investigar o caso com urgência. \n Você deve interrogar individualmente: \n O Mordomo \n A Governanta \n O Sobrinho')

maior_suspeito = -1
nome_culpado = ""

for c in range (1,4):
  suspeito = 0
  nome = input('Suspeito {}. Digite o nome: \n'.format(c))
  alibi = int(input('Tinha álibi? (1- Sim/ 0- Não)'))
  motivo = int(input('Tinha motivo? (1- Sim/ 0- Não)'))
  escritorio = int(input('Visto próximo ao escritorio? (1- Sim/ 0- Não)'))

  if alibi == 0:
    suspeito = suspeito + 3
  if motivo == 1:
    suspeito = suspeito + 2
  if escritorio == 1:
    suspeito = suspeito + 4

  if suspeito > maior_suspeito:
    maior_suspeito = suspeito
    nome_culpado = nome

if maior_suspeito >= 6:
  if nome_culpado == 'Mordomo' or nome_culpado == 'Sobrinho':
    print("Caso Encerrado! O {} confessou sob pressão.".format(nome_culpado))
  else:
    print("Temos um culpado sólido: {} foi levado para a delegacia.".format(nome_culpado))

elif maior_suspeito > 3 and maior_suspeito < 5:
  print('As evidências contra {} são circunstanciais. Precisamos de mais investigações.'.format(nome_culpado))
else:
  print("O assassino planejou o crime perfeito. Todos os suspeitos parecem inocentes!")
