'''
Fonte: https://docs.google.com/presentation/d/177g9N4hFAddzrY8drxVk1CDRtZ9ywSQB9KhqgymPGe0/edit#slide=id.gc0f05f94a3_0_64
Escreva um programa em Python que mostre todos os ímpares menores que n. 
'''
#1) Pedir o valor de n
n = int(input('Digite o valor de n: '))

#2) Fazer o i varia de 1 até n-1
for i in range(1,n,1):
    if (i%2)==1:
        print(i)

#Alternativa:
for i in range(1,n,2):
    print(i)