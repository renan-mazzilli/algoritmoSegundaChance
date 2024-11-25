from fifo_clock import FIFOClock

# função pra simular o algoritmo fifo clock (segunda chance)
def simular_fifo_clock(capacidade, sequencia_paginas):
    memoria = FIFOClock(capacidade)
    # loop pra processar as páginas na sequência da fila
    for i, pagina in enumerate(sequencia_paginas):
        print(f"Iteração {i + 1}:")
        print(f"Referenciando a página: {pagina}")
        
        # substitui ou mantém a página na memória
        memoria.substituir(pagina)
        
        # exibe o estado da memória e os bits de referência
        memoria_atual = memoria.exibir_memoria()
        uso_bits = memoria.exibir_uso_bits()
        
        print("Memória atual (números das páginas):", memoria_atual)
        print("Bits de referência (R):", uso_bits)
        print("-" * 30)
    
    # Exibe o estado final após todas as iterações
    print("\nEstado final:")
    memoria_final = memoria.exibir_memoria()
    uso_bits_final = memoria.exibir_uso_bits()
    print("Memória final (apenas números das páginas):", memoria_final)
    print("Uso de bits (R) de cada página:", uso_bits_final)
    print(f"\nTotal de faltas de página: {memoria.faltas}")
