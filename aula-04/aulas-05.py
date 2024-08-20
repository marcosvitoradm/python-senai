
# váriaveis
#numero1 = 5
#numero2 = 3
#idade = int(input('informe sua idade: \n'))
'''


# operador maior
print(numero1 > numero2)
print(numero2 > numero1)

# operador menor
print(numero1 < numero2)
print(numero2 < numero1)

# operador igual
print(numero1 == numero1)

# maior ou igual
print(numero1 >= numero2)
print(numero2 >= numero1)


# verificar se as váriaveis são diferente
print(numero1 != numero2)

if (idade > 120):
    print('Idade invalida')
elif (idade >= 18):
    print('idade invalida')
elif (idade < 0):
    print('não nasceu')
else:
    print('menor de idade')#

idade = int(input('informe sua idade: \n'))

if (idade >= 18):
    print('pode assistir')
elif(idade >= 16):
    acompanhado = input('Esta acompanhado de adulto, sim ou não? \n')
    if(acompanhado == 'sim'):
        print('pode assistir')
    else:
        print('não pode assistir')
else:
    print('não pode assistir')


idade = int(input('informe sua idade: \n'))
if (idade < 18):
    acompanhado = input('Esta acompanhado de adulto, sim ou não? \n')
    if (acompanhado == 'sim'):
        print('pode assistir')
    else:
        print('não pode assistir')
else:
    print('pode assistir')

alladin = input ('Alladin apareceu? \n')
jasmine = input ('Jasmine apareceu? \n')

if (alladin =='sim') and (jasmine == 'sim'):
    print('Love')
else:
    print('Não roulou')

trabalhei = input ('você trabalhou hoje? \n')
estudei = input ('você estudou hoje? \n')

if (trabalhei == 'sim') or (estudei == 'sim'):
    print('parabéns, vai ficar rico')
else:
    print('que pena, fica pra próxima vida!')'''

trabalhei = input ('você trabalhou hoje? \n')
estudei = input ('você estudou hoje? \n')

not if (trabalhei == 'sim') or (estudei == 'sim'):
    print('parabéns, vai ficar rico')









