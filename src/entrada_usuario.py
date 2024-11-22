# entrada_usuario.py
class EntradaUsuario:
    @staticmethod
    def obter_entradas():
        quadros = int(input("Digite o número de quadros de memória: "))
        paginas_input = input("Digite as referências de páginas separadas por espaço: ")
        paginas = list(map(int, paginas_input.split()))
        
        return paginas, quadros
