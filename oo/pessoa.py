class Pessoa:

    def __init__(self, nome=None, idade=40):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    p = Pessoa('Fernando')
    print(p.nome)
    print(p.cumprimentar())
