import sys

def ler_arquivo(caminho: str) -> tuple:
    """A função lê o arquivo de entrada e retorna os dados atrelados aos
    processos que farão parte da simulação.
    
    Args:
        caminho (str): O caminho do arquivo a ser lido.
    
    Returns:
        tuple: Uma tupla contendo três elementos:
            - num_processos (int): Quantidade total de processos.
            - lista_pid (list[str]): PIDs dos processos.
            - lista_processos (list[str]): Descrição dos processos.
    """
    num_processos = 0
    lista_pid = []
    lista_processos = []
    
    with open(caminho, "r") as arquivo:
        
        for numero_linha, linha in enumerate(arquivo, start=1):
            if numero_linha == 1:
                num_processos = int(linha)
            elif numero_linha == 2:
                lista_pid = linha.strip().split(";")
            else:
                lista_processos.append(linha.strip())

    return num_processos, lista_pid, lista_processos

def salvar_saida(saidas: list[str], caminho_saida: str):
    """
    
    """
    with open(caminho_saida, "w") as arquivo:
        pass

if __name__ == '__main__':
    
    # estrategia = sys.argv[1]
    # caminho_entrada = sys.argv[2]
    # caminho_saida = f"log_{caminho_entrada}_{estrategia}.txt"
    
    num_processos, lista_pid, lista_processos = ler_arquivo("exemplos_entrada\entrada001.txt")
    
    print(num_processos, lista_pid, lista_processos)
    
    # pid, ini, fim = simular()
    