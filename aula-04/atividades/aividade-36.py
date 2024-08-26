# Solicite ao usuário um número de 1 a 12. 
num1 = int(input('Digite aqui um número de 1 a 12: \n'))

# Exiba o mês correspondente.
meses = ['janeiro', 'fevereiro', 'março', 'abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
if 1<= num1 <=12:
    print(f'O mês correspondente é: {meses[num1-1]}.')
else:
    print('O número digitado não corresponde a um mês válido!')
    







