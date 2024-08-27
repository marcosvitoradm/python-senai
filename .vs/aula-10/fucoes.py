'''num1 = int(input('Informe o número: \n'))
num2 = int(input('Informe o número: \n'))

print('A soma é:', num1 + num2)


# sum: soma os objetos
print(sum(numeros))


# max: achar maior número
print(max(numeros))

# min: achar o menor número
print(min(numeros))

# len: percorre os algaritimos do objeto
print(len(numeros))'''

numeros = [1, 2, 4, 9, 78, 120]
numeros_2 = [25, 48, 74]
def media (numeros):
    resultado = sum(numeros) / len(numeros)
    return resultado

print(media(numeros))

def soma (numeros):
    resultados = sum(numeros)
    return resultados
print(soma(numeros))

print(soma(numeros_2))
