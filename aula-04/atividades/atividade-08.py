# Solicitar o estado civil do usuário
estado_civil = input("Digite o seu estado civil (solteiro, casado, divorciado, viúvo): ").lower()

# Exibir mensagem correspondente ao estado civil
if estado_civil == "solteiro":
    print("Você está solteiro.")
elif estado_civil == "casado":
    print("Você está casado.")
elif estado_civil == "divorciado":
    print("Você está divorciado.")
elif estado_civil == "viúvo":
    print("Você está viúvo.")
else:
    print("Estado civil inválido!")
