from trie import Trie
def descomprimir_binario(nome_arq_bin: str, nome_arq_saida: str, num_codigos: int, num_bytes_int: int, dicionario: Trie):
    raiz = dicionario.get_raiz()
    arq_saida = open(nome_arq_saida, "a")
    with open(nome_arq_bin, "rb") as arq_bin:
        while True:
            char_bytes = arq_bin.read(4)
            if not char_bytes:
                break
            char = char_bytes.decode('utf-16')
            indice_bytes = arq_bin.read(num_bytes_int)
            indice = int.from_bytes(indice_bytes, byteorder='big')
            cadeia = dicionario.buscar_por_indice(raiz, indice)
            arq_saida.write(cadeia + char)
    arq_saida.close()
