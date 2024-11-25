from pagina import Pagina

class FIFOClock:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = []  
        self.indice = 0
        self.faltas = 0

    def consultar(self, numero_pagina):
        # loop para verificar se a pagina ja esta na memoria
        for pagina in self.fila:
            # se encontrada, define o bit R como 1
            if pagina.numero == numero_pagina:
                pagina.R = 1
                return True
        return False

    def substituir(self, numero_pagina):
        # se a pagina nao estiver na memoria adiciona +1 ao contador de faltas
        if not self.consultar(numero_pagina):
            self.faltas += 1
            if len(self.fila) < self.capacidade:
                # adiciona a nova pagina se tiver espaço na memoria
                nova_pagina = Pagina(numero_pagina)
                self.fila.append(nova_pagina)
            else:
                # caso contrario, faz o fifo clock (segunda chance)
                while True:
                    pagina = self.fila[self.indice]
                    if pagina.R == 0:
                        # substitui a pagina se o bit R for 0
                        self.fila[self.indice] = Pagina(numero_pagina)
                        self.indice = (self.indice + 1) % self.capacidade
                        return
                    else:
                        # reseta o bit e passa o ponteiro pra proxima pagina
                        pagina.R = 0
                        self.indice = (self.indice + 1) % self.capacidade
                        continue

    # função pra retornar os números que estão na memória no momento
    def exibir_memoria(self):
        return [pagina.numero for pagina in self.fila]

    # função pra retornar os bits de referencia R de todas as paginas
    def exibir_uso_bits(self):
        return [pagina.R for pagina in self.fila]
