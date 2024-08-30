#  peça ao usuário um número.
num_final = 1
num_01 = int(float(input('Digite aqui o número que desejar: \n')))



#  exiba a contagem regressiva desse número até 1.
if num_01 >= 1:
    for i in range(num_01, 0, -1):
        print(i)
else:
    print('por favor, digite um número maior ou igual a 1.')

    


