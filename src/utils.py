class Utils:
    @staticmethod
    def ler_arquivo(caminho_arquivo):
        # Lê um arquivo contendo uma sequência de DNA e retorna a sequência como uma única string.
        with open(caminho_arquivo, "r") as f:
            genoma = f.read().replace("\n", "")
        return genoma

    @staticmethod
    def salvar_arquivo(sequencia, caminho_arquivo):
        # Salva uma sequência genômica em um arquivo.
        with open(caminho_arquivo, "w") as f:
            f.write(sequencia)

    @staticmethod
    def salvar_resultado(resultado, caminho_arquivo):
        # Salva um resultado genérico (ex: log ou métrica) em um arquivo.
        with open(caminho_arquivo, "w") as f:
            f.write(str(resultado))