from simulador import simular_fifo_clock

def main():
    capacidade = int(input("Digite o número de quadros na memória: "))
    sequencia_input = input("Digite a sequência de páginas de referência separadas por espaço: ")
    sequencia_paginas = [int(pagina) for pagina in sequencia_input.split()]
    
    simular_fifo_clock(capacidade, sequencia_paginas)

if __name__ == "__main__":
    main()
