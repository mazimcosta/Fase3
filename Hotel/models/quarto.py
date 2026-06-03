


class Quarto:

    def __init__(self,numero,tipo,preco_diaria,disponivel=1):
        if preco_diaria<=0:
            raise ValueError('Preco invalido')
       
       
       
        self.numero=numero
        self.tipo=tipo
        self.preco_diaria=preco_diaria
        self.disponivel=disponivel