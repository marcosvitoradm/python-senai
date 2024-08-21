#05 - Solicita dois números ao usuário
numero1 = int(input("Digite o primeiro número: \n"))
numero2 = int(input("Digite o segundo número: \n"))

# Verifica se ambos os números são pares
if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos os números são pares.")
else:
    print("Algum dos números não é par.")
    
