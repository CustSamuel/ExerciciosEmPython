#Simulador de financiamento de uma casa

casa = int(input('Insira o valor da casa'))
finan = int(input('Financiamento em quantos anos? '))
salario = int(input('Seu salario? '))

porc = salario * 0.3
parcela = casa / (finan * 12)

if parcela > porc:
  print('Financiamento negado!')
else:
  print('Financiamento aceito!')
