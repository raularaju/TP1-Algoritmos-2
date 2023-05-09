from trie import Trie
def min_bytes_necessarios_int(n):
    if n == 0:
        return 1
    num_bits = n.bit_length()
    return (num_bits + 7) // 8

def min_bytes_necessarios_char(c):
    num_bits  = len(format(ord(c), '08b'))
    return (num_bits + 7) // 8
    
def escrever_binario(nome_arq_saida, codigos_bin):
    with open(nome_arq_saida, "wb") as f:
        for codigo in codigos_bin:
            f.write(codigo)

def tranformar_str_em_byte_arr(string_bits):
    return int(string_bits, 2).to_bytes((len(string_bits) + 7) // 8, byteorder='big')

def comprimir_texto(nome_arq_entrada, nome_arq_saida):
    t = Trie()
    raiz = t.get_raiz()
    num_bytes_int = 0
    num_bytes = 0
    codigos = []
    n = None
    with open(nome_arq_entrada, 'r') as f:
        maior_cadeia = ""
        while True:
            c_arquivo = f.read(1) 
            maior_cadeia += str(c_arquivo)
            n = t.buscar_por_cadeia(raiz, maior_cadeia)
            if (n == None or not c_arquivo):
                indice, char = t.inserir(raiz, maior_cadeia)
                codigos.append((indice, char))
                if(not char):
                    break
                char_min_bytes = min_bytes_necessarios_char(char)
                if(char_min_bytes > num_bytes):
                    num_bytes = char_min_bytes
                ind_min_bytes = min_bytes_necessarios_int(indice)
                if (ind_min_bytes > num_bytes_int):
                    num_bytes_int = ind_min_bytes
                maior_cadeia = ""
            if not char:
                break
    num_bytes_int = max(num_bytes_int, min_bytes_necessarios_int(len(codigos)))
    num_bytes_int_bin = str(bin(num_bytes_int)[2:]).rjust(8, '0')
    num_bytes_bin = str(bin(num_bytes)[2:]).rjust(8, '0')
    with open(nome_arq_saida, "wb") as f:
        f.write(tranformar_str_em_byte_arr(num_bytes_int_bin+num_bytes_bin))
        for indice, char in  codigos:
            char_bin = ''
            if(not char):
                char_bin = '0' * num_bytes * 8
            else:
                char_bin = format(ord(char[-1]), '08b').rjust(num_bytes * 8, '0')
            indice_bin = str(bin(indice)[2:]).rjust(num_bytes_int * 8, '0')
            code_bin = indice_bin + char_bin
            code_bin_byte_array = tranformar_str_em_byte_arr(code_bin)
            f.write(code_bin_byte_array)
