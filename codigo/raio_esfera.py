'''
1. Faça uma função que recebe por parâmetro o raio de uma esfera e 
calcula o seu volume (v = 4/3.Pi .R3).

'''
import math

def volume (raio):
    v = (4/3)*math.pi*(raio**3)
    return (v)


#ENTRADA
raio = float(input('Digite o raio: '))
print(volume(raio))

raio = float(input('Digite o raio: '))
print(volume(raio))
