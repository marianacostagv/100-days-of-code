idade = int(input('qual a sua idade'))
peso = int(input('qual seu peso'))
altura = float(input('qual a sua altura'))

if idade >= 18 and peso >= 50 and altura >= 1.7:
    print("você está apto a entrar no exército")
else:
    print('nao está apto')
