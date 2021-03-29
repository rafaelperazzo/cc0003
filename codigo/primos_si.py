'''
Escreva um programa em Python que determine se dois valores 
inteiros e positivos A e B são primos entre si.

Chamamos números primos entre si (ou coprimos) ao conjunto de números 
onde o único divisor comum a todos eles é o número 1.

Dica: A e B são primos entre si quando o MDC de A,B é 1.

Exemplo:

Verificar se são coprimos os números 20 e 21:

Divisores de 20: 1, 2, 4, 5, 10 e 20.
Divisores de 21: 1, 3, 7 e 21.
Resposta: Os números 20 e 21 são primos entre si, pois o único divisor 
comum entre os dois é o 1.
ENTRADA

2 números inteiros

SAÍDA

SIM ou NAO (sem o ~)
'''

a = int(input('Digite a: '))
b = int(input('Digite b: '))
mdc = 1
for i in range(1,b,1):
    if (a%i==0) and (b%i==0):
        mdc = i

if (mdc==1):
    print("SIM")
else:
    print("NAO")

