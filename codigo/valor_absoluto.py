'''
Escreva um programa em	 Python que leia 5 valores	inteiros e imprima 
para cada um o seu correspondente valor absoluto.	
Para obter o	valor absoluto do número utilize a 
função Absoluto especificada abaixo:		 
Nome: Absoluto
Descrição: Retorna o valor absoluto do número fornecido. 
Entrada:	 n
Saída: (int) O	respectivo valor absoluto	de n. 
'''
def absoluto(n):
    if (n<=0):
        return(n*(-1))
    else:
        return (n)

#PROGRAMA PRINCIPAL
for i in range(1,6,1):
    n = int(input('Digite um numero: '))
    print(absoluto(n))

