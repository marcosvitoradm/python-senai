# Solicitar a idade do usuário
idade = int(input("Digite sua idade: "))

# Verificar se a idade é válida
if idade <= 0:
    print("Erro: Idade inválida. A idade deve ser maior que zero.")
elif idade > 120:
    print("Erro: Idade inválida. A idade não pode ser maior que 120 anos.")
# Verificar se a idade é maior ou igual a 18
elif idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

