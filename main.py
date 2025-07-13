import os
from src.pipeline import executar_reconstrucao_genomica
from src.utils import Utils
from src.gerenciador import Gerenciador_de_Genomas


def main():
    while True:
        print("\n=== Reconstrução de Sequências Genéticas ===\n")
        print("Escolha um dos testes abaixo:\n")
        print("1. Genoma da bactéria - Genoma real do vírus Escherichia phage, ideal para simulação biológica realista.")
        print("2. Genoma pequeno (tamanho 8) - Genoma artificial simples para testes rápidos e visualização clara.")
        print("3. Genoma médio (tamanho 80) - Genoma artificial de tamanho moderado para testar reconstrução com complexidade intermediária.")
        print("4. Genoma grande (tamanho 800) - Genoma artificial maior, ideal para observar desempenho e precisão.")
        print("5. Genoma muito grande (tamanho 8000) - Genoma ainda mais extenso, útil para avaliar tempo e qualidade de reconstrução.")
        print("6. Genoma enorme (tamanho 80000) - Genoma sintético de grande porte para testes de performance pesada.")
        print("9. Teste Personalizado - Você define o tamanho do genoma, das reads, k-mers, cobertura e temperatura.")
        print("0. Sair\n")

        escolha = input("Escolha um teste: ")
        manager = Gerenciador_de_Genomas()

        if escolha == '1':
            nome_arq = "genoma_escherichia_phage.txt"
            caminho = os.path.join("data", nome_arq)
            if not os.path.exists(caminho):
                print(" Arquivo de genoma não encontrado.")
                return
            genoma = Utils.ler_arquivo(caminho)
            read_size = 120
            k = 80
            cobertura = 0.7
            temperatura = 10
            nome_base = os.path.splitext(nome_arq)[0]

        elif escolha == '2':
            nome_arq = "genoma_tamanho_8.txt"
            caminho = os.path.join("data", nome_arq)
            genoma = Utils.ler_arquivo(caminho)
            read_size = 5
            k = 4
            cobertura = 1.0
            temperatura = 0
            nome_base = os.path.splitext(nome_arq)[0]

        elif escolha == '3':
            nome_arq = "genoma_tamanho_80.txt"
            caminho = os.path.join("data", nome_arq)
            genoma = Utils.ler_arquivo(caminho)
            read_size = 20
            k = 8
            cobertura = 1.0
            temperatura = 0
            nome_base = os.path.splitext(nome_arq)[0]

        elif escolha == '4':
            nome_arq = "genoma_tamanho_800.txt"
            caminho = os.path.join("data", nome_arq)
            genoma = Utils.ler_arquivo(caminho)
            read_size = 60
            k = 50
            cobertura = 1.0
            temperatura = 0
            nome_base = os.path.splitext(nome_arq)[0]

        elif escolha == '5':
            nome_arq = "genoma_tamanho_8000.txt"
            caminho = os.path.join("data", nome_arq)
            genoma = Utils.ler_arquivo(caminho)
            read_size = 100
            k = 50
            cobertura = 1.0
            temperatura = 0
            nome_base = os.path.splitext(nome_arq)[0]

        elif escolha == '6':
            nome_arq = "genoma_tamanho_80000.txt"
            caminho = os.path.join("data", nome_arq)
            genoma = Utils.ler_arquivo(caminho)
            read_size = 80
            k = 40
            cobertura = 1.0
            temperatura = 0
            nome_base = os.path.splitext(nome_arq)[0]

        elif escolha == '9':
            print("\n Parâmetros personalizados:")
            print("- Tamanho do Genoma: o tamanho do material genético original que vai ser reconstruído")
            print("- Tamanho das reads: quantidade de bases de cada segmento de leitura gerado a partir do genoma.")
            print("- Tamanho dos k-mers: número de bases em cada k-mer usado para criar o grafo.")
            print("- Cobertura: porcentagem do genoma que deve ser coberta pelas reads (ex: 1.0 cobre 100%).")
            print("- Temperatura: grau de variação aleatória no tamanho das reads (ex: 0 = sem variação).\n")
            try:
                tamanho_genoma = int(input(" Tamanho do genoma (ex: 100): "))
                read_size = int(input(" Tamanho das reads (ex: 30): "))
                k = int(input(" Tamanho dos k-mers (ex: 15): "))
                cobertura = float(input(" Cobertura (ex: 1.0 para 100%): "))
                temperatura = int(input(" Temperatura (ex: 0 para sem variação): "))
            except ValueError:
                print(" Entrada inválida. Use apenas números válidos.")
                return

            genoma = manager.gerar_genoma(tamanho_genoma)
            nome_base = f"genoma_personalizado_{tamanho_genoma}"

        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

        executar_reconstrucao_genomica(
            genoma=genoma,
            tamanho_read=read_size,
            k=k,
            salvar_resultados=True,
            nome_base=nome_base,
            cobertura=cobertura,
            temperatura=temperatura
        )

if __name__ == "__main__":
    main()
