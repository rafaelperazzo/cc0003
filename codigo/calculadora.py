'''
Escrever uma função que represente uma máquina de calcular, 
com as opções das operações fundamentais, fatorial, potência e raiz quadrada. 

'''
def fatorial(n):
    fat = 1
    
    for i in range(1,n+1,1):
        fat = fat * i
    
    return (fat)


def calculadora(operacao,a,b):
    if (operacao=='+'):
        return(a+b)
    elif (operacao=='-'):
        return(a-b)
    elif (operacao=='*'):
        return(a*b)
    elif (operacao=='/'):
        return(a/b)
    elif (operacao=='r'):
        return(a**(0.5))
    elif (operacao=='p'):
        return(a**b)
    else:
        return(fatorial(a))

#PROGRAMA PRINCIPAL

#ENTRADA: operação e os números
while (True):
    operacao = input('Digite a operacao (r)aiz, (p)otencia (f)atorial (+,-,*,/) fundamental (s)air: ')
    if (operacao=='s'):
        break
    else:
        a = float(input('Digite o primeiro numero: '))
        b = float(input('Digite o segundo numero (0) se nao houver: '))
        print(calculadora(operacao,a,b))
    