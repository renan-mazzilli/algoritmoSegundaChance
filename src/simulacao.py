# simulacao.py
from memoria import Memoria

class SimulacaoSegundaChance:
    def __init__(self, paginas, quadros):
        self.paginas = paginas
        self.quadros = quadros
        self.memoria = Memoria(quadros)

    def iniciar_simulacao(self):
        print("\nIniciando a simulação...\n")
        for pagina in self.paginas:
            self.memoria.processar_pagina(pagina)
        self.memoria.exibir_resultado()
