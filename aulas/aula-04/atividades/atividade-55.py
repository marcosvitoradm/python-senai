# peça ao usuário para inserir um número maior que 100.
numero = int(input('Insira aqui um número maior que 100: \n'))


# Se o número for menor ou igual a 100, continue pedindo até que um número maior que 100 seja inserido.

while numero <= 100:
    print(f'Seu número é {numero}.')
    numero = int(input('Insira aqui um número maior que 100: \n'))

print("Encerrado.")

