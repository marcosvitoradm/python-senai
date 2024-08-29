# Peça ao usuário para digitar um número.
num1 = int(input('Digite aqui um número inteiro: \n'))

# Verifique se ele é múltiplo de 2 ou de 5.
if num1 % 2 == 0 or num1 % 5 == 0:
    print('Esse número é múltiplo de 2 ou de 5.')
else:
    print('Esse número não é múltiplo de 2 ou de 5.')
