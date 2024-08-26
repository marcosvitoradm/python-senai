'''# Peça ao usuário um número inteiro positivo. 
num1 = int(input('Digite um número inteiro positivo: \n'))

# Exiba todos os números de 1 até o número informado.

if num1 > 0:
    for i in range(1, num1 = 1):
        print(i)'''

        # Solicitar um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verificar se o número é positivo
if numero > 0:
    # Exibir todos os números de 1 até o número informado
    for i in range(1, numero + 1):
        print(i)
else:
    print("Por favor, insira um número inteiro positivo.")


