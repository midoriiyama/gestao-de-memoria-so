from componentes import *

class FirstFit:
    
    def encontrar_espaco(self, memoria: Memoria, tamanho: int):
        """
        Escolhe o primeiro espaço livre que satisfaz o pedido de alocação, a partir do endereço
        de memória menos significativo.
        """
        cont = 0
        total_memoria = len(memoria.vetor)
        
        for i in range(total_memoria):
            if memoria.vetor[i] is None:
                cont += 1
                if cont == tamanho:
                    return i - cont + 1
            else:
                cont = 0
        return -1
            

class BestFit:
    
    def encontrar_espaco(self, memoria: Memoria, tamanho: int):
        """
        Escolhe a menor área possível que pode receber a alocação.
        """ 
        menor = float('inf')
        indice_menor = -1
        cont = 0
        total_memoria = len(memoria.vetor)
        
        for i in range(total_memoria):
            if memoria.vetor[i] is None:
                cont += 1
            else:
                if cont >= tamanho and cont < menor:
                    indice_menor = i - cont
                    menor = cont
                cont = 0
        
        if cont >= tamanho and cont < menor:
            indice_menor = total_memoria - cont

        return indice_menor
            
    
class WorstFit:
    
    def encontrar_espaco(self, memoria: Memoria, tamanho: int):
        """
        Escolhe sempre a maior área possível.
        """ 
        maior = 0
        indice_maior = -1
        cont = 0
        total_memoria = len(memoria.vetor)
        
        for i in range(total_memoria):
            if memoria.vetor[i] is None:
                cont += 1
            else:
                if cont >= tamanho and cont > maior:
                    indice_maior = i - cont
                    maior = cont
                cont = 0
        
        if cont >= tamanho and maior < cont:
            indice_maior = total_memoria - cont

        return indice_maior    


class Buddy: 
    """
    Realiza a alocação e liberação por pares considerando blocos de tamanho 2^n, tal
    que 1 <= n <= 1, totalizando blocos mínimos de 2 UA e blocos máximos de 4096 UA.
    """ 
    def __init__(self):
        self.blocos_livres: list[tuple] = [(0, TAMANHO_MEMORIA)]
    
    def encontrar_espaco(self, memoria: Memoria, tamanho: int):
        """
        """
        tamanho_ideal = 2
        while tamanho_ideal < tamanho:
            tamanho_ideal *= 2
        
        menor_bloco = None
        
        for bloco in self.blocos_livres:
            if bloco[1] >= tamanho_ideal:
                if menor_bloco is None or bloco[1] < menor_bloco[1]:
                    menor_bloco = bloco
        
        if menor_bloco is None:
            return -1
        
        self.blocos_livres.remove(menor_bloco)
        
        while menor_bloco[1] > tamanho_ideal:
            menor_bloco = (menor_bloco[0], menor_bloco[1]//2)
            bloco_irmao = (menor_bloco[0] + menor_bloco[1], menor_bloco[1])
            self.blocos_livres.append(bloco_irmao)
        
        self.blocos_livres.sort()

        return menor_bloco[0]
    
    
    def liberar_espaco(self, particao: Particao):
        
        tamanho = particao.tamanho
        inicio = particao.inicio
        
        tamanho_bloco = 2
        while tamanho_bloco < tamanho:
            tamanho_bloco *= 2
        
        while tamanho_bloco < TAMANHO_MEMORIA:
            
            if (inicio // tamanho_bloco) % 2 == 0:
                inicio_irmao = inicio + tamanho_bloco
                
            else:
                inicio_irmao = inicio - tamanho_bloco
                
            bloco_irmao = (inicio_irmao, tamanho_bloco)
        
            if bloco_irmao in self.blocos_livres:
                
                self.blocos_livres.remove(bloco_irmao)
                inicio = min(inicio, inicio_irmao)
                tamanho_bloco *= 2
            
            else:
                break
 
        self.blocos_livres.append((inicio, tamanho_bloco))
        self.blocos_livres.sort()