# -*- coding: utf-8 -*-
'''
Sabe-se que um número da forma n^3 é igual a soma de n ímpares consecutivos.
Exemplo: 1^3= 1, 2^3= 3+5, 3^3= 7+9+11,  4^3= 13+15+17+19,...
Dado n, determine os ímpares consecutivos cuja soma é igual a n^3.

'''
n = int(input('Digite n:'))

u = (n*n)+(n-1)
soma = 0
for i in range(u,u-(2*n-1),-2):
    print(i)
    soma = soma + i

#print(soma)

