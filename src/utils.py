class Utils:
    @staticmethod
    # Lê um arquivo contendo uma sequência de DNA e retorna a sequência como uma única string.
    def ler_arquivo(caminho_arquivo):
        with open(caminho_arquivo, "r") as f:
            genoma = f.read().replace("\n", "")
        return genoma

    @staticmethod
    # Salva uma sequência genômica em um arquivo.
    def salvar_arquivo(sequencia, caminho_arquivo):
        with open(caminho_arquivo, "w") as f:
            f.write(sequencia)

    @staticmethod
    # Salva um resultado genérico (ex: log ou métrica) em um arquivo.
    def salvar_resultado(resultado, caminho_arquivo):
        with open(caminho_arquivo, "w") as f:
            f.write(str(resultado))