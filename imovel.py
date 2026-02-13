class Imovel:
    def __init__(self, tipo, quartos=1, garagem=0, tem_criancas=True):
        self.tipo = tipo.lower()
        self.quartos = quartos
        self.garagem = garagem
        self.tem_criancas = tem_criancas

    def calcular_aluguel(self):
        valor = 0

        if self.tipo == "apartamento":
            valor = 700
            if self.quartos == 2:
                valor += 200
            if not self.tem_criancas:
                valor *= 0.95

        elif self.tipo == "casa":
            valor = 900
            if self.quartos == 2:
                valor += 250

        elif self.tipo == "estudio":
            valor = 1200
        
        # Garagem para casa e apartamento
        if self.tipo in ["apartamento", "casa"]:
            valor += self.garagem * 300

        # Estúdio tem regra diferente
        if self.tipo == "estudio":
            if self.garagem >= 2:
                valor += 250
                if self.garagem > 2:
                    valor += (self.garagem - 2) * 60

        return valor