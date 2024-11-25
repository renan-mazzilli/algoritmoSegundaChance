from fifo_clock import FIFOClock

# função pra simular o algoritmo fifo clock (segunda chance)
def simular_fifo_clock(capacidade, sequencia_paginas):
    memoria = FIFOClock(capacidade)
    # loop pra processar as paginas na sequencia da fila
    for pagina in sequencia_paginas:
        memoria.substituir(pagina)
    # usa as funções pra exibir o estado final da memoria
    memoria_final = memoria.exibir_memoria()
    uso_bits = memoria.exibir_uso_bits()

    # mostra os resultados
    print("Memória final:")
    print(memoria_final)
    print("Uso de bits (R) de cada página:")
    print(uso_bits)
    print(f"\nTotal de faltas de página: {memoria.faltas}")