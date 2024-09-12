# peça ao usuário para inserir 5 números, adicione-os a uma lista
numeros = []


# depois, exiba a soma de todos os números na lista.
for i in range(5):
    num = float(input(f"Insira o número {i + 1}: "))
    numeros.append(num)


print("Os números inseridos foram:", numeros)
