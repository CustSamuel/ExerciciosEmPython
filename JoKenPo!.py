import random

joken = ['Pedra', 'Papel', 'Tesoura']
joken = random.choice(joken)

po = int(input('Escolha uma opção: \n [1] - Pedra \n [2] - Papel \n [3] - Tesoura'))

print('JO')
print('KEN')
print('PO!')
print('. . .')

while True:
  if po == 1 and joken == 'Papel':
    print('Você escolheu Pedra e o computador escolheu Papel')
    print('Você perdeu!')
    break

  elif po == 1 and joken == 'Tesoura':
    print('Você escolheu Pedra e o computador escolheu Tesoura')
    print('Você ganhou!')
    break

  elif po == 1 and joken == 'Pedra':
    print('Você escolheu Pedra e o computador também escolheu Pedra')
    print('Empate!')

  elif po == 2 and joken == 'Papel':
    print('Você escolheu Papel e o computador escolheu Papel')
    print('Empate!')

  elif po == 2 and joken == 'Tesoura':
    print('Você escolheu Papel e o computador escolheu Tesoura')
    print('Você perdeu!')
    break

  elif po == 2 and joken == 'Pedra':
    print('Você escolheu Papel e o computador escolheu Pedra')
    print('Você ganhou!')
    break

  if po == 3 and joken == 'Papel':
    print('Você escolheu Tesoura e o computador escolheu Papel')
    print('Você ganhou!')
    break

  elif po == 3 and joken == 'Tesoura':
    print('Você escolheu Tesoura e o computador escolheu Tesoura')
    print('Empate!')

  elif po == 3 and joken == 'Pedra':
    print('Você escolheu Tesoura e o computador escolheu Pedra')
    print('Você perdeu!')
    break

  else:
    print('Opção inválida')
