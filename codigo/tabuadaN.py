# -*- coding: utf-8 -*-
'''
Fonte: https://docs.google.com/presentation/d/177g9N4hFAddzrY8drxVk1CDRtZ9ywSQB9KhqgymPGe0/edit#slide=id.gc0f05f94a3_0_64
Escreva um programa em Python que mostre a tabuada de um número fornecido 
pelo usuário. (considerar a tabuada do número 1 ao 10).
'''
#COM O WHILE
n = int(input('Digite o valor de n: '))
i = 1
while (i<=10):
    print(n*i)
    i = i + 1

#COM O FOR
for i in range(1,11,1):
    print(n*i)


