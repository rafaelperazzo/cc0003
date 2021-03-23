'''
Escreva um	programa que leia	5 números	inteiros positivos 
(utilize uma  função que leia esse número e verifique se ele é positivo). 
Para cada número informado escrever a	soma	 
de seus divisores (exceto	ele	mesmo).	 
Utilize a função SomaDivisores para obter a soma.
Nome: SomaDivisores
Descrição:	Calcula a soma dos divisores do número informado 
(exceto	 ele	mesmo).	 

Entrada: Um número inteiro e positivo.	 
Saída: A soma dos divisores.	 
Exemplo: Para o valor 8: 1+2+4=7
'''
def positivo(n):
    if (n>0):
        return (True)
    else:
        return (False)

def soma_divisores(n):
    soma = 0
    for i in range(1,n,1):
        if (n%i==0):
            soma = soma + i
    return (soma)

#PROGRAMA PRINCIPAL
for i in range(1,6,1):
    n = int(input('Digite um numero: '))
    if (positivo(n)):
        print(soma_divisores(n))
    else:
        print("Numero nao e positivo!!")
    
