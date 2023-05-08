from trie import Trie
def min_bytes_necessarios(n):
    if n == 0:
        return 1
    bits = n.bit_length()
    return (bits + 7) // 8


def escrever_binario(nome_arq_saida, codigos_bin):
    with open(nome_arq_saida, "wb") as f:
        for codigo in codigos_bin:
            f.write(codigo)

def comprimir_texto(nome_arq_entrada, nome_arq_saida):
    t = Trie()
    raiz = t.get_raiz()
    num_bytes_int = 0
    codigos = []

    with open(nome_arq_entrada, 'r') as f:
        maior_cadeia = ""
        while True:
            char = f.read(1)
            maior_cadeia += str(char)
            n = t.buscar_por_cadeia(raiz, maior_cadeia)
            if (n == None):
                indice, char = t.inserir(raiz, maior_cadeia)
                codigos.append((indice, char))
                ind_min_bytes = min_bytes_necessarios(indice)
                if (ind_min_bytes > num_bytes_int):
                    num_bytes_int = ind_min_bytes
                maior_cadeia = ""
            if not char:
                break
    num_bytes_int = max(num_bytes_int, min_bytes_necessarios(len(codigos)))
    print(codigos)
    codigos_bin = []
    while codigos:
        indice, char = codigos.pop(0)
        indice_bin = indice.to_bytes(num_bytes_int, byteorder= "big")
        codigos_bin.append(indice_bin)

    escrever_binario(nome_arq_saida,codigos_bin) 

    return t