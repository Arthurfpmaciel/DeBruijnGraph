# Projeto Reconstrução Genômica com Grafos de De Bruijn

Este projeto implementa algoritmos para reconstrução genômica utilizando grafos de De Bruijn. Ele permite gerar genomas sintéticos, realizar benchmarks de desempenho e visualizar resultados.

## Estrutura de Pastas

- `benchmark.py` — Script para rodar benchmarks de desempenho da reconstrução genômica.
- `main.py` — Script principal para executar a reconstrução genômica em diferentes genomas.
- `requirements.txt` — Lista de dependências Python do projeto.
- `data/` — Contém arquivos de genomas de diferentes tamanhos usados como entrada.
- `resultados/` — Pasta de saída dos resultados:
  - `benchmark/` — Resultados e gráficos dos benchmarks.
  - `genoma_reconstruido/` — Genomas reconstruídos pelo algoritmo.
  - `imagens/` — Imagens dos grafos gerados.
  - `relatorio/` — Relatórios textuais dos experimentos.
- `src/` — Código-fonte principal do projeto:
  - `gerenciador.py` — Gerencia a geração e manipulação de genomas.
  - `grafo.py` — Implementação dos grafos de De Bruijn.
  - `pipeline.py` — Pipeline de execução da reconstrução genômica.
  - `utils.py` — Funções utilitárias.

## Como Executar

### 1. Crie um ambiente virtual e Instale as dependências

Abra o terminal na raiz do projeto e crie uma ambiente virtual executando:

```powershell
python -m venv venv
```

Ative o ambiente virtual:

```powershell
./venv/Scripts/activate
```

Instale as depedências do projeto:

```powershell
pip install -r requirements.txt
```


### 2. Executando o Benchmark

O script `benchmark.py` executa benchmarks de desempenho para diferentes tamanhos de genoma e gera gráficos e relatórios.

```powershell
python benchmark.py
```

Os resultados serão salvos em `resultados/benchmark/`.

### 3. Executando o Script Principal

O script `main.py` executa a reconstrução genômica padrão, utilizando os arquivos de entrada em `data/`.

```powershell
python main.py
```

Os resultados (genomas reconstruídos, imagens e relatórios) serão salvos nas subpastas de `resultados/`.

---

Para dúvidas ou sugestões, abra uma issue no repositório.
