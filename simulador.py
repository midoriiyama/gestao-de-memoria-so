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
            
            if isinstance(self.estrategia, Buddy):
                tamanho_bloco = 2
                while tamanho_bloco < requisicao.tamanho:
                    tamanho_bloco *= 2
                fim_log = ind_inicio + tamanho_bloco - 1
            else:
                fim_log = ind_inicio + requisicao.tamanho - 1
            
            
            self.logs.append(f"alocacao {particao.pid} {particao.inicio} {fim_log}")
            
            return True
            
    
    def liberar(self, requisicao: Requisicao):
        """
        """
        particao = self.tabela_particao.buscar_particao(requisicao.pid)
        
        if isinstance(self.estrategia, Buddy):
            self.estrategia.liberar_espaco(particao)
        
        for i in range(particao.inicio, particao.inicio + particao.tamanho):
            self.memoria.vetor[i] = None
        
        self.tabela_particao.remover_particao(particao)
        
        if isinstance(self.estrategia, Buddy):
            tamanho_bloco = 2
            while tamanho_bloco < particao.tamanho:
                tamanho_bloco *= 2
            fim_log = particao.inicio + tamanho_bloco - 1
        else:
            fim_log = particao.inicio + particao.tamanho - 1
        
        self.logs.append(f"liberacao {particao.pid} {particao.inicio} {fim_log}")
            
        
    def acessar(self, requisicao: Requisicao):
        
        particao = self.tabela_particao.buscar_particao(requisicao.pid)
        
        if isinstance(self.estrategia, Buddy):
            limite = 2
            while limite < particao.tamanho:
                limite *= 2
        else:
            limite = particao.tamanho
        
        resultado = self.mmu.traduzir_endereco(particao.inicio, requisicao.tamanho, limite)
        
        if resultado == -1:
            self.logs.append(f"acesso {particao.pid} {requisicao.tamanho} violacao")
            
        else:
            self.logs.append(f"acesso {particao.pid} {requisicao.tamanho} {resultado}")
            
    
    