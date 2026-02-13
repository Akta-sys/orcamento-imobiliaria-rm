from imovel import Imovel
from contrato import Contrato
from utils import gerar_csv

def main():
    print("=== GERADOR DE ORÇAMENTO R.M ===")

    tipo = input("Tipo do imóvel (Apartamento, Casa, Estúdio): ")
    quartos = int(input("Número de quartos (1 ou 2): "))
    garagem = int(input("Quantidade de vagas na garagem: "))
    criancas = input("Tem crianças? (Sim/Não): ").strip().lower() == "sim"
    parcelas = int(input("Número de parcelas (1 a 5): "))

    imovel = Imovel(tipo, quartos, garagem, criancas)
    valor_aluguel = imovel.calcular_aluguel()

    contrato = Contrato(parcelas=parcelas)
    valor_parcela_contrato = contrato.calcular_parcela()

    print(f"\nValor mensal do aluguel: R$ {valor_aluguel:.2f}")
    print(f"Contrato parcelado em {contrato.parcelas}x de R$ {valor_parcela_contrato:.2f}")

    gerar_csv(valor_aluguel)
    print("Arquivo CSV gerado com sucesso!")

if __name__ == "__main__":
    main()