'''
2. Escreva uma função que recebe as 3 notas de um aluno por 
parâmetro e uma letra. Se a letra for A o procedimento 
calcula a média aritmética das notas do aluno, se for P, a sua 
média ponderada (pesos: 5, 3 e 2). A média calculada também 
deve ser retornada.

'''
def media(n1,n2,n3,p):
    if p=='A':
        media = (n1+n2+n3)/3
        return (media)
    else:
        media = (n1*5+n2*3+n3*2)/10
        return (media)

#ENTRADA E SAÍDA
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
p = input('Digite a letra: ')

print(media(n1,n2,n3,p))

