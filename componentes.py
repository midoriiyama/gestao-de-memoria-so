from dataclasses import dataclass

TAMANHO_MEMORIA = 4096

@dataclass
class Memoria:
    def __init__(self):
        pass

@dataclass
class MMU:
    def __init__(self):
        pass

@dataclass
class Processo:
    def __init__(self, pid: str, ini: int, fim: int):
        self.pid = pid
        self.ini = ini
        self.fim = fim