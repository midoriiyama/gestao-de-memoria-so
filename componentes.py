TAMANHO_MEMORIA = 4096 

class Memoria:
    def __init__(self):
        self.vetor: list = [None] * TAMANHO_MEMORIA


class MMU:
    def traduzir_endereco(self, endereco_base: int, endereco_logico: int, limite: int) -> int:
        """
        """
        if endereco_logico < limite:
            return endereco_base + endereco_logico
        else:
            return -1
        

class TabelaParticao:
    def __init__(self):
        self.tabela_particao: list[Particao] = []
    
    def inserir_particao(self, particao):
        """
        """
        self.tabela_particao.append(particao)
    
    def remover_particao(self, particao):
        """
        """
        self.tabela_particao.remove(particao)
    
    def buscar_particao(self, pid: str):
        """
        """
        for particao in self.tabela_particao:
            if particao.pid == pid:
                return particao
            
        return -1


class Particao:
    def __init__(self, pid: str, inicio: int, tamanho: int):
        self.pid: str = pid
        self.inicio: int = inicio
        self.tamanho: int = tamanho


class Requisicao:
    def __init__(self, operacao: str, pid: str, tamanho: int):
        self.operacao: str = operacao
        self.pid: str = pid
        self.tamanho: int = tamanho