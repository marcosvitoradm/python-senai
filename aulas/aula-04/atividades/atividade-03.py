#03 - Solicita ao usuário para inserir um número de 1 a 7
dia = int(input("Digite um número de 1 a 7 para o dia da semana: \n"))

# Verifica o número inserido e exibe o dia correspondente, começando pela segunda-feira
if dia == 1:
    print("Segunda-feira")
elif dia == 2:
    print("Terça-feira")
elif dia == 3:
    print("Quarta-feira")
elif dia == 4:
    print("Quinta-feira")
elif dia == 5:
    print("Sexta-feira")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("Número inválido. Por favor, insira um número entre 1 e 7.")

