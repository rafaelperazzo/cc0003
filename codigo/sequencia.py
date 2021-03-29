'''
Escreva um programa em Python que determine se uma sequência de n 
números fornecidos pelo usuário está em ordem 
crescente, decrescente ou aleatória.

ENTRADA

n - quantidade de números

cada um dos n números

SAÍDA

CRESCENTE, DECRESCENTE OU ALEATORIA (sem acentos)
'''
n = int(input('Digite n: '))
anterior = int(input('Digite um numero: '))
crescente = 0
descrescente = 0
for i in range(1,n,1):
    proximo = int(input('Digite um numero: '))
    if (proximo>anterior):
        crescente = crescente + 1
    else:
        descrescente = descrescente + 1
    anterior = proximo

if (crescente==n-1):
    print("CRESCENTE")
elif (descrescente==n-1):
    print("DECRESCENTE")
else:
    print("ALEATORIA")