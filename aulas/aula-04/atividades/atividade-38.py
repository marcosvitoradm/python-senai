# Peça ao usuário para digitar sua altura em metros.
altura = float(input('Digite sua altura em metros: \n'))

# Verifique se ela é maior que 1.75.
if altura > 1.75 and altura <= 2.20:
    print('Você é alto.') 
elif altura > 2.20 or altura <= 0.20:
    print('altura incorreta, corrija, por favor.')
else:
    print('Você não é alto.')

