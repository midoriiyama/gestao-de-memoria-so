TAMANHO_MEMORIA = 4096 

class Memoria:
    """
    Classe que representa a Memória Principal (RAM), possui tamanho *TAMANHO_MEMORIA*.
    """
    def __init__(self):
        self.vetor: list = [None] * TAMANHO_MEMORIA


class MMU:
    """
    Classe que representa a MMU. Realiza a tradução de endereço lógico para endereço físico.
    """
    def traduzir_endereco(self, endereco_base: int, endereco_logico: int, limite: int) -> int:
        if endereco_logico < limite:
            return endereco_base + endereco_logico
        else:
            return -1
        

class TabelaParticao:
    """
    Classe que representa a Tabela de Partição. Armazena o registro das partiçÕes já alocadas.
    """
    def __init__(self):
        self.tabela_particao: list[Particao] = []
    
    def inserir_particao(self, particao):
        self.tabela_particao.append(particao)
    
    def remover_particao(self, particao):
        self.tabela_particao.remove(particao)
    
    def buscar_particao(self, pid: str):
        for particao in self.tabela_particao:
            if particao.pid == pid:
                return particao
            
        return -1


class Particao:
    """
    Classe que representa Partições alocadas, é armazenada na tabela de partições.
    """
    def __init__(self, pid: str, inicio: int, tamanho: int):
        self.pid: str = pid
        self.inicio: int = inicio
        self.tamanho: int = tamanho


class Requisicao:
    """
    Classe que representa Requisições (Alocação, Liberação e Acesso) solicitadas por Processos.
    """
    def __init__(self, operacao: str, pid: str, tamanho: int):
        self.operacao: str = operacao
        self.pid: str = pid
        self.tamanho: int = tamanho