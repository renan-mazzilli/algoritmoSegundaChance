# main.py
from entrada_usuario import EntradaUsuario
from simulacao import SimulacaoSegundaChance

def main():
    # Recebe as entradas do usuário
    paginas, quadros = EntradaUsuario.obter_entradas()
    
    # Inicia a simulação
    simulacao = SimulacaoSegundaChance(paginas, quadros)
    simulacao.iniciar_simulacao()


if __name__ == "__main__":
    main()
