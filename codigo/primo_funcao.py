'''
3. Faça uma função que recebe por parâmetro um valor inteiro e 
positivo e retorna o valor lógico Verdadeiro caso o valor seja primo 
e Falso em caso contrário.

'''

def primo(n):
    cont = 0 #contagem de divisores entre 2 e n-1
    for i in range(2,n,1):
        if (n%i==0):
            cont = cont + 1
            break
    if (cont==0):
        return (True)
    else:
        return (False)

#ENTRADA
numero = int(input('Digite o numero: '))
if (primo(numero)):
    print('PRIMO')
else:
    print('NAO PRIMO')

'''
Primos no intervalo

'''

'''
#Primos no intervalo [100,1000]
for i in range(100,1000,1):
    if primo(i):
        print(i)

for i in range(100,200,1):
    if primo(i):
        print(i)
'''