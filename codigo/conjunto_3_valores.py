# -*- coding: utf-8 -*-
'''
 Faça um programa que leia vários conjuntos de três valores reais e 
 mostre para cada conjunto: sua soma, seu produto e sua média. O programa para 
 quando um conjunto não entrar com seus valores em ordem crescente.

'''

while (True):
    #O que se repete ?
    n1 = float(input('Digite n1: '))
    n2 = float(input('Digite n2: '))
    n3 = float(input('Digite n3: '))
    soma = n1+n2+n3
    produto = n1*n2*n3
    media = soma/3
    print(soma)
    print(produto)
    print(media)
    #Critério de parada: Se não estiver em ordem crescente
    if (not(n1<n2<n3)):
        break






