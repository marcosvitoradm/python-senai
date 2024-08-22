# Solicite ao usuário um mês do ano (1 a 12).
mes = int(input('Digite o mês atual de forma numérica (1 a 12): \n'))

# Exibir a estação do ano correspondente.
if mes == 3 or mes == 4 or mes == 5:
    print('Outono')
elif mes == 6 or mes == 7 or mes == 8:
    print('Inverno')
elif mes == 9 or mes == 10 or mes == 11:
    print('Primavera')
elif mes == 12 or mes == 1 or mes == 2:
    print('Verão')
else:
    print("Mês inválido, digite de 1 a 12, por favor")

