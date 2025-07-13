import os
import time
import matplotlib.pyplot as plt
from src.pipeline import executar_reconstrucao_genomica
from src.gerenciador import Gerenciador_de_Genomas

# Função para rodar o benchmark de reconstrução genômica
def rodar_benchmark():
    tamanhos = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 80000]
    resultados_path = "resultados/benchmark/benchmark_reconstrucao.txt"
    os.makedirs("resultados", exist_ok=True)
    manager = Gerenciador_de_Genomas()

    tamanhos_genomas = []
    tempos_execucao = []
    ks_usados = []

    with open(resultados_path, "w") as f:
        f.write("# Benchmark da reconstrução genômica com grafos de De Bruijn\n")
        f.write("# Tamanho     Tempo (s)    k-usado\n")

        for tamanho in tamanhos:
            genoma = manager.gerar_genoma(tamanho)
            read_size = max(8, int(tamanho * 0.3))
            k = max(4, int(read_size * 0.5))
            cobertura = 1.0
            temperatura = 0

            tempos = []
            for _ in range(3):
                inicio = time.perf_counter()
                executar_reconstrucao_genomica(
                    genoma=genoma,
                    tamanho_read=read_size,
                    k=k,
                    salvar_resultados=False,
                    nome_base=f"benchmark_{tamanho}",
                    cobertura=cobertura,
                    temperatura=temperatura
                )
                fim = time.perf_counter()
                tempos.append(fim - inicio)

            tempo_medio = sum(tempos) / len(tempos)
            f.write(f"{tamanho:8}   {tempo_medio:.6f}    {k}\n")
            print(f"Tamanho {tamanho:6} | Tempo médio: {tempo_medio:.4f} s | k = {k}")

            tamanhos_genomas.append(tamanho)
            tempos_execucao.append(tempo_medio)
            ks_usados.append(k)

    return tamanhos_genomas, tempos_execucao, ks_usados

# Função para plotar os gráficos do benchmark
def plotar_graficos(tamanhos, tempos, ks):
    plt.figure(figsize=(15, 8))

    plt.subplot(1, 2, 1)
    plt.plot(tamanhos, tempos, marker='o', color='blue', linewidth=2)
    plt.title("Tempo de Execução vs Tamanho da Amostra\n(k = 50% do read)", fontsize=16)
    plt.xlabel("Tamanho da Amostra", fontsize=14)
    plt.ylabel("Tempo (s)", fontsize=14)
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.bar([str(t) for t in tamanhos], ks, color='orange')
    plt.title("Tamanho da Amostra vs Valor de k Usado", fontsize=16)
    plt.xlabel("Tamanho da Amostra", fontsize=14)
    plt.ylabel("Valor de k", fontsize=14)
    plt.grid(axis='y')

    plt.tight_layout()
    plt.savefig("resultados/benchmark/benchmark_grafico.png")
    plt.show()

if __name__ == "__main__":
    tamanhos, tempos, ks = rodar_benchmark()
    plotar_graficos(tamanhos, tempos, ks)
