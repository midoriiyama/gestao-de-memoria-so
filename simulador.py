from componentes import *
from estrategias import *

class SistemaOperacional:

    def __init__(self, lista_requisicao: list[Requisicao], estrategia):
        self.memoria: Memoria = Memoria()
        self.requisicoes: list[Requisicao] = lista_requisicao
        self.mmu: MMU = MMU()
        self.tabela_particao: TabelaParticao = TabelaParticao()
        self.estrategia = estrategia
        self.logs: list[str] = []

    def simular(self):
        """
        """
        for requisicao in self.requisicoes:
            
            if requisicao.operacao == "aloca":
                funfou = self.alocar(requisicao)
                if not funfou:
                    break
                
            elif requisicao.operacao == "libera":
                self.liberar(requisicao)
                
            elif requisicao.operacao == "acessa":
                self.acessar(requisicao)
        
        return self.logs

    
    def alocar(self, requisicao: Requisicao):
        """
        """
        ind_inicio = self.estrategia.encontrar_espaco(self.memoria, requisicao.tamanho)
        
        if ind_inicio == -1:
            self.logs.append(f"alocacao {requisicao.pid} erro!")
            
            return False
            
        else:
            for i in range(ind_inicio, ind_inicio + requisicao.tamanho):
                self.memoria.vetor[i] = requisicao.pid
            
            particao = Particao(requisicao.pid, ind_inicio, requisicao.tamanho)
            self.tabela_particao.inserir_particao(particao)
            
            self.logs.append(f"alocacao {particao.pid} {particao.inicio} {particao.inicio + particao.tamanho - 1}")
            
            return True
            
    
    def liberar(self, requisicao: Requisicao):
        """
        """
        particao = self.tabela_particao.buscar_particao(requisicao.pid)
        
        for i in range(particao.inicio, particao.inicio + particao.tamanho):
                self.memoria.vetor[i] = None
        
        if isinstance(self.estrategia, Buddy):
            self.estrategia.liberar_espaco(particao)

        self.tabela_particao.remover_particao(particao)
        
        self.logs.append(f"liberacao {particao.pid} {particao.inicio} {particao.inicio + particao.tamanho - 1}")
            
        
    def acessar(self, requisicao: Requisicao):
        
        particao = self.tabela_particao.buscar_particao(requisicao.pid)
        resultado = self.mmu.traduzir_endereco(particao.inicio, requisicao.tamanho, particao.tamanho)
        
        if resultado == -1:
            self.logs.append(f"acesso {particao.pid} {requisicao.tamanho} violacao")
            
        else:
            self.logs.append(f"acesso {particao.pid} {requisicao.tamanho} {resultado}")
            
    
    