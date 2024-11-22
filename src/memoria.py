# memoria.py
class Memoria:
    def __init__(self, quadros):
        self.quadros = quadros
        self.memoria = []
        self.bits_de_uso = []
        self.ponteiro = 0
        self.faltas_de_pagina = 0

    def processar_pagina(self, pagina):
        print(f"Processando página: {pagina}")

        # Caso a página já esteja na memória
        if pagina in self.memoria:
            indice = self.memoria.index(pagina)
            self.bits_de_uso[indice] = 1  # Atualiza o bit de uso
            print(f"Referência: {pagina} | Memória: {self.memoria} | Bits de Uso: {self.bits_de_uso}")
            return

        # Caso seja uma falta de página
        if len(self.memoria) < self.quadros:
            self.memoria.append(pagina)
            self.bits_de_uso.append(1)  # Inicializa o bit de uso para 1
            self.faltas_de_pagina += 1
            print(f"Referência: {pagina} | Memória: {self.memoria} | Bits de Uso: {self.bits_de_uso}")
        else:
            # Substituição de página com a lógica da Segunda Chance
            while True:
                print(f"Tentativa: Página {self.memoria[self.ponteiro]} | Bits de Uso: {self.bits_de_uso}")
                
                if self.bits_de_uso[self.ponteiro] == 0:
                    # Substituir página
                    print(f"Substituindo página {self.memoria[self.ponteiro]} por {pagina}")
                    self.memoria[self.ponteiro] = pagina
                    self.bits_de_uso[self.ponteiro] = 1
                    self.ponteiro = (self.ponteiro + 1) % self.quadros
                    self.faltas_de_pagina += 1
                    break
                else:
                    # Dá uma segunda chance e avança o ponteiro
                    self.bits_de_uso[self.ponteiro] = 0
                    self.ponteiro = (self.ponteiro + 1) % self.quadros

            print(f"Referência: {pagina} | Memória: {self.memoria} | Bits de Uso: {self.bits_de_uso}")

    def exibir_resultado(self):
        print("\nFinal:")
        print(f"Memória: {self.memoria} | Bits de Uso: {self.bits_de_uso}")
        print(f"Total de faltas de página: {self.faltas_de_pagina}")
