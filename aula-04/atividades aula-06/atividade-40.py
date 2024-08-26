# Peça ao usuário para inserir três números.
num1 = float(input('Digite aqui o primeiro número: \n'))
num2 = float(input('Digite aqui o segundo número: \n'))
num3 = float(input('Digite aqui o terceiro número: \n'))

# Verifique se todos são iguais.
if num1 == num2 == num3:
    print('Todos os números digitados são iguais.')
else:
    print('Os número digitados não são iguais.')
    