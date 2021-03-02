# -*- coding: utf-8 -*-
'''
Fonte: https://docs.google.com/presentation/d/177g9N4hFAddzrY8drxVk1CDRtZ9ywSQB9KhqgymPGe0/edit#slide=id.gc0f05f94a3_0_64
Escreva um programa em Python que leia n valores inteiros positivos e 
mostre o menor valor
'''
#1) Pedir o valor de n (quantidade de números)
n = int(input('Digite o valor de n: '))

#2) Inicializar o menor
menor = int(input('Digite um número: '))

#3) Pedir os demais (n-1) números
for i in range(1,n,1):
    numero = int(input('Digite um número: '))
    if (numero<menor):
        menor = numero

#4) Mostrar o menor
print(menor)
