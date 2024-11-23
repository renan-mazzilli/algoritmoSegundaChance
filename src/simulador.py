from fifo_clock import FIFOClock

def simular_fifo_clock(capacidade, sequencia_paginas):
    memoria = FIFOClock(capacidade)

    for pagina in sequencia_paginas:
        memoria.substituir(pagina)
    
    memoria_final = memoria.exibir_memoria()
    uso_bits = memoria.exibir_uso_bits()
    
    print("Memória final (apenas números das páginas):")
    print(memoria_final)
    print("Uso de bits (R) de cada página:")
    print(uso_bits)
    print(f"\nTotal de faltas de página: {memoria.faltas}")
