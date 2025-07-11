import networkx as nx
import matplotlib.pyplot as plt
import random
import time


class Gerenciador_de_Genomas:
    
    def __init__(self):
        self.bases = ['A', 'C', 'G', 'T']
    def gerar_genoma(self,tamanho, random_state=None):
        random.seed(random_state)
        genoma = ''.join(random.choice(self.bases) for _ in range(tamanho))
        return genoma
    
    def gerar_reads(self,genoma, tamanho_read, cobertura=1.0,temperatura=0,random_state=None):
        reads_totais = [genoma[i:i+random.choice(range(tamanho_read-temperatura,tamanho_read+temperatura+1))]
                        for i in range(len(genoma)-tamanho_read+1)]
        numero_de_reads = int(len(reads_totais)*cobertura)
        random.seed(random_state)
        reads_cobertos = random.sample(reads_totais,numero_de_reads)
        return reads_cobertos
    
    def gerar_kmers(self, reads, k):
        kmers = set()
        for read in reads:
            for i in range(len(read) - k + 1):
                kmear = read[i:i + k]
                kmers.add(kmear)
        return list(kmers)
    
    def gerar_grafo_de_DeBruijn(self, kmers):
        Graph = nx.DiGraph()
        Graph.add_nodes_from(kmers)
        prefixos =  [kmer[:-1] for kmer in kmers]
        sufixos = [kmer[1:] for kmer in kmers]
        for i in range(len(kmers)):
            for j in range(len(kmers)):
                if prefixos[j] == sufixos[i]:
                    Graph.add_edge(kmers[i], kmers[j])
        return Graph

    def desenhar_grafo(self, grafo):
        pos = nx.spring_layout(grafo)
        plt.figure(figsize=(8, 6))
        labels_encurtados = {}
        for node in grafo.nodes():
            if len(node) > 8:
                novo_label = node[:3] + "..." + node[-3:]
            else:
                novo_label = node
            labels_encurtados[node] = novo_label
        nx.draw(grafo, pos, labels=labels_encurtados,
                with_labels=True, node_size=1000,
                node_color='lightblue', font_size=8,
                font_color='black', font_weight='bold',
                arrows=True)

        plt.title("Grafo de De Bruijn")
        plt.show()

    def verificar_se_tem_caminho_euleriano(self,grafo):
        return nx.has_eulerian_path(grafo)
    
    def obter_caminho_euleriano(self,grafo):
        caminho_arestas = list(nx.eulerian_path(grafo))
        caminho = [i[0] for i in caminho_arestas] + [caminho_arestas[-1][1]]
        return caminho
    
    def reconstruir_genoma(self,caminho_euleriano):
        k = len(caminho_euleriano[0])
        novo_genoma = ""
        for i in range(len(caminho_euleriano)):
            if i == 0:
                novo_genoma += caminho_euleriano[i]
            else:
                novo_genoma += caminho_euleriano[i][k-1:]
        return novo_genoma
    
    def comparar_genormas(self,genoma1, genoma2):
        count = 0
        for i in range(len(genoma1)):
            if i > len(genoma2) -1:
                break
            if genoma1[i] == genoma2[i]:
                count +=1
        corr = count/len(genoma1)
        return corr
    
    def fundir_vertices(self,grafo,vertices):
        arestas_de_entrada = set()
        arestas_de_saida = set()
        novo_grafo = grafo.copy()
        for v in vertices:
            arestas_de_entrada = arestas_de_entrada.union(set(grafo.in_edges(v)))
            arestas_de_saida = arestas_de_saida.union(set(grafo.out_edges(v)))
        novo_grafo.remove_nodes_from(vertices)
        nome = self.reconstruir_genoma(vertices)
        arestas_de_entrada = [i for i in list(arestas_de_entrada) if not (i[0] in vertices and i[1] in vertices)]
        arestas_de_saida = [i for i in list(arestas_de_saida) if not (i[0] in vertices and i[1] in vertices)]
        novas_arestas_entrada = [(i[0],nome) for i in arestas_de_entrada]
        novas_arestas_saida = [(nome,i[1]) for i in arestas_de_saida]
        arestas = novas_arestas_entrada + novas_arestas_saida
        novo_grafo.add_node(nome)
        novo_grafo.add_edges_from(arestas)
        return novo_grafo, nome

    def simplificar_grafo(self,grafo, caminho):
        graus_de_entrada = [grafo.in_degree(i) for i in caminho]
        graus_de_saida = [grafo.out_degree(i) for i in caminho]
        pode_fundir = [graus_de_entrada[i]==1 and graus_de_saida[i]==1 for i in range(len(caminho))]
        grupos_de_fusao = []
        sec = 0
        for i in range(len(pode_fundir)):
            if pode_fundir[i]:
                sec +=1
                if sec ==1:
                    grupos_de_fusao.append([caminho[i]])
                else:
                    grupos_de_fusao[-1].append(caminho[i])
            else:
                sec = 0
        novo_grafo = grafo.copy()
        novos_nomes = []
        for i in grupos_de_fusao:
            novo_grafo,novo_nome = self.fundir_vertices(novo_grafo,i)
            novos_nomes.append(novo_nome)
        return novo_grafo,novos_nomes