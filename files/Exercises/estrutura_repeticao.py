'''
#Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = float(input("insira uma nota:"))
while  nota < 1 or nota >10:
   nota =  float(input('insira novamente'))
else:
    print('ok')
'''
from typing import Any, Union

'''
#Programa que imprime a quantidade de números pares de 100 até 200

numb = range(100, 200, 2)
for x in numb:
    print(x)
'''
'''
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

login = input('insira o login')
senha = input('insira a senha')
while senha == login:
    senha = input('insira uma senha diferente do login')
    print('vai de novo')
else:
    print('ok')
'''
#Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
'''
nome = input('insira seu nome')
idade = int(input('insira sua idade'))
salario = float(input('insira seu salario'))
sexo = input('informe seu gênero com F para feminino, M para masculino e O para outro')
estadocivil = input('informe seu estado civil com S para solteiro, C para casado, V para viuvo e D para divorciado')
while len(nome)<3:
    nome = input('insira o seu nome novamente')
while idade <0 or idade > 150:
    idade = int(input('insira a sua idade novamente'))
while salario <= 0:
  salario = input('Salário: (maior que 0) ')
while sexo !='F' and sexo != 'M' and sexo != 'O':
  sexo = input('Sexo: [m/f/o]')
while estadocivil != 'S' and estadocivil != 'C' and estadocivil != 'V' and estadocivil != 'D':
  estadocivil = input('Estado Civil: [s/c/v/d]')
'''
'''
#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento
# de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
populacaoA, populacaoB, ano, taxaA, taxaB  = 80000, 200000, 0, 0.03, 0.015

while populacaoA < populacaoB:
    ano = ano+1
    populacaoA = populacaoA + (populacaoA*taxaA)
    populacaoB = populacaoB + (populacaoB * taxaB)
print(populacaoA)
print(populacaoB)
print(ano)
'''
'''
#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.
ano = 0
populacaoA =float(input('insira a população de A'))
while populacaoA < 0:
    populacaoA = float(input('insira a população de A'))
populacaoB = float(input('insira a população de B'))
while populacaoB < 0:
    populacaoB = float(input('insira a população de B'))
taxaA = float(input('insira a taxa de A'))
taxaB = float(input('insira a taxa de B'))
while populacaoA < populacaoB:
    ano = ano+1
    populacaoA = populacaoA + (populacaoA*taxaA)
    populacaoB = populacaoB + (populacaoB*taxaB)
print(populacaoA)
print(populacaoB)
print(ano)
'''
'''
#Faça um programa que leia 5 números e informe o maior número.
lista = []
quantidade = input('informe a quantidade de numeros: ')

for n in range(0,int(quantidade)):
    lista.append(int(input('Digite o número: ')))

print ('Maior número da lista: ', max(lista))   
'''
#Faça um programa que leia 5 números e informe a soma e a média dos números.
lista = []
quantidade = int(input('insira a quantidade de números'))
for i in range(0, int(quantidade)):
    lista.append(int(input('insira os numeros:')))
soma = sum(lista)
print(soma)
media = soma/quantidade
print(media)
