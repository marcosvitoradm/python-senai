#04 - Solicita ao usuário para inserir uma cor
cor = input("Digite uma cor (vermelho, verde, azul): \n").lower()

# Verifica a cor inserida e exibe a mensagem correspondente
if cor == "vermelho":
    print("Você escolheu a cor vermelha!")
elif cor == "verde":
    print("Você escolheu a cor verde!")
elif cor == "azul":
    print("Você escolheu a cor azul!")
else:
    print("Cor inválida. Por favor, escolha entre vermelho, verde ou azul.")