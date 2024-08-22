# Solicitar a operação ao usuário
operacao = input("Escolha uma operação (+, -, *, /): \n")

# Solicitar os dois números ao usuário
num1 = float(input("Insira o primeiro número: \n"))
num2 = float(input("Insira o segundo número: \n"))

# Realizar a operação escolhida
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:  # Verifica se o divisor não é zero para evitar erro de divisão
        resultado = num1 / num2
    else:
        resultado = "Erro! Divisão por zero não permitida."
else:
    resultado = "Operação inválida!"

# Exibir o resultado
print("O resultado é:", resultado)