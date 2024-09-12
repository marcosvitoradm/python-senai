# peça ao usuário um número
solicitacao = int(input('insira um número de sua preferência: \n'))


# exiba todos os divisores desse número

print(f'Divisores de {solicitacao} são:')
for i in range(1, solicitacao + 1):
    if solicitacao % i == 0:
        print(i)
        
