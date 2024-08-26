# Pedir ao usuário para digitar dois números.

numero1 = float(input('Digite o primeiro número: \n'))
numero2 = float(input('Digite o segundo número: \n'))

# Calcula a soma dos dois números
soma = numero1 + numero2

# Verifica se a soma é maior que 100
if soma > 100:
    print("A soma dos números é maior que 100.")
else:
    print("A soma dos números não é maior que 100.")
    
