'''candidato = int(input('informe o número do candidato: \n'))

if candidato == 13:
    print('votou no lula \n')
elif candidato == 22:
    print('votou no bolsonaro \n')
else:
    print('candidato invalido \n')

# com _ podemos marcar as opções fora das anteriores
match candidato:
    case 13:
        print('votou no Lula')
    case 22:
        print('votou no Bolsonaro')
    case _:
        print('opção invalida')

numero = 10
print(numero)
    
numero = numero + 10
print(numero)

numero = numero - 10
print(numero)

numero = numero * 10
print(numero)

numero = numero / 10
print(numero)

numero = 10
print(numero)

numero *= 10
print(numero)

# VERIICANDO SE UM NUMERO É PAR OU IMPAR

numero = int(input('informe o número\n'))

if numero % 2 == 0:
    print('numero é par')
else:
    print('numero é impar')

# LAÇOS DE REPETIÇÃO

for i in range(5):
    print('Marcos Vitor')


nomes = ['Luciano', 'lucas', 'Arthur', 'Aline', 'Beatriz']

print(nomes)

for nome in nomes:
    print(nome)

frutas = ['banana', 'maça', 'morango', 'laranja']
for fruta in frutas:
    print(fruta)

frutas = ['banana', 'maça', 'morango', 'laranja']
for fruta in range(10):
    print(fruta)

from tracemalloc import start


frutas = ['banana', 'maça', 'morango', 'laranja']
for item in frutas:
    print(frutas[3])



for indice, fruta in enumerate(frutas, start=1):
    print(indice, fruta)

nomes = []
for i in range(5):
    nome = input('Informe o seu nome: \n')
    nomes.append(nome)
for nome in nomes:
    print(nome)

# WHILE EM PORTUGÊS ENQUANTO NÃO DIGITAR O NUMERO QUE FAZ PARAR

numero=None
while numero !=0:
    numero = int(input('Informe o númerio: \n'))

contador = 1
numero = input('informe o número: \n')
while contador<10:
    print(numero*2)
    contador +=1'''
    
    











    









