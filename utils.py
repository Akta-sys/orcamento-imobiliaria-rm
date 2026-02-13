import csv

def gerar_csv(valor_mensal):
    with open("orcamento.csv", mode="w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Parcela", "Valor"])

        for i in range(1, 13):
            writer.writerow([i, valor_mensal])