frutas = ['acerola', 'maçã', 'uva', 'umbu']


def listar_frustas():
    for i in frutas:
        print(i)


def adicionar_fruta(nome):
    frutas.append(nome)


fruta = input('Qual fruta deseja cadastrar: \n')

adicionar_fruta(fruta)
listar_frustas()


