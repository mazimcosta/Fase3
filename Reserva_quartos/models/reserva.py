

class Reserva:

    def __init__(self,cliente_id,quarto_id,dias):
        
        if dias<=0:
            raise ValueError('Dias invalido')
        
        
        self.cliente_id=cliente_id
        self.quarto_id=quarto_id
        self.dias=dias