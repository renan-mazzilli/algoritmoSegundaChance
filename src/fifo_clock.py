from pagina import Pagina

class FIFOClock:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = []  
        self.indice = 0
        self.faltas = 0

    def consultar(self, numero_pagina):
        for pagina in self.fila:
            if pagina.numero == numero_pagina:
                pagina.R = 1
                return True
        return False

    def substituir(self, numero_pagina):
        if not self.consultar(numero_pagina):
            self.faltas += 1
            if len(self.fila) < self.capacidade:
                nova_pagina = Pagina(numero_pagina)
                self.fila.append(nova_pagina)
            else:
                while True:
                    pagina = self.fila[self.indice]
                    if pagina.R == 0:
                        self.fila[self.indice] = Pagina(numero_pagina)
                        self.indice = (self.indice + 1) % self.capacidade
                        return
                    else:
                        pagina.R = 0
                        self.indice = (self.indice + 1) % self.capacidade
                        continue

    def exibir_memoria(self):
        return [pagina.numero for pagina in self.fila]

    def exibir_uso_bits(self):
        return [pagina.R for pagina in self.fila]
