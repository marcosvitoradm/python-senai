# Peça ao usuário três números 
# Solicita ao usuário três números
num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))
num3 = float(input("Digite o terceiro número: \n"))

# Verifica se todos os números são positivos
if num1 > 0 and num2 > 0 and num3 > 0:
    print("Todos os números são positivos.")
else:
    print("Nem todos os números são positivos.")

