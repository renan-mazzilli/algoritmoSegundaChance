def segunda_chance(paginas, quadros):
    memoria = []
    bits_de_uso = []
    ponteiro = 0

    print("\nIniciando a simulação...\n")
    faltas_de_pagina = 0
    
    for pagina in paginas:
        print(f"Processando página: {pagina}")
        
        # Caso a página já esteja na memória
        if pagina in memoria:
            indice = memoria.index(pagina)
            bits_de_uso[indice] = 1  
            print(f"Referência: {pagina} | Memória: {memoria} | Bits de Uso: {bits_de_uso}")
            continue

        # Caso seja uma falta de página
        if len(memoria) < quadros:
            memoria.append(pagina)
            bits_de_uso.append(1)  
            faltas_de_pagina += 1 
            print(f"Referência: {pagina} | Memória: {memoria} | Bits de Uso: {bits_de_uso}")
        else:
            # Substituição de página com a lógica da Segunda Chance
            while True:
                print(f"Tentativa: Página {memoria[ponteiro]} | Bits de Uso: {bits_de_uso}")
                
                if bits_de_uso[ponteiro] == 0:
                    # Substituir página
                    print(f"Substituindo página {memoria[ponteiro]} por {pagina}")
                    memoria[ponteiro] = pagina
                    bits_de_uso[ponteiro] = 1  
                    ponteiro = (ponteiro + 1) % quadros
                    faltas_de_pagina += 1 
                    break
                else:
                    # Dá uma segunda chance e avança o ponteiro
                    bits_de_uso[ponteiro] = 0
                    ponteiro = (ponteiro + 1) % quadros

            print(f"Referência: {pagina} | Memória: {memoria} | Bits de Uso: {bits_de_uso}")
    
    print("\nFinal:")
    print(f"Memória: {memoria} | Bits de Uso: {bits_de_uso}")
    print(f"Total de faltas de página: {faltas_de_pagina}")


# Função para receber entradas do usuário
def obter_entradas():
    quadros = int(input("Digite o número de quadros de memória: "))
    paginas_input = input("Digite as referências de páginas separadas por espaço: ")
    paginas = list(map(int, paginas_input.split()))
    
    return paginas, quadros

# Função principal
def main():
    paginas, quadros = obter_entradas()
    segunda_chance(paginas, quadros)

if __name__ == "__main__":
    main()
