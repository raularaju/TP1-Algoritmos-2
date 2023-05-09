from trie import Trie
def min_bits_necessarios_int(n):
    if n == 0 or n == 1:
        return 8
    num_bits = n.bit_length()
    num_bits += 7
    return num_bits - (num_bits % 8)

def min_bits_necessarios_char(c):
    num_bits  = len(format(ord(c), '08b'))
    num_bits += 7
    return num_bits - (num_bits % 8)
    
def escrever_binario(nome_arq_saida, codigos_bin):
    with open(nome_arq_saida, "wb") as f:
        for codigo in codigos_bin:
            f.write(codigo)

def tranformar_str_em_byte_arr(string_bits):
    return int(string_bits, 2).to_bytes((len(string_bits) + 7) // 8, byteorder='big')

def comprimir_texto(nome_arq_entrada, nome_arq_saida):
    t = Trie()
    raiz = t.get_raiz()
    num_bits_int = 0
    num_bits_char = 0
    codigos = []
    with open(nome_arq_entrada, 'r') as f:
        maior_cadeia = ""
        while True:
            char = f.read(1)
            maior_cadeia += str(char)
            n = t.buscar_por_cadeia(raiz, maior_cadeia)
            if (n == None):
                indice, char = t.inserir(raiz, maior_cadeia)
                char_min_bits = min_bits_necessarios_char(char)
                if(char_min_bits > num_bits_char):
                    num_bits_char = char_min_bits
                codigos.append((indice, char))
                ind_min_bits = min_bits_necessarios_int(indice)
                if (ind_min_bits > num_bits_int):
                    num_bits_int = ind_min_bits
                maior_cadeia = ""
            if not char:
                break
    num_bits_int = max(num_bits_int, min_bits_necessarios_int(len(codigos)))
    num_bits_int_bin = str(bin(num_bits_int)[2:]).rjust(8, '0')
    num_bits_char_bin = str(bin(num_bits_char)[2:]).rjust(8, '0')

    with open(nome_arq_saida, "wb") as f:
        f.write(tranformar_str_em_byte_arr(num_bits_int_bin+num_bits_char_bin))
        for indice, char in  codigos:
            char_bin = format(ord(char[-1]), '08b').rjust(num_bits_char, '0')
            indice_bin = str(bin(indice)[2:]).rjust(num_bits_int, '0')
            code_bin = indice_bin + char_bin
            code_bin_byte_array = tranformar_str_em_byte_arr(code_bin)
            f.write(code_bin_byte_array)
    return t