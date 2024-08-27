# Peça ao usuário para inserir 5 números.
maior_num = []
for i in range(5):
    numeros = int(input(f'Digite aqui seu {i+1}º número. \n'))
    maior_num.append(numeros)
    
# E, ao final, exiba o maior número inserido.
print('Seu maior número é:', max(maior_num))



