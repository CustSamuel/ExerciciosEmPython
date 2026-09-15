#Alistamento militar

nasc = int(input('Qual o seu ano de nascimento? '))
ano = int(input('Em que ano estamos? '))

idd = ano - nasc

if idd < 18:
  print('Ainda não é hora de se alistar')
  print(f'Faltam {18 - idd} anos para o alistamento')

elif idd > 18:
  print('Já passou da hora de se alistar')
  print(f'Você deveria ter se alistado há {idd - 18} anos')
else:
  print('Você deve se alistar esse ano')
  print('Prepare-se para o serviço militar')
