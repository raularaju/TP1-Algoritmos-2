class No:
    def __init__(self, indice: int, caracter: str):
        self.indice = None
        self.caracter = None
        self.filhos: list[No] = []
    
class Trie:
    def __init__(self):
        self.raiz = No(0, "")
        self.ultimo_indice = 0
    def buscar(self, inicio: No, indice: int) -> No:
        if(inicio.indice == indice):
            return No
        if(len(inicio.filhos) != 0):
            for filho in inicio.filhos:
                self.buscar(filho, indice)
        else: 
            return None