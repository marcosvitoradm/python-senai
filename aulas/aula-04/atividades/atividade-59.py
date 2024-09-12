# solicite ao usuário para digitar dois números
solicitacao_1 = int(input('Digite o primeiro número de sua preferência: \n'))
solicitacao_2 = int(input('Digite o segundo número de sua preferência: \n'))
# verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo.

while solicitacao_1 <= solicitacao_2:
    print('O primeiro número não é maior que o segundo, continue tentando.')
    solicitacao_1 = int(input('Digite o primeiro número de sua preferência: \n'))
    solicitacao_2 = int(input('Digite o segundo número de sua preferência: \n'))

print('O primeiro número é maior que o segundo. comando encerrado.')



