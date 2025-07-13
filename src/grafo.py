import networkx as nx
import matplotlib.pyplot as plt
import math

# gerar o grafo de De Bruijn a partir dos k-mers
def gerar_grafo_de_DeBruijn(kmers):
    Graph = nx.DiGraph()
    Graph.add_nodes_from(kmers)
    prefixos =  [kmer[:-1] for kmer in kmers]
    sufixos = [kmer[1:] for kmer in kmers]
    for i in range(len(kmers)):
        for j in range(len(kmers)):
            if prefixos[j] == sufixos[i]:
                Graph.add_edge(kmers[i], kmers[j])
    return Graph

# visualizar o grafo de De Bruijn e salvar como imagem
def desenhar_grafo(grafo, nome="Grafo de De Bruijn", caminho_saida=None):
    pos = nx.spring_layout(grafo)
    largura = max(8, min(0.5 * len(grafo.nodes), 30))
    altura = max(6, min(0.5 * len(grafo.nodes), 30))
    plt.figure(figsize=(largura, altura))

    labels_encurtados = {}
    for node in grafo.nodes():
        if len(node) > 8:
            novo_label = node[:3] + "..." + node[-3:]
        else:
            novo_label = node
        labels_encurtados[node] = novo_label

    nx.draw(
        grafo, pos,
        labels=labels_encurtados,
        with_labels=True,
        node_size=1000,
        node_color='lightblue',
        font_size=8,
        font_color='black',
        font_weight='bold',
        arrows=True
    )

    plt.title(nome)

    if caminho_saida:
        plt.savefig(caminho_saida, bbox_inches='tight')
        print(f"Imagem do grafo salva em {caminho_saida}")
    else:
        plt.show()

    plt.close()

# verificar se o grafo tem caminho euleriano
def tem_caminho_euleriano(grafo):
    return nx.has_eulerian_path(grafo)

# obter o caminho euleriano do grafo
def obter_caminho_euleriano(grafo):
    caminho_arestas = list(nx.eulerian_path(grafo))
    caminho = [a[0] for a in caminho_arestas] + [caminho_arestas[-1][1]]
    return caminho
