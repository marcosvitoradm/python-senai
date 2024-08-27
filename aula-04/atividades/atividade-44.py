# Peça ao usuário 10 números. 
numeros_pares = []
for i in range(10):
    num1 = int(input(f'Digite aqui seu {i+1}º número: \n'))
    

# Exiba apenas os números pares.
    if num1 % 2 == 0:
        numeros_pares.append(num1)
print('Seus números pares são:', numeros_pares)


