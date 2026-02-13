class Contrato:
    def __init__(self, valor_contrato=2000, parcelas=1):
        self.valor_contrato = valor_contrato
        self.parcelas = min(parcelas, 5)

    def calcular_parcela(self):
        return self.valor_contrato / self.parcelas