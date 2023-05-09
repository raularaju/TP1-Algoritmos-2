class No:
    def __init__(self, indice: int, caracter: str):
        self.indice = indice
        self.caracter = caracter
        self.filhos: list[No] = []
    def __str__(self):
        return f"({self.indice},{self.caracter})"
    
class Trie:
    def __init__(self):
        self.raiz = No(0, "")
        self.ultimo_indice = 0
    def get_raiz(self):
        return self.raiz
    def buscar_por_indice(self, inicio: No, indice: int, cadeia = "") -> str:
        if(inicio.indice == indice):
            return cadeia + inicio.caracter
        if(len(inicio.filhos) == 0):
            return ""     
        elif(len(inicio.filhos) != 0):
            for filho in inicio.filhos:
                r_busca_filho = self.buscar_por_indice(filho, indice, cadeia + inicio.caracter)
                if (r_busca_filho != ""):
                    return r_busca_filho
        return ""
    def buscar_por_cadeia(self, inicio: No, cadeia: str) -> No:
        if(cadeia == ""):
            return inicio

        for filho in inicio.filhos:
            if(filho.caracter == cadeia):
                return filho
            elif(cadeia.startswith(filho.caracter)):
                return self.buscar_por_cadeia(filho, cadeia[1:])
    def get_antecessor(self, inicio: No, cadeia: str) -> No:
        """ if(inicio.caracter == cadeia):
            return None """
        for filho in inicio.filhos:
            if(filho.caracter == cadeia):
                return inicio
            elif(cadeia.startswith(filho.caracter)):
                return self.get_antecessor(filho, cadeia[1:])
        return inicio

    """ def inserir(self, inicio: No, nova_cadeia: str) -> No:
        if(inicio.caracter == nova_cadeia):
            return
        if(inicio.indice != 0 and nova_cadeia == ""):
            return
        tem_match = False
        for filho in inicio.filhos:
            if(nova_cadeia.startswith(filho.caracter)):
                tem_match = True
                return self.inserir(filho, nova_cadeia[1:])
                return
        if(not tem_match):
            self.ultimo_indice+=1
            novo_no = No(self.ultimo_indice, nova_cadeia)
            inicio.filhos.append(novo_no)
            return novo_no """
    def inserir(self, inicio: No, nova_cadeia: str) -> No:
        """ if(inicio.caracter == nova_cadeia):
            return """
        if(nova_cadeia == ""):
            return
        tem_match = False
        for filho in inicio.filhos:
            if(nova_cadeia.startswith(filho.caracter)):
                tem_match = True
                return self.inserir(filho, nova_cadeia[1:])
        if(not tem_match):
            self.ultimo_indice+=1
            novo_no = No(self.ultimo_indice, nova_cadeia)
            inicio.filhos.append(novo_no)
            return inicio.indice, nova_cadeia[-1]

""" t = Trie()
raiz = t.get_raiz()
t.inserir(raiz, "a")
t.inserir(raiz, "a")
t.inserir(raiz, "ab")
t.inserir(raiz, "b")
t.inserir(raiz, "ac")
t.inserir(raiz, "bc")
n = t.buscar_por_indice(raiz, 4)
print(n) """