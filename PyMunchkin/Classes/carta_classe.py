from Classes.carta import Carta


class Classe(Carta):
    def __init__(
        self,
        imagepath,
        nome,
        descricao,
        efeito,
        tipo,
        habilidadesClasse,
        # poder,
        # tamanho,
        # valor,
        # restricao,
        # usoUnico,
    ):
        super().__init__(imagepath, nome, descricao, efeito, tipo)
        self.habilidadesClasse = habilidadesClasse
        # self.poder = poder
        # self.tamanho = tamanho
        # self.valor = valor
        # self.restricao = restricao
        # self.usoUnico = usoUnico

    def habilidadeClasse(self):
        pass

