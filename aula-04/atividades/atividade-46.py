# Peça ao usuário para inserir 5 números. 
import statistics


lista_01 = []
for i in range(5):
    numeros = float(input(f'Digite aqui seu n{i+1}º número: \n'))
    lista_01.append(numeros)
media = statistics.mean(lista_01)

# Exiba a média dos números inseridos.
print('A média dos seus números é:', media)