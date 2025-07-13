import time
from src.gerenciador import Gerenciador_de_Genomas
from src.utils import Utils
from src.grafo import *

manager = Gerenciador_de_Genomas()

def executar_reconstrucao_genomica(genoma, tamanho_read, k, cobertura=1.0, temperatura=0, salvar_resultados=False, nome_base="teste"):
    start = time.time()
    print(f"Tamanho do Genoma Original: {len(genoma)}")

    reads = manager.gerar_reads(genoma, tamanho_read, cobertura=cobertura, temperatura=temperatura)
    print(f"Foram gerados {len(reads)} reads de tamanho aproximado {tamanho_read} com cobertura {cobertura} e temperatura {temperatura}")

    kmers = manager.gerar_kmers(reads, k)
    print(f"Foram gerados {len(kmers)} k-mers de tamanho {k}")

    grafo = gerar_grafo_de_DeBruijn(kmers)

    if grafo.number_of_nodes() == 0:
        print("Grafo vazio. Abordagem abortada.")
        return grafo, None, 0

    if tem_caminho_euleriano(grafo):
        caminho = obter_caminho_euleriano(grafo)
        genoma_reconstruido = manager.reconstruir_genoma(caminho)
        tempo = time.time() - start
        print("Genoma final reconstruído com sucesso.")
        print(f"Tempo de execução: {round(tempo, 4)} segundos")

        if salvar_resultados:
            imagem_path = f"resultados/imagens/{nome_base}_grafo.png"
            txt_path = f"resultados/{nome_base}_reconstruido.txt"
            relatorio_path = f"resultados/{nome_base}_relatorio.txt"

            desenhar_grafo(grafo, caminho_saida=imagem_path)
            Utils.salvar_arquivo(genoma_reconstruido, txt_path)

            similaridade = manager.comparar_genomas(genoma, genoma_reconstruido)
            relatorio = (
                f"Genoma: {nome_base}\n"
                f"Tamanho original: {len(genoma)}\n"
                f"Tamanho reconstruído: {len(genoma_reconstruido)}\n"
                f"Read: {tamanho_read}, k-mer: {k}\n"
                f"Cobertura: {cobertura}, Temperatura: {temperatura}\n"
                f"Similaridade: {similaridade:.2%}\n"
                f"Tempo: {tempo:.4f} segundos\n"
            )
            Utils.salvar_resultado(relatorio, relatorio_path)
            print(f"Relatório e imagem salvos como '{nome_base}'")

        return grafo, genoma_reconstruido, tempo

    else:
        print("O grafo não possui caminho Euleriano.")
        return grafo, None, 0
