from trie import Trie
def descomprimir_binario(nome_arq_bin: str, nome_arq_saida: str):
    dicionario = Trie()
    raiz = dicionario.get_raiz()
    with open(nome_arq_bin, "rb") as arq_bin,open(nome_arq_saida, "w") as arq_saida:
        num_bytes_ind = ord(arq_bin.read(1))
        num_bytes_char = ord(arq_bin.read(1))
       
        while True:
            indice_bytes = (arq_bin.read(num_bytes_ind))
            if not indice_bytes:
                break
            indice =  int.from_bytes(indice_bytes, byteorder='big')
            char_byte = arq_bin.read(num_bytes_char)
            char = int.from_bytes(char_byte, byteorder='big', signed=False)
            char = chr(char) 
            cadeia = dicionario.buscar_por_indice(indice)
            dicionario.inserir(raiz, cadeia+char)
            arq_saida.write("".join([cadeia + char]))
            """ cadeia = dicionario.buscar_por_indice(raiz, indice)
            arq_saida.write(cadeia + char) """
