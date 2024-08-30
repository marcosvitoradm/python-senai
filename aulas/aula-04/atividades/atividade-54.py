#  solicite ao usuário um número.

num_01 = int(input('Digite aqui o número de sua preferencia: \n'))

 
#  continue pedindo outro número até que um número negativo seja inserido.


while num_01 >= 0:
    print(f'você digitou: {num_01}.')
    num_01 = int(input('Digite outro número ( ou um número negativo, caso queira sair: \n'))
print('número negativo inserido, programa encerrado.')



