import networkx as nx
import matplotlib.pyplot as plt

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

def desenhar_grafo(grafo, nome="Grafo de De Bruijn", caminho_saida=None):
    pos = nx.spring_layout(grafo)
    plt.figure(figsize=(8, 6))
    
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

def tem_caminho_euleriano(grafo):
    return nx.has_eulerian_path(grafo)

def obter_caminho_euleriano(grafo):
    caminho_arestas = list(nx.eulerian_path(grafo))
    caminho = [a[0] for a in caminho_arestas] + [caminho_arestas[-1][1]]
    return caminho
