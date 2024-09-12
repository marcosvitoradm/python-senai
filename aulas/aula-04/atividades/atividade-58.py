# solicite ao usuário uma palavra
solicitacao = str(input('Digite uma palavra chave para sair: \n'))


# e continue pedindo outra palavra até que ele digite "sair".

while solicitacao.lower() != 'senhora':
    print('Você errou, tente novamente: \n')
    solicitacao = str(input('tente novamente: \n'))




