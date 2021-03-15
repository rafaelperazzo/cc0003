#Solicitar n
n = int(input("Digite n: "))

primeiro = (n*n)-n+1

soma = primeiro
proximo = primeiro + 2
print(primeiro)
for i in range(1,n,1):
    soma = soma + proximo
    print(proximo)
    proximo = proximo + 2

print(soma)
