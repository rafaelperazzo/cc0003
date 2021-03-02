'''
Fonte: https://docs.google.com/presentation/d/177g9N4hFAddzrY8drxVk1CDRtZ9ywSQB9KhqgymPGe0/edit#slide=id.gc0f05f94a3_0_64
Escreva um programa em Python que leia n valores inteiros positivos e 
mostre a média aritmética
'''

#1) Pedir a quantidade de números
n = int(input('Digite a quantidade de números: '))

#2) Inicializar o somatório
soma = 0

#3) Pedir cada um dos n números e colocar no somatório
for i in range(1,n+1,1):
    numero = float(input('Digite um número: '))
    soma = soma + numero

#4) Mostra a média
print(soma/n)

