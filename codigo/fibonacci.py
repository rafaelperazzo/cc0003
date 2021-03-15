# -*- coding: utf-8 -*-
'''
Escreva um programa para gerar os n primeiros termos da seqüência: 
1 1 2 3 5 8 13 21 34 55 89 …

'''
#Pedir valor de n
n = int(input('Digite o valor de n:'))

anterior1 = 1
anterior2 = 1
for i in range(3,n+1,1):
    an = anterior1+anterior2
    print(an)
    anterior1 = anterior2
    anterior2 = an
