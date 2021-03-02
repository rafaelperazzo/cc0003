# -*- coding: utf-8 -*-
'''
Fonte: https://docs.google.com/presentation/d/177g9N4hFAddzrY8drxVk1CDRtZ9ywSQB9KhqgymPGe0/edit#slide=id.gc0f05f94a3_0_64
Escreva um programa em Python que leia n valores inteiros positivos e 
mostre o maior valor
'''
#1) Pedir o valor de n
n = int(input("Digite o valor de n: "))

#2) Inicializar o maior
maior = 0
#3) Pedir cada um dos n números
for i in range(1,n+1,1):
    numero = int(input('Digite um número: '))
    if (numero>maior):
        maior = numero

#4) Mostrar o maior
print(maior)



