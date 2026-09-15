print('======= BEM VINDO =======')
species = input('Qual a espécie do viajante? \n .Humano \n .Alienígena \n. Robô').lower()
passport = int(input('O passaporte está válido? \n [1] - Válido \n [2] - Inválido'))
sus = input('Carga suspeita? \n [1] - Sim \n [2] - Não') == '1'

if species == 'humano':
  if passport == 1:
    if sus == True:
      print("Acesso permitido, mas sua bagagem foi retida para inspeção.")
    else:
      print("Bem-vindo de volta a Nova Éden!")
  else:
    print("Passaporte expirado. Entrada proibida.")

elif species == "alienígena":
  if passport == 1 and sus == False:
    print("Entrada autorizada! Aproveite sua estadia interplanetária.")
  elif passport == 1 and sus == True:
    print("Entrada negada. Contrabando detectado!")
  else:
    print("Entrada negada. Procure a embaixada do seu sistema solar.")

elif species == 'robô':
  if sus == True:
    print("Acesso negado. Atualize suas diretrizes de segurança.")
  else:
    print("Acesso robótico liberado. Inicializando protocolos urbanos.")

else:
  print("Espécie não reconhecida. Por favor, tente novamente.")
