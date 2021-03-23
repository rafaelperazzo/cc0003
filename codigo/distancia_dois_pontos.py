'''
Escreva	uma	função	que	calcule e	retorne a	distância	entre	
dois	pontos	( x1, y1)	e	 (x2, y2).	
Todos	os números	e	 valores	de	 retorno	devem	ser	do	 
tipo	float.
'''

def distancia(x1,y1,x2,y2):
    d = (((x2-x1)**2) + ((y2-y1)**2))**(0.5)
    return (d)

#PROGRAMA PRINCIPAL
#ENTRADA: x1,y1,x2,y2
x1 = float(input('Digite x1: '))
y1 = float (input('Digite y1: '))
x2 = float(input('Digite x2: '))
y2 = float (input('Digite y2: '))
#PROCESSAMENTO CHAMANDO A FUNÇÃO
d = distancia(x1,y1,x2,y2)
print(d)
