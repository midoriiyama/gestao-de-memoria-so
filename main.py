import sys
from componentes import *
from simulador import *
from estrategias import *

def ler_arquivo(caminho: str) -> tuple:
    """
    A função lê o arquivo de entrada e retorna os dados atrelados aos
    processos que farão parte da simulação.
    """
    num_processos = 0
    lista_requisicoes = []
    
    with open(caminho, "r") as arquivo:
        
        for numero_linha, linha in enumerate(arquivo, start=1):
            
            if numero_linha == 1:
                num_processos = int(linha)
                
            elif numero_linha == 2:
                lista_processos = linha.strip().split(";")
                
            else:
                aux = linha.split()

                if len(aux) == 3:
                    processo = Requisicao(aux[0], aux[1], int(aux[2]))
                    
                else:
                    processo = Requisicao(aux[0], aux[1], 0)
                    
                lista_requisicoes.append(processo)

    return num_processos, lista_processos, lista_requisicoes


def salvar_saida(saidas: list[str], caminho_saida: str):
    """
    """
    with open(caminho_saida, "w") as arquivo:
        
        for log in saidas:
            arquivo.write(log + "\n")
            

if __name__ == '__main__':
    
    estrat = sys.argv[1]
    caminho_entrada = sys.argv[2]

    caminho_saida = f"log_{caminho_entrada[:-4]}_{estrat}.txt"
    
    if estrat == "first":
        estrategia = FirstFit()
        
    elif estrat == "best":
        estrategia = BestFit()
        
    elif estrat == "worst":
        estrategia = WorstFit()
        
    elif estrat == "buddy":
        estrategia = Buddy()
        
    else:
        raise ValueError("Estratégia inválida!")
    
    num_processos, lista_processos, lista_requisicoes = ler_arquivo(caminho_entrada)
    
    simulador = SistemaOperacional(lista_requisicoes, estrategia)
    
    lista_logs = simulador.simular()
    
    salvar_saida(lista_logs, caminho_saida)
    