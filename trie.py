class No:
    def __init__(self, indice: int, caracter: str):
        self.indice = indice
        self.caracter = caracter
        self.filhos: list[No] = []
    
class Trie:
    def __init__(self):
        self.raiz = No(0, "")
        self.ultimo_indice = 0
    def get_raiz(self):
        return self.raiz
    def buscar_por_indice(self, inicio: No, indice: int) -> No:
        if(inicio.indice == indice):
            return No
        elif(len(inicio.filhos) != 0):
            for filho in inicio.filhos:
                return self.buscar(filho, indice)

    def buscar_por_cadeia(self, inicio: No, cadeia: str) -> No:
        if(inicio.caracter == cadeia):
            return inicio

        for filho in inicio.filhos:
            if(filho.caracter == cadeia):
                return filho
            elif(cadeia.startswith(filho.caracter)):
                return self.buscar_por_cadeia(filho, cadeia[1:])

    def inserir(self, inicio: No, nova_cadeia: str) -> None:
        if(inicio.caracter == nova_cadeia):
            return
        if(inicio.indice != 0 and nova_cadeia == ""):
            return
        tem_match = False
        for filho in inicio.filhos:
            if(nova_cadeia.startswith(filho.caracter)):
                tem_match = True
                self.inserir(filho, nova_cadeia[1:])
        if(not tem_match):
            self.ultimo_indice+=1
            novo_no = No(self.ultimo_indice, nova_cadeia)
            inicio.filhos.append(novo_no)

t = Trie()
raiz = t.get_raiz()
t.inserir(raiz, "a")
t.inserir(raiz, "a")
t.inserir(raiz, "ab")
t.inserir(raiz, "b")
t.inserir(raiz, "ac")
t.inserir(raiz, "bc")
n = t.buscar_por_cadeia(raiz,"ab")
print(raiz.filhos)