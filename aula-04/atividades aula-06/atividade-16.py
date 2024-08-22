# Peça ao usuário um tipo de combustível (gasolina, etanol, diesel).
combustivel = (input('Qual o tipo de combustivel (gasolina, etanol, diesel): \n')).lower().strip()
gasolina = 6.13
etanol = 4.08
diesel = 5.95


# Exiba o preço correspondente por litro.

if combustivel == 'gasolina':
    print(f'o valor do seu combustivel é R$ {gasolina}.')
elif combustivel == 'etanol':
    print(f'o valor do seu combustivel é R$ {etanol}.')
elif combustivel == 'gasolina':
    print(f'o valor do seu combustivel é R$ {diesel}.')
else:
    print('combustivel inválido. Por favor, escolha o combustivel adequado.')
