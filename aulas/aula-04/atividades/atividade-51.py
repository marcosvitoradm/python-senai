
# Peça ao usuário para inserir números até que ele digite o número 0. 
soma = 0
while True:
    numero_01 = int(input('Digite números inteiros (digite 0 para sair): \n'))
    if numero_01 == 0:
        break
    
# Ao final, exiba a soma de todos os números inseridos (exceto o 0).

    soma += numero_01
    print('A soma de todos os números inseridos é:', soma)
    

