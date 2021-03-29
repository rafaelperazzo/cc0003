'''
Escreva um programa em Python que determine o MMC (mínimo múltiplo comum) 
entre dois números A e B.

O mínimo múltiplo comum (MMC) corresponde ao menor 
número inteiro positivo, diferente de zero, que é múltiplo ao 
mesmo tempo de dois ou mais números.

Lembre-se que para encontrar os múltiplos de um 
número, basta multiplicar esse número pela sequência dos números naturais.

Note que o zero (0) é múltiplo de todos os números naturais 
e que os múltiplos de um número são infinitos.

Para saber se um número é múltiplo de um outro, devemos descobrir 
se um é divisível pelo outro.

Por exemplo, 25 é múltiplo de 5, pois ele é divisível por 5.

Dica: O MMC(A,B) é no máximo A*B

ENTRADA

2 números inteiros

SAÍDA

o valor do MMC entre A e B
'''

a = int(input('Digite a: '))
b = int(input('Digite b: '))

for i in range(1,(a*b)+1,1):
    if (i%a==0) and (i%b==0):
        print(i)
        break