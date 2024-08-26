
#01 - Pergunta ao usuário um número de 1 a 3
numero = int(input("Digite um número de 1 a 3: \n"))

# Verifica qual número foi digitado e exibe o nome correspondente
if numero == 1:
    print("um")
elif numero == 2:
    print("dois")
elif numero == 3:
    print("três")
else:
    print("Número fora do intervalo de 1 a 3")

