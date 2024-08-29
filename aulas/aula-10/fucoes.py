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
print(len(numeros))

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

def saudacao(nome):
    print(f'Olá {nome}!')

saudacao('Marcos Vitor')

def ola(mensagem, nome = 'olá'):
    print(mensagem, nome)
ola('oi,', 'Marcos Vitor')
ola('Marcos')

numeros = [1, 2, 4, 9, 78, 120]
numeros_2 = [25, 48, 74]

def dividir(numeros, numeros_2):
    resposta = numeros //numeros_2
    resto = numeros % numeros_2
    return resposta, resto

divisao, resto_divisao = dividir(10,2)
print(divisao)
print(resto_divisao)

def dividir(numeros, numeros_2):
    resposta = numeros //numeros_2
    resto = numeros % numeros_2
    return resposta, resto
divisao = dividir(10,2)
print(divisao)

def soma (numeros):
    resultados = sum(numeros)
    return resultados


somar = lambda a, b: a+b
print(somar(10,70))

def exibir_informacoes(*args):
    print('Argumentos posicionais: ', args)

exibir_informacoes(1, 4, 'Marcos', 'Teste')

def exibir_informacoes2(**args):
    print('Argumentos posicionais: ', args)

exibir_informacoes2(nome ='Marcos', idade = 36, curso = 'Python')'''


pessoas = [{'nome': 'Marcos', 'idade': '36', 'formação': 'administração'},
{'nome': 'Caio','escolaridade':'superior'}]

print(pessoas[0])


    

