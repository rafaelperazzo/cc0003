def divisores(n):
    cont = 0
    for i in range(1,n+1,1):
        if (n%i==0):
            cont = cont + 1;
    return (cont)

numero = int(input('Digite o numero: '))
qtde_divisores = divisores(numero)
print(qtde_divisores)
