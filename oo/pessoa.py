class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=40):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    fernando = Pessoa(nome='Fernando')
    celso = Pessoa(fernando, nome='Celso', idade=67)
    print(celso.nome)
    print(celso.idade)
    print(celso.filhos)
    print(celso.cumprimentar())
    for filho in celso.filhos:
        print(filho.nome)
    celso.sobrenome = 'Machado'
    print(celso.sobrenome)
    del celso.filhos
    celso.olhos = 1
    print(celso.__dict__)
    print(fernando.__dict__)
    print(Pessoa.olhos)
    print(celso.olhos)
    print(fernando.olhos)