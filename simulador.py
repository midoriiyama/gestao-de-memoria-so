from dataclasses import dataclass
from componentes import *

@dataclass
class Simulador:
    def __init__(self, estrategia):
        self.memoria: Memoria = Memoria()
        self.processos: list[Processo] = []
        self.mmu: MMU = MMU()
        self.estategia = estrategia

    