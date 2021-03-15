# -*- coding: utf-8 -*-
'''
Dados n números fornecidos pelo usuário, calcular a média e o 
desvio padrão dos n números. n é um dado de entrada.

'''

#Pedir valor de n
n = int(input('Digite a quantidade de números: '))

#Pedir os n números
somatorio = 0
for i in range(0,n,1):
    numero = float(input('Digite um número: '))
    somatorio = somatorio + numero

media = somatorio/n
print(media)

