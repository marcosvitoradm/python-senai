# Solicitar que o usuário escolha um modo de transporte
transporte = input("Escolha um modo de transporte (carro, bicicleta, a pé): \n").lower()

# Exibir a velocidade média correspondente
if transporte == "carro":
    print("A velocidade média de um carro é de aproximadamente 100 km/h.")
elif transporte == "bicicleta":
    print("A velocidade média de uma bicicleta é de aproximadamente 20 km/h.")
elif transporte == "a pé":
    print("A velocidade média de uma pessoa a pé é de aproximadamente 5 km/h.")
else:
    print("Modo de transporte inválido!")
