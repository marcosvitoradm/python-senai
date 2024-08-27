# Peça ao usuário para inserir 7 números. 
lista_01 = 0

for i in range(7):
    num_01 = int(input(f'Digite aqui seu {i+1}º número: \n'))
    lista_01.append(num_01)

# Exiba quantos desses números são maiores que 10.
if lista_01 > 10:
        lista_01 +=1
print(f' maiores que 10 {lista_01}')



